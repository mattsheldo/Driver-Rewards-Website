from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from viewsFunctions.ProfilePage import getUserInfo 
from viewsFunctions.UpdateProfilePage import updateUserInfo
from viewsFunctions.SponsorProfile import SponsorProfile, pullAdminProfile, pullSponsorProfile
from viewsFunctions.SponsorList import SponsorListItem, pulldownAdmins, pulldownSponsors
from viewsFunctions.AddFunctions import DriverPoints, DriverProfile, pullDriverProfile, addPoints, addPointsAdmin
from viewsFunctions.DriverList import DriverListItem, pulldownDrivers, adminPulldownDrivers
from viewsFunctions.PointsPerDollar import UpdatePVal, getID
from viewsFunctions.NewUserReg import addUserInfo, addUserTypeInfo
from viewsFunctions.Account import verifyAccount
from .forms import UserForm, UpdateForm

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
    driverObj = pullDriverProfile(loginUsername)
    if accType == "d":
        return render(request, 'homepage/homepage.html', {'infoList':infoList, 'driverObj':driverObj})
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
    driverObj = pullDriverProfile(uname)
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

def UpdatePointVal(request):
    if request.method == 'POST':
        sUserName = request.user.username
        sponsorUser = getID(sUserName)
        dollarValue = request.POST.get("pointVal")
        # Call this if it's an ad
        if dollarValue:
            UpdatePVal(sponsorUser, dollarValue)
            return render(request, 'pointValue/pointVal.html', {'dollarValue':dollarValue})
        else:
            return redirect('//54.88.218.67/logout/')
    else:
        return render(request, 'pointValue/pointVal.html')


def updateMyProfile(request):
    if request.method == 'POST':
        daUser = request.user.username
        form = UpdateForm(request.user, request.POST)
        if form.is_valid():
            form.save()

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
        form = UpdateForm(request.user, initial=initial_dict)
    return render(request, 'profile/update.html', {'form':form})        


