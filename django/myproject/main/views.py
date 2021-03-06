from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from viewsFunctions.ProfilePage import getUserInfo, getUserAlerts, deleteUserMsg, updateFilter 
from viewsFunctions.UpdateProfilePage import updateUserInfo
from viewsFunctions.UpdateBillPage import updateBillInfo
from viewsFunctions.SponsorProfile import SponsorProfile, pullAdminProfile, pullSponsorProfile
from viewsFunctions.SponsorList import SponsorListItem, pulldownAdmins, pulldownSponsors
from viewsFunctions.AddFunctions import DriverPoints, DriverProfile, removeComp, pullDriverProfile, addPoints, addPointsAdmin, spPullDriverProfile, setPoints
from viewsFunctions.DriverList import DriverListItem, pulldownDrivers, adminPulldownDrivers, pullPendingDrivers, addTempUname, addTempUnameSponsor, getTempName, removeTempName, getTempNameSponsor
from viewsFunctions.PointsPerDollar import UpdatePVal, getID, pullCompanyProfile, drPullCompanyProfile, getPoints, pullAllCompanies, getSpCompany, getCompanySp
from viewsFunctions.NewUserReg import addUserInfo, addUserTypeInfo
from viewsFunctions.Account import verifyAccount
from viewsFunctions.CreateCompany import createCompany, joinCompany
from viewsFunctions.FindCompany import applyToCompany
from viewsFunctions.ApproveDriver import approveDriver, sendRemoveMessage
from viewsFunctions.AddToCart import addToCart, pulldownCart, removeFromCart, driverCheckout, sponsorCheckout, adminCheckout, getOutstandingPurchases, spGetOutstandingPurchases, cancelPurchase
from viewsFunctions.AdminReports import getDriverPurchaseHistory, listEmployers
from viewsFunctions.Reports import getSalesBySponsor, getSalesOverTime
from SponsorCatalog import searchGeneralAPI, updateCatalog, adminUpdateCatalog
from .forms import UserForm, UpdateForm, UpdatePass, UnameForm, AlertFilters
from django.contrib.auth.models import User

import mysql.connector

from datetime import datetime

def createAcc(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            
            #Fill in additional information in user database
            uname = user_form.cleaned_data.get('username')
            phone = user_form.cleaned_data.get('phone')
            address = user_form.cleaned_data.get('address')
            prefName = user_form.cleaned_data.get('prefName')
            addUserInfo(uname, prefName, phone, address)

            #Add user to their specific user type table            
            userType = user_form.cleaned_data.get('type_of_user_choices')
            userType = dict(user_form.fields['type_of_user_choices'].choices)[userType]
            addUserTypeInfo(uname, userType)
            return redirect('//54.88.218.67/')
    else:
        user_form = UserForm()
    return render(request, 'createAcc/register.html', {'user_form':user_form})


def home(request):
    loginUsername = request.user.username
    accType = verifyAccount(loginUsername)
    infoList = getUserInfo(loginUsername, accType)
    #if the user is a Driver
    if accType == "d":
        driverObj = pullDriverProfile(loginUsername)
        if request.method == 'POST':
            #The user is done seeing the website as a driver and wants to return to their view
            if request.POST.get("returntoview"):
                tempname = getTempName(loginUsername)
                removeTempName(loginUsername)
                logout(request)
                user = User.objects.get(username=tempname)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request,user)
                originalAccType = verifyAccount(tempname)
                if originalAccType == "s":
                    return render(request, 'homepage/sponsor_homepage.html')
                elif originalAccType == "a":
                    return render(request, 'homepage/admin_homepage.html')
            else:
                form = AlertFilters(request.POST)
                if form.is_valid():
                    pc = form.cleaned_data['pointChange']
                    oc = form.cleaned_data['orderCompletion']
                    oi = form.cleaned_data['orderIssue']
                    updateFilter(loginUsername, pc, oc, oi)
                    alerts = getUserAlerts(loginUsername, pc, oc, oi) 
                    for i in alerts:
                        if str(i.msgid) in request.POST:
                            deleteUserMsg(i.msgid)
                            alerts = getUserAlerts(loginUsername, pc, oc, oi)
                    return render(request, 'homepage/homepage.html', {'driverObj':driverObj,'form':form,'alerts':alerts})
        else:
            form = AlertFilters()
            alerts = getUserAlerts(loginUsername, True, True, True)
            return render(request, 'homepage/homepage.html', {'driverObj':driverObj,'form':form,'alerts':alerts})
    #If the User is a Sponsor
    elif accType == "s":
        if request.method == 'POST':
            #The Sponsor is trying to see the website as a driver
            if request.POST.get("changeviewd"):
                addTempUname(loginUsername)
                logout(request)
                dummyuser = authenticate(request,username='dummydriver',password='testing321')
                driverObj = pullDriverProfile('dummydriver')
                login(request,dummyuser)
                setPoints()
                return render(request, 'homepage/homepage.html', {'driverObj':driverObj})
            #an Admin is trying to return to their view
            elif request.POST.get("returntoview"):
                tempname = getTempNameSponsor(loginUsername)
                removeTempName(loginUsername)
                logout(request)
                user = User.objects.get(username=tempname)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request,user)
                originalAccType = verifyAccount(tempname)
                return render(request, 'homepage/admin_homepage.html')
        sponsorObj = pullSponsorProfile(loginUsername)
        return render(request, 'homepage/sponsor_homepage.html', {'sponsorObj':sponsorObj})
    #if the user is an Admin
    elif accType == "a":
        if request.method == 'POST':
            #the admin wants to see the page as a driver
            if request.POST.get("changeviewd"):
                addTempUname(loginUsername)
                logout(request)
                dummyuser = authenticate(request,username='dummydriver',password='testing321')
                driverObj = pullDriverProfile('dummydriver')
                login(request,dummyuser)
                setPoints()
                return render(request, 'homepage/homepage.html', {'driverObj':driverObj})
            #The admin wants to see the page as a sponsor
            elif request.POST.get("changeviews"):
                addTempUnameSponsor(loginUsername)
                logout(request)
                dummyuser = authenticate(request,username='dummysponsor',password='testing321')
                sponsorObj = pullSponsorProfile('dummysponsor')
                login(request,dummyuser)
                return render(request, 'homepage/sponsor_homepage.html', {'sponsorObj':sponsorObj})
        return render(request, 'homepage/admin_homepage.html')
    else:
        return redirect('//54.88.218.67')

def viewMyDrivers(request):
    if request.method == 'POST':
        sponsorUser = request.user.username
        driverUser = request.POST.get("username")
        currPoints = int(request.POST.get("point"))
        comp = getSpCompany(request.user.username)

        #Call this to remove Sponsorship
        if request.POST.get("revokeBut"):
            removeComp(driverUser, comp)
            sendRemoveMessage(driverUser)
        # Call this if it's an add
        elif request.POST.get("addBut"):
            nextPoints = int(request.POST.get("pointInput"))
            addPoints(sponsorUser, driverUser, currPoints, nextPoints, True)
        # Call this if it's a remove
        else:
            nextPoints = int(request.POST.get("pointInput"))
            addPoints(sponsorUser, driverUser, currPoints, nextPoints, False)
        return redirect('//54.88.218.67/home/drivers/')
    else:
        currentSponsor = request.user.username
        driverList = pulldownDrivers(currentSponsor)
        return render(request, 'points/driverList.html', {'driverList':driverList})

def viewAllDrivers(request):
    if request.method == 'POST':
        adminUser = request.user.username
        driverUser = request.POST.get("username")
        currPoints = int(request.POST.get("point"))
        nextPoints = int(request.POST.get("pointInput"))
        empID = int(request.POST.get("emp"))
        #if request.POST.get("RevokeBut"):
        #    sendRemoveMessage(driverUser)
        if request.POST.get("addBut"):
            addPointsAdmin(adminUser, driverUser, currPoints, nextPoints, True, empID)
        else:
            addPointsAdmin(adminUser, driverUser, currPoints, nextPoints, False, empID)
        return redirect('//54.88.218.67/home/all_drivers/')
    else:
        driverList = adminPulldownDrivers()
        return render(request, 'points/admin_driverList.html', {'driverList':driverList})

def viewAllSponsors(request):
    sponsorList = pulldownSponsors()
    if request.method == "POST":
        daUser = request.POST.get('uname')
       #accType = verifyAccount(daUser)
        sUser = getID(daUser)
    #companyProf = pullCompanyProfile(daUser)
    if request.POST.get("pointVal"):
        dollarValue = request.POST.get("pointVal")
        if dollarValue:
            UpdatePVal(sUser, dollarValue)
            sponsorList = pulldownSponsors()
    return render(request, 'points/sponsorList.html', {'sponsorList':sponsorList})

def viewAllAdmins(request):
    adminList = pulldownAdmins()
    return render(request, 'points/adminList.html', {'adminList':adminList})

def viewMyProfile(request):
    currentUser = request.user.username
    accType = verifyAccount(currentUser)
    infoList = getUserInfo(currentUser, accType)
    driverObj = pullDriverProfile(currentUser)
    if accType == "d":
        return render(request, 'profile/driver_profile.html', {'infoList':infoList,'driverObj':driverObj})
    elif accType == "s":
        return render(request, 'profile/sponsor_profile.html', {'infoList':infoList})
    elif accType == "a":
        return render(request, 'profile/admin_profile.html', {'infoList':infoList})
    else:
        return redirect('//54.88.218.67')

def viewDriverProfile(request):
    # Get the driver username from the GET params
    uname = request.GET['uname']
    sponsorUser = request.user.username
    driverObj = spPullDriverProfile(uname, sponsorUser)
    return render(request, 'profile/view_driver.html', {'driverObj':driverObj})

def adviewDriverProfile(request):
    if request.method == "GET":
        uname = request.GET['uname']
        driverObj = pullDriverProfile(uname)
    if request.POST.get("compID"):
        empID = request.POST.get("compID")
        uname = request.POST.get("username")
        removeComp(uname, empID)
        driverObj = pullDriverProfile(uname)
    return render(request, 'profile/admin_view_driver.html', {'driverObj':driverObj})

def adviewSponsorProfile(request):
    uname = request.GET['uname']
    sponsorObj = pullSponsorProfile(uname)
    return render(request, 'profile/admin_view_sponsor.html', {'sponsorObj':sponsorObj})

def adviewAdminProfile(request):
    uname = request.GET['uname']
    adminObj = pullAdminProfile(uname)
    return render(request, 'profile/admin_view_admin.html', {'adminObj':adminObj})

def updateBill(request):
    if request.method == "POST":
        daUser = request.POST.get['uname']
        sUser = getID(daUser)
        endDate = "11/21/2020"
        total = 412
        paid = "No"
        companyProf = pullCompanyProfile(daUser)
        bill = UpdateBillInfo(sUser,endDate,total,paid)
        return render(request, 'profile/updateBill.html', {'companyProf':companyProf}) 

def adminUpdatePointValue(request):
    daUser = ""
    if request.method == "POST":
        daUser = request.POST.get('uname')
    accType = verifyAccount(daUser)
    sUser = getID(daUser)
    companyProf = pullCompanyProfile(daUser)
    if request.POST.get("pointVal"):
        dollarValue = request.POST.get("pointVal")
    if dollarValue:
        UpdatePVal(sUser, dollarValue)
        return render(request, 'points/sponsorList.html', {'companyProf':companyProf})

def UpdatePointVal(request):
    if request.method == 'POST':
        sUserName = request.user.username
        sponsorUser = getID(sUserName)
        # If the sponsor is currently unemployed
        if sponsorUser == -1:
            if request.POST.get("join"):
                compCode = request.POST.get("compCode")
                joinCompany(sUserName, compCode)
            else:
                compName = request.POST.get("compName")
                createCompany(sUserName, compName)
            return redirect('//54.88.218.67/home/point_value/')
        else:
            if request.POST.get("pointVal"):
                dollarValue = request.POST.get("pointVal")
                if dollarValue:
                    UpdatePVal(sponsorUser, dollarValue)
            else:
                # The sponsor hit "accept"
                if request.POST.get("accept"):
                    approveDriver(request.POST.get("dUser"), sUserName, True)
                # The sponsor hit "reject"
                else:
                    approveDriver(request.POST.get("dUser"), sUserName, False)
            return redirect('//54.88.218.67/home/point_value/')

    companyProf = pullCompanyProfile(request.user.username)
    driverList = pullPendingDrivers(request.user.username)
    # If the sponsor is currently unemployed
    if companyProf.name == "unemployed":
        return render(request, 'pointValue/createComp.html')
    else:
        return render(request, 'pointValue/pointVal.html', {'companyProf':companyProf, 'driverList':driverList})

def viewMyCompanies(request):
    if request.method == 'POST':
        driverUser = request.user.username
        code = request.POST.get("compCode")
        applyToCompany(driverUser, code)
    driverObj = pullDriverProfile(request.user.username)
    return render(request, 'pointValue/viewComps.html', {'driverObj':driverObj})

def viewACompany(request):
    if request.method == "GET":
        empID = request.GET["comp"]
        driverUser = request.user.username
        companyProf = drPullCompanyProfile(empID)
        dPoints = getPoints(request.user.username, empID)
    else:
        driverUser = request.user.username
        comp = request.POST.get("compID")
        removeComp(driverUser, comp)
        return redirect('//54.88.218.67/home/companies/')
    return render(request, 'pointValue/compProfile.html', {'companyProf':companyProf, 'dPoints':dPoints})

def updateMyPersonalInfo(request):
    if request.method == 'POST':
        daUser = request.user.username
        form = UpdateForm(request.POST)
        if form.is_valid():
            #form.save()

            #Fill in additional information in user database
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            prefName = form.cleaned_data.get('prefName')
            updateUserInfo(daUser, fname, lname, prefName, email, phone, address)
            return redirect('//54.88.218.67/home/profile/')
    else:
        daUser = request.user.username
        accType = verifyAccount(daUser)
        infoList = getUserInfo(daUser, accType)
        if accType == 'd':
            initial_dict = {
                "fname": infoList[0].fname,
                "lname": infoList[0].lname,
                "email": infoList[0].email,
                "phone": infoList[0].phone,
                "address": infoList[0].address,
                "prefName": infoList[0].pname,
            }
        else:
            initial_dict = {
                "fname": infoList[0].fname2,
                "lname": infoList[0].lname2,
                "email": infoList[0].email2,
                "phone": infoList[0].phone2,
                "address": infoList[0].address2,
                "prefName": infoList[0].pname2,
            }
        form = UpdateForm(initial=initial_dict)
    return render(request, 'profile/update.html', {'form':form})        

def updateMyPass(request):
    if request.method == "POST":
        daUser = request.user.username
        user = User.objects.get(username=daUser)
        accType = verifyAccount(daUser)
        form = UpdatePass(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('//54.88.218.67/home/profile/')
    else:
        daUser = request.user.username
        user = User.objects.get(username=daUser)
        accType = verifyAccount(daUser)
        form = UpdatePass(user)
    return render(request, 'profile/update.html', {'form':form})

def updateNotMyPersonalInfo(request):
    if request.method == "POST":
        daUser = request.GET['uname']
        #user = User.objects.get(username=daUser)
        accType = verifyAccount(daUser)
        form = UpdateForm(request.POST)
        if form.is_valid():
            #form.save()

            #Fill in additional information in user database
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            prefName = form.cleaned_data.get('prefName')
            updateUserInfo(daUser, fname, lname, prefName, email, phone, address)
            if accType == 'd':
                return redirect('//54.88.218.67/home/all_drivers/viewProfile/?uname='+daUser+'')
            elif accType == 's':
                return redirect('//54.88.218.67/home/all_sponsors/viewProfile/?uname='+daUser+'')
            else:
                return redirect('//54.88.218.67/home/all_admins/viewProfile/?uname='+daUser+'')
    else:
        daUser = request.GET['uname']
        #user = User.objects.get(username=daUser)
        accType = verifyAccount(daUser)
        infoList = getUserInfo(daUser, accType)
        if accType == 'd':
            initial_dict = {
                "fname": infoList[0].fname,
                "lname": infoList[0].lname,
                "email": infoList[0].email,
                "phone": infoList[0].phone,
                "address": infoList[0].address,
                "prefName": infoList[0].pname,
            }
        else:
            initial_dict = {
                "fname": infoList[0].fname2,
                "lname": infoList[0].lname2,
                "email": infoList[0].email2,
                "phone": infoList[0].phone2,
                "address": infoList[0].address2,
                "prefName": infoList[0].pname2,
            }
        form = UpdateForm(initial=initial_dict)
    return render(request, 'profile/update.html', {'form':form})

def updateNotMyPass(request):
    if request.method == "POST":
        daUser = request.GET['uname']
        user = User.object.get(username=daUser)
        accType = verifyAccount(daUser)
        form = UpdatePass(user, request.POST)
        if form.is_valid():
            form.save()
            if accType == 'd':                                                                     return redirect('//54.88.218.67/home/all_drivers/viewProfile/?uname='+daUser+'')
            elif accType == 's':
                return redirect('//54.88.218.67/home/all_sponsors/viewProfile/?uname='+daUser+'')
            else:
                return redirect('//54.88.218.67/home/all_admins/viewProfile/?uname='+daUser+'')
    else:
        daUser = request.GET['uname']
        user = User.objects.get(username=daUser)
        accType = verifyAccount(daUser)
        form = UpdatePass(user)
    return render(request, 'profile/update.html', {'form':form})


def adminCreate(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            #Fill in additional information in user database
            uname = user_form.cleaned_data.get('username')
            phone = user_form.cleaned_data.get('phone')
            address = user_form.cleaned_data.get('address')
            prefName = user_form.cleaned_data.get('prefName')
            addUserInfo(uname, prefName, phone, address)

            #Add user to their specific user type table
            userType = user_form.cleaned_data.get('type_of_user_choices')
            userType = dict(user_form.fields['type_of_user_choices'].choices)[userType]
            addUserTypeInfo(uname, userType)
            return redirect('//54.88.218.67/home/')
    else:
        user_form = UserForm()
    return render(request, 'createAcc/adregister.html', {'user_form':user_form})

def seeMyCatalog(request):
    daUser = ""

    if request.method == "POST":
        fName = request.POST.get('fName')
        if fName == 'add':
            dUser = request.POST.get('dUser')
            itemID = int(request.POST.get('itemID'))
            itemName = request.POST.get('itemName')
            pointCost = int(request.POST.get('pointCost'))
            spComp = getSpCompany(request.user.username)
            addToCart(dUser, spComp, pointCost, itemID, itemName)
            return redirect('//54.88.218.67/home/drivers/viewCart/?dUser=' + dUser)
        elif fName == 'query':
            newQuery = request.POST.get('newQuery')
            updateCatalog(request.user.username, newQuery)
        else:
            daUsername = request.POST.get('dUser')
            daUser = pullDriverProfile(daUsername)

    comp = pullCompanyProfile(request.user.username)
    pointRatio = float(comp.pointRatio)
    compName = comp.name

    itemList = searchGeneralAPI(comp.query)
    for item in itemList:
        item.points = round(item.price * 1.01 * pointRatio)

    drivList = pulldownDrivers(request.user.username)

    return render(request, 'catalog/sponsorCatalog.html', {'itemList':itemList, 'compName':compName, 'query':comp.query, 'drivList':drivList, 'daUser':daUser})

def seeMyCatalogs(request):
    driverObj = pullDriverProfile(request.user.username)
    return render(request, 'catalog/myCatalogs.html', {'comps':driverObj.pointObjs})

def seeThisCatalog(request):
    if request.method == "POST":
        
        driverUser = request.user.username

        compID = int(request.POST.get("company"))
        pointCost = int(request.POST.get("pointCost"))
        itemID = int(request.POST.get("itemID"))
        itemName = request.POST.get("itemName")
        
        addToCart(driverUser, compID, pointCost, itemID, itemName)

        return redirect('//54.88.218.67/home/cart_list/cart/?comp=' + str(compID))
    else:
        comp = request.GET['comp']
        compProfile = drPullCompanyProfile(comp)
        pointRatio = float(compProfile.pointRatio)
        drivPoints = getPoints(request.user.username, compProfile.cid)

        itemList = searchGeneralAPI(compProfile.query)
        for item in itemList:
            item.points = round(item.price * 1.01 * pointRatio)
        return render(request, 'catalog/driverCatalog.html', {'itemList':itemList, 'compProf':compProfile, 'drivPoints':drivPoints})

def adminCatalogs(request):
    compList = pullAllCompanies()
    return render(request, 'catalog/allCatalogs.html', {'compList':compList})

def adminViewCatalog(request):
    daUser = ""
    comp = -1

    if request.method == "POST":
        fName = request.POST.get('fName')
        if fName == "add":
            dUser = request.POST.get('dUser')
            pointCost = int(request.POST.get('pointCost'))
            itemID = int(request.POST.get('itemID'))
            itemName = request.POST.get('itemName')
            compID = int(request.POST.get('compID'))

            addToCart(dUser, compID, pointCost, itemID, itemName)

            return redirect('//54.88.218.67/home/all_drivers/viewCart/?dUser=' + dUser + '&comp=' + str(compID))
        elif fName == "query":
            empID = int(request.POST.get('compID'))
            newQuery = request.POST.get('newQuery')
            adminUpdateCatalog(empID, newQuery)

            return redirect('//54.88.218.67/home/admin_catalogs/view/?comp=' + str(empID))
        else:
            dUser = request.POST.get('dUser')
            daUser = pullDriverProfile(dUser)
            comp = int(request.POST.get('compID'))
    else:
        comp = int(request.GET['comp'])

    spUser = getCompanySp(comp)
    drivList = pulldownDrivers(spUser)

    compProf = drPullCompanyProfile(comp)
    pointRatio = float(compProf.pointRatio)
    
    itemList = searchGeneralAPI(compProf.query)
    for item in itemList:
        item.points = round(item.price * 1.01 * pointRatio)
    return render(request, 'catalog/adminCatalog.html', {'itemList':itemList, 'comp':compProf, 'daUser':daUser, 'drivList':drivList})

def seeMyCarts(request):
    driverObj = pullDriverProfile(request.user.username)
    return render(request, 'cart/myCartList.html', {'comps':driverObj.pointObjs})

def seeThisCart(request):
    driverUser = request.user.username
    comp = -1

    if request.method == "GET":
        comp = int(request.GET['comp'])
    else:
        comp = int(request.POST.get('compID'))
        itemID = int(request.POST.get('itemID'))
        removeFromCart(itemID)

    cartItems = pulldownCart(driverUser, comp)

    compProf = drPullCompanyProfile(comp)
    drivPoints = getPoints(driverUser, compProf.cid)

    # Get total cost of cart
    pointCost = 0
    for i in cartItems:
        pointCost += i.pointCost

    return render(request, 'cart/viewMyCart.html', {'itemList':cartItems, 'comp':compProf, 'drivPoints':drivPoints, 'totalPoints':pointCost})

def adminSeeCart(request):
    if request.method == "POST":
        itemID = request.POST.get('itemID')
        removeFromCart(itemID)

        driverUser = request.POST.get('dUser')
        compID = int(request.POST.get('compID'))

        return redirect('//54.88.218.67/home/all_drivers/viewCart/?dUser=' + driverUser + '&comp=' + str(compID))

    driverUser = request.GET['dUser']
    comp = request.GET['comp']
    cartItems = pulldownCart(driverUser, comp)

    compProf = drPullCompanyProfile(comp)
    drivPoints = getPoints(driverUser, comp)
    dProf = pullDriverProfile(driverUser)

    pointCost = 0
    for i in cartItems:
        pointCost += i.pointCost

    return render(request, 'cart/adminViewCart.html', {'itemList':cartItems, 'comp':compProf, 'dUser':driverUser, 'drivPoints':drivPoints, 'totalPoints':pointCost, 'dProf':dProf})

def sponsorSeeCart(request):
    if request.method == "POST":
        itemID = request.POST.get("itemID")
        removeFromCart(itemID)

        driverUser = request.POST.get('dUser')

        return redirect('//54.88.218.67/home/drivers/viewCart/?dUser=' + driverUser)

    driverUser = request.GET['dUser']
    compProf = pullCompanyProfile(request.user.username)
    cartItems = pulldownCart(driverUser, compProf.cid)

    drivPoints = getPoints(driverUser, compProf.cid)
    dProf = spPullDriverProfile(driverUser, request.user.username)

    pointCost = 0
    for i in cartItems:
        pointCost += i.pointCost

    return render(request, 'cart/sponsorViewCart.html', {'itemList':cartItems, 'comp':compProf, 'dUser':driverUser, 'drivPoints':drivPoints, 'totalPoints':pointCost, 'dProf':dProf})

def confirmThisCart(request):
    driverUser = request.user.username

    # For when you load the page
    if request.method == "GET":
        comp = int(request.GET['comp'])

        cartItems = pulldownCart(driverUser, comp)
        compProf = drPullCompanyProfile(comp)
        drivPoints = getPoints(driverUser, compProf.cid)

        # Get total cost of cart
        pointCost = 0
        for i in cartItems:
            pointCost += i.pointCost

        diff = drivPoints - pointCost

        return render(request, 'cart/confirmPurchase.html', {'itemList':cartItems, 'comp':compProf, 'drivPoints':drivPoints, 'totalPoints':pointCost, 'diff':diff})
    # For when you confirm your purchase
    else:
        comp = int(request.POST.get('compID'))
                
        cartItems = pulldownCart(driverUser, comp)
        driverCheckout(driverUser, comp, cartItems)
        
        return redirect('//54.88.218.67/home/purchases')

def spConfirmThisCart(request):
    # For when you load the page
    if request.method == "GET":
        driverUser = request.GET['dUser']

        comp = getSpCompany(request.user.username)

        cartItems = pulldownCart(driverUser, comp)
        compProf = drPullCompanyProfile(comp)
        drivPoints = getPoints(driverUser, compProf.cid)
        dProf = spPullDriverProfile(driverUser, request.user.username)

        # Get total cost of cart
        pointCost = 0
        for i in cartItems:
            pointCost += i.pointCost

        diff = drivPoints - pointCost

        return render(request, 'cart/spConfirmPurchase.html', {'itemList':cartItems, 'comp':compProf, 'drivPoints':drivPoints, 'totalPoints':pointCost, 'diff':diff, 'dUser':driverUser, 'dProf':dProf})
    # For when you confirm your purchase
    else:
        comp = int(request.POST.get('compID'))
        driverUser = request.POST.get('dUser')

        cartItems = pulldownCart(driverUser, comp)
        sponsorCheckout(driverUser, comp, cartItems, request.user.username)                                                                     
        return redirect('//54.88.218.67/home/drivers/purchases/?dUser=' + driverUser)

def adConfirmThisCart(request):
    # For when you load the page
    if request.method == "GET":
        driverUser = request.GET['dUser']
        comp = request.GET['comp']

        cartItems = pulldownCart(driverUser, comp)
        compProf = drPullCompanyProfile(comp)
        drivPoints = getPoints(driverUser, compProf.cid)
        dProf = pullDriverProfile(driverUser)

        # Get total cost of cart
        pointCost = 0
        for i in cartItems:
            pointCost += i.pointCost

        diff = drivPoints - pointCost

        return render(request, 'cart/adConfirmPurchase.html', {'itemList':cartItems, 'comp':compProf, 'drivPoints':drivPoints, 'totalPoints':pointCost, 'diff':diff, 'dUser':driverUser, 'dProf':dProf})
    # For when you confirm your purchase
    else:
        comp = int(request.POST.get('compID'))
        driverUser = request.POST.get('dUser')

        cartItems = pulldownCart(driverUser, comp)
        adminCheckout(driverUser, comp, cartItems, request.user.username)
        return redirect('//54.88.218.67/home/all_drivers/purchases/?dUser=' + driverUser)

def viewMyPurchases(request):
    driverUser = request.user.username

    # If an item was clicked to be canceled, do it here before reloading the page
    if request.method == "POST":
        itemID = int(request.POST.get('itemID'))
        itemCost = int(request.POST.get('itemCost'))
        cancelPurchase(driverUser, itemID, itemCost)

    purchasedItems = getOutstandingPurchases(driverUser)
    driverObj = pullDriverProfile(driverUser)

    return render(request, 'purchases/viewPurchases.html', {'itemList':purchasedItems, 'drivObj':driverObj})

def spViewPurchases(request):
    if request.method == "POST":
        itemID = int(request.POST.get('itemID'))
        itemCost = int(request.POST.get('itemCost'))
        driverUser = request.POST.get('dUser')
        cancelPurchase(driverUser, itemID, itemCost)

        return redirect('//54.88.218.67/home/drivers/purchases/?dUser=' + driverUser)

    driverUser = request.GET['dUser']
    dProf = spPullDriverProfile(driverUser, request.user.username)

    purchasedItems = spGetOutstandingPurchases(driverUser, request.user.username)

    return render(request, 'purchases/spViewPurchases.html', {'itemList':purchasedItems, 'dProf':dProf})

def adViewPurchases(request):
    if request.method == "POST":
        itemID = int(request.POST.get('itemID'))
        itemCost = int(request.POST.get('itemCost'))
        driverUser = request.POST.get('dUser')
        cancelPurchase(driverUser, itemID, itemCost)                                                                    
        return redirect('//54.88.218.67/home/all_drivers/purchases/?dUser=' + driverUser)

    driverUser = request.GET['dUser']
    dProf = pullDriverProfile(driverUser)

    purchasedItems = getOutstandingPurchases(driverUser)

    return render(request, 'purchases/adViewPurchases.html', {'itemList':purchasedItems, 'dProf':dProf})

def resetPuname(request):
    if request.method == 'POST':	
        form = UnameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('uname')
            user = User.objects.get(username=name) 
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            return redirect('//54.88.218.67/reset/pass/')
    else:
        form = UnameForm()
        return render(request, 'login/reset.html', {'form':form})

def resetP(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('//54.88.218.67/')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'login/preset.html', {'form':form})

def reportsHome(request):
    return render(request, 'reports/reportHome.html')

def reportsOverTime(request):
    if request.method == "POST":
        monthID = int(request.POST.get('month'))
        year = int(request.POST.get('year'))

        # Get report data
        reportData = getSalesOverTime(monthID, year)
        companyList = pullAllCompanies()

        # Get total cost and revenue
        totalCost = 0.0
        for i in reportData:
            totalCost += float(i.cost)
        totalRev = "{:.2f}".format(round(0.01 * totalCost, 2))
        totalCost = "{:.2f}".format(totalCost)

        # Get month spelled out
        month = ""
        if monthID == 1:
            month = "January"
        elif monthID == 2:
            month = "February"
        elif monthID == 3:
            month = "March"
        elif monthID == 4:
            month = "April"
        elif monthID == 5:
            month = "May"
        elif monthID == 6:
            month = "June"
        elif monthID == 7:
            month = "July"
        elif monthID == 8:
            month = "August"
        elif monthID == 9:
            month = "September"
        elif monthID == 10:
            month = "October"
        elif monthID == 11:
            month = "November"
        elif monthID == 12:
            month = "December"

        return render(request, 'reports/salesOverTime.html', {'companies':companyList, 'reportData':reportData, 'month':month, 'year':year, 'allSales':totalCost, 'rev':totalRev})

    companyList = pullAllCompanies()

    return render(request, 'reports/salesOverTime.html', {'companies':companyList})


def reportsSponsor(request):
    if request.method == "POST":
        monthID = int(request.POST.get('month'))
        year = int(request.POST.get('year'))
        compID = int(request.POST.get('comp'))
        compName = request.POST.get(str(compID))

        # Get report data
        reportData = getSalesBySponsor(compID, monthID, year)
        companyList = pullAllCompanies()

        # Get total cost and revenue
        totalCost = 0.0
        for i in reportData:
            totalCost += float(i.cost)
        totalRev = "{:.2f}".format(round(0.01 * totalCost, 2))
        totalCost = "{:.2f}".format(totalCost)

        # Get month spelled out
        month = ""
        if monthID == 1:
            month = "January"
        elif monthID == 2:
            month = "February"
        elif monthID == 3:
            month = "March"
        elif monthID == 4:
            month = "April"
        elif monthID == 5:
            month = "May"
        elif monthID == 6:
            month = "June"
        elif monthID == 7:
            month = "July"
        elif monthID == 8:
            month = "August"
        elif monthID == 9:
            month = "September"
        elif monthID == 10:
            month = "October"
        elif monthID == 11:
            month = "November"
        elif monthID == 12:
            month = "December"

        return render(request, 'reports/salesBySponsor.html', {'companies':companyList, 'reportData':reportData, 'compName':compName, 'month':month, 'year':year, 'allSales':totalCost, 'rev':totalRev})

    companyList = pullAllCompanies()

    return render(request, 'reports/salesBySponsor.html', {'companies':companyList})



def reportsDriverPurchases(request):
    employers = []
    employers = listEmployers()
    summary = []
    for i in employers:
        summary.append(getDriverPurchaseHistory(i.ID))
    return render(request, 'reports/driverPurchases.html',{'summary':summary})
