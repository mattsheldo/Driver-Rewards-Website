from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import login, update_session_auth_hash
from viewsFunctions.ProfilePage import getUserInfo, getUserAlerts, deleteUserMsg, updateFilter 
from viewsFunctions.UpdateProfilePage import updateUserInfo
from viewsFunctions.UpdateBillPage import updateBillInfo
from viewsFunctions.SponsorProfile import SponsorProfile, pullAdminProfile, pullSponsorProfile
from viewsFunctions.SponsorList import SponsorListItem, pulldownAdmins, pulldownSponsors
from viewsFunctions.AddFunctions import DriverPoints, DriverProfile, pullDriverProfile, addPoints, addPointsAdmin, spPullDriverProfile
from viewsFunctions.DriverList import DriverListItem, pulldownDrivers, adminPulldownDrivers, pullPendingDrivers
from viewsFunctions.PointsPerDollar import UpdatePVal, getID, pullCompanyProfile, drPullCompanyProfile, getPoints, pullAllCompanies
from viewsFunctions.NewUserReg import addUserInfo, addUserTypeInfo
from viewsFunctions.Account import verifyAccount
from viewsFunctions.CreateCompany import createCompany, joinCompany
from viewsFunctions.FindCompany import applyToCompany
from viewsFunctions.ApproveDriver import approveDriver
from viewsFunctions.AddToCart import addToCart, pulldownCart, removeFromCart, driverCheckout, getOutstandingPurchases, cancelPurchase
from SponsorCatalog import searchGeneralAPI
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
    if accType == "d":
        driverObj = pullDriverProfile(loginUsername)
        if request.method == 'POST':
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
    elif accType == "s":
        return render(request, 'homepage/sponsor_homepage.html')
    elif accType == "a":
        return render(request, 'homepage/admin_homepage.html')
    else:
        return redirect('//54.88.218.67')

def viewMyDrivers(request):
    if request.method == 'POST':
        sponsorUser = request.user.username
        driverUser = request.POST.get("username")
        currPoints = int(request.POST.get("point"))
        nextPoints = int(request.POST.get("pointInput"))
        # Call this if it's an add
        if request.POST.get("addBut"):
            addPoints(sponsorUser, driverUser, currPoints, nextPoints, True)
        # Call this if it's a remove
        else:
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
    uname = request.GET['uname']
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
    empID = request.GET["comp"]
    driverUser = request.user.username
    companyProf = drPullCompanyProfile(empID)
    dPoints = getPoints(request.user.username, empID)
    #if request.POST.get("resign")
     #   removeComp(driverUser, empID)
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
    comp = pullCompanyProfile(request.user.username)
    pointRatio = float(comp.pointRatio)
    compName = comp.name

    itemList = searchGeneralAPI(comp.query)
    for item in itemList:
        item.points = round(item.price * pointRatio + item.shipping * pointRatio)
    return render(request, 'catalog/sponsorCatalog.html', {'itemList':itemList, 'compName':compName})

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
            item.points = round(item.price * pointRatio + item.shipping * pointRatio)
        return render(request, 'catalog/driverCatalog.html', {'itemList':itemList, 'compProf':compProfile, 'drivPoints':drivPoints})

def adminCatalogs(request):
    compList = pullAllCompanies()
    return render(request, 'catalog/allCatalogs.html', {'compList':compList})

def adminViewCatalog(request):
    comp = request.GET['comp']
    compProf = drPullCompanyProfile(comp)
    pointRatio = float(compProf.pointRatio)
    
    itemList = searchGeneralAPI(compProf.query)
    for item in itemList:
        item.points = round(item.price * pointRatio + item.shipping * pointRatio)
    return render(request, 'catalog/adminCatalog.html', {'itemList':itemList, 'comp':compProf})

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
    driverUser = request.GET['dUser']
    comp = request.GET['comp']
    cartItems = pulldownCart(driverUser, comp)

    compProf = drPullCompanyProfile(comp)
    drivPoints = getPoints(driverUser, comp)

    return render(request, 'cart/adminViewCart.html', {'itemList':cartItems, 'comp':compProf, 'dUser':driverUser, 'drivPoints':drivPoints})

def sponsorSeeCart(request):
    driverUser = request.GET['dUser']
    compProf = pullCompanyProfile(request.user.username)
    cartItems = pulldownCart(driverUser, compProf.cid)

    drivPoints = getPoints(driverUser, compProf.cid)

    return render(request, 'cart/sponsorViewCart.html', {'itemList':cartItems, 'comp':compProf, 'dUser':driverUser, 'drivPoints':drivPoints})

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
        newPoints = int(request.POST.get('newPoints'))
                
        cartItems = pulldownCart(driverUser, comp)
        driverCheckout(driverUser, comp, cartItems)
        
        return redirect('//54.88.218.67/home/')

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
