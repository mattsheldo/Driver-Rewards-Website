from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from ProfilePage import getUserInfo 
from UpdateProfilePage import updateUserInfo
from .forms import UserForm, UpdateForm

import mysql.connector

from datetime import datetime

class SponsorProfile:
    def __init__(self, user, first, last, prefName, email, phone, address):
        self.user = user
        self.first = first
        self.last = last
        self.prefName = prefName
        self.email = email
        self.phone = phone
        self.address = address

def pullAdminProfile(username):
    profileObj = SponsorProfile("", "", "", "", "", "", "")

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all info for this driver
        myCursor = mydb.cursor()
        query = "SELECT auth_user.username, first_name, last_name, preferred_name, email, phone, address_ FROM auth_user JOIN Admins ON Admins.Username = auth_user.username WHERE auth_user.username = '" + username + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            for d in myResults:
                pref = ""
                if d[3]:
                    pref = d[3]
                profileObj = SponsorProfile(d[0], d[1], d[2], pref, d[4], d[5], d[6])
        except Exception as e:
            print("pullAdminProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullAdminProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj

def pullSponsorProfile(username):
    profileObj = SponsorProfile("", "", "", "", "", "", "")

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all info for this driver
        myCursor = mydb.cursor()
        query = "SELECT auth_user.username, first_name, last_name, preferred_name, email, phone, address_ FROM auth_user JOIN Sponsors ON Sponsors.Username = auth_user.username WHERE auth_user.username = '" + username + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            for d in myResults:
                pref = ""
                if d[3]:
                    pref = d[3]
                profileObj = SponsorProfile(d[0], d[1], d[2], pref, d[4], d[5], d[6])
        except Exception as e:
            print("pullSponsorProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullSponsorProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj

class SponsorListItem:
    def __init__(self, first, last, user):
        self.first = first
        self.last = last
        self.user = user

def pulldownAdmins():
    adminNames = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all sponsors
        myCursor = mydb.cursor()
        query = "SELECT first_name, last_name, auth_user.username FROM auth_user JOIN Admins ON Admins.Username = auth_user.username;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into a list
            for d in myResults:
                adminNames.append(SponsorListItem(d[0], d[1], d[2]))
        except Exception as e:
            print("pulldownAdmins(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownAdmins(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return adminNames

def pulldownSponsors():
    sponsorNames = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all sponsors
        myCursor = mydb.cursor()
        query = "SELECT first_name, last_name, auth_user.username FROM auth_user JOIN Sponsors ON Sponsors.Username = auth_user.username;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into a list
            for d in myResults:
                sponsorNames.append(SponsorListItem(d[0], d[1], d[2]))
        except Exception as e:
            print("pulldownSponsors(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownSponsors(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return sponsorNames

class DriverProfile:
    def __init__(self, user, first, last, pointTotal, prefName, email, phone, address):
        self.user = user
        self.first = first
        self.last = last
        self.pointTotal = pointTotal
        self.prefName = prefName
        self.email = email
        self.phone = phone
        self.address = address

def pullDriverProfile(username):
    profileObj = DriverProfile("", "", "", 0, "", "", "", "")

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all info for this driver
        myCursor = mydb.cursor()
        query = "SELECT auth_user.username, first_name, last_name, Point_Total, preferred_name, email, phone, address_ FROM auth_user JOIN Drivers ON Drivers.Username = auth_user.username WHERE auth_user.username = '" + username + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            for d in myResults:
                pref = ""
                if d[4]:
                    pref = d[4]
                profileObj = DriverProfile(d[0], d[1], d[2], d[3], pref, d[5], d[6], d[7])
        except Exception as e:
            print("pullDriverProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullDriverProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj

def addPoints(sponsor, driver, currentPoints, newPoints, addB):
    newTotal = 0
    changeType = ""
    if addB:
        newTotal = currentPoints + newPoints
        changeType = "add"
    else:
        newTotal = currentPoints - newPoints
        changeType = "sub"

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Update driver's points
        myCursor = mydb.cursor()
        query = "UPDATE Drivers SET Point_Total = " + str(newTotal) + " WHERE Username = '" + driver + "';"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPoints(): Failed to update database: " + str(e))
        finally:
            myCursor.close()

        # Get the last used ID from Point_History
        myid = 0
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Point_History ORDER BY ID DESC LIMIT 1;"
        try:
            # Execute query
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
              myid = int(i[0]) + 1
              break
        except Exception as e:
            print("addPoints(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Get current date
        today = datetime.today().strftime("%Y-%m-%d")
        # Update Point_History
        myCursor = mydb.cursor()
        query = "INSERT INTO Point_History (ID, Username, Date_, Point_Cost, Type_Of_Change, Sponsor_ID) VALUES (" + str(myid) + ", '" + driver + "', '" + today + "', " + str(newPoints) + ", '" + changeType + "', '" + sponsor + "');"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPoints(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("addPoints(): Failed to connect: " + str(e))
    finally:
        mydb.close()

def addPointsAdmin(admin, driver, currentPoints, newPoints, addB):
    newTotal = 0
    changeType = ""
    if addB:
        newTotal = currentPoints + newPoints
        changeType = "add"
    else:
        newTotal = currentPoints - newPoints
        changeType = "sub"

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Update driver's points
        myCursor = mydb.cursor()
        query = "UPDATE Drivers SET Point_Total = " + str(newTotal) + " WHERE Username = '" + driver + "';"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPoints(): Failed to update database: " + str(e))
        finally:
            myCursor.close()

        # Get the last used ID from Point_History
        myid = 0
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Point_History ORDER BY ID DESC LIMIT 1;"
        try:
            # Execute query
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
              myid = int(i[0]) + 1
        except Exception as e:
            print("addPoints(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Get current date
        today = datetime.today().strftime("%Y-%m-%d")
        # Update Point_History
        myCursor = mydb.cursor()
        query = "INSERT INTO Point_History (ID, Username, Date_, Point_Cost, Type_Of_Change, Admin_ID) VALUES (" + str(myid) + ", '" + driver + "', '" + today + "', " + str(newPoints) + ", '" + changeType + "', '" + admin + "');"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPoints(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("addPoints(): Failed to connect: " + str(e))
    finally:
        mydb.close()

class DriverListItem:
    def __init__(self, first, last, pointTotal, user):
        self.first = first
        self.last = last
        self.pointTotal = pointTotal
        self.user = user

def pulldownDrivers(sponsor):
    driverNames = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all driver under the current sponsor
        myCursor = mydb.cursor()
        query = "SELECT auth_user.first_name, auth_user.last_name, Drivers.Point_Total, auth_user.username FROM (Drivers JOIN Sponsors ON Drivers.Employer_ID = Sponsors.Employer_ID) JOIN auth_user ON Drivers.Username = auth_user.username WHERE Sponsors.Username LIKE '" + sponsor + "' ORDER BY auth_user.last_name, auth_user.first_name;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into a list
            for d in myResults:
                driverNames.append(DriverListItem(d[0], d[1], d[2], d[3]))
        except Exception as e:
            print("pulldownDrivers(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownDrivers(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return driverNames

def UpdatePVal(sponsorID, DollarValue):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()
    query = "UPDATE Employers SET PointsPerDollar = '"+str(DollarValue)+"' WHERE ID = '"+str(sponsorID)+"';"

    myCursor.execute(query)
    mydb.commit()

    myCursor.close()
    mydb.close()

def getID(userName):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )

    myCursor = mydb.cursor()
    query = "SELECT Employer_ID FROM Sponsors WHERE Username = '"+userName+"';"

    myCursor.execute(query)
    myResults = myCursor.fetchall()
    mydb.commit()

    myCursor.close()
    mydb.close()
    return myResults

def addUserInfo(userUser,prefName,phoneNum,address):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )

    myCursor = mydb.cursor()
    query = "UPDATE auth_user SET phone = '"+phoneNum+"', address_ = '"+address+"', preferred_name = '"+prefName+"' WHERE username = '"+userUser+"';"

    myCursor.execute(query)
    mydb.commit()
        
    myCursor.close()
    mydb.close()


def addUserTypeInfo(userUser,userType):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )

    myCursor = mydb.cursor()

    if userType is 'Driver':
        query = "INSERT INTO Drivers (Username, Employer_ID, Point_Total) VALUES ('"+userUser+"', -1, 0);"

    elif userType is 'Sponsor':
        query = "INSERT INTO Sponsors (Username, Employer_ID) VALUES ('"+userUser+"',-1);"
        
    else:
        query = "INSERT INTO Admins (Username) VALUES ('"+userUser+"');"
        
    myCursor.execute(query)
    mydb.commit()
    myCursor.close()
    mydb.close()

def verifyAccount(userUser):
    returnType = ""

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for a match in Drivers
        myCursor = mydb.cursor()
        query = "SELECT * FROM Drivers WHERE Username = '" + userUser + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # If a result is found, then there's a match
            if len(myResults) > 0:
                # Driver found
                returnType = "d"
                myCursor.close()
                mydb.close()
                return returnType
        except Exception as e:
            print("verifyAccount(): Failed to query Drivers: " + str(e))
        finally:
            myCursor.close()

        # Look for a match in Sponsors
        myCursor = mydb.cursor()
        query = "SELECT * FROM Sponsors WHERE Username = '" + userUser + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # If a result is found, then there's a match
            if len(myResults) > 0:
                # Sponsor found
                returnType = "s"
                myCursor.close()
                mydb.close()
                return returnType
        except Exception as e:
            print("verifyAccount(): Failed to query Sponsors: " + str(e))
        finally:
            myCursor.close()

        # Look for a match in Admins
        myCursor = mydb.cursor()
        query = "SELECT * FROM Admins WHERE Username = '" + userUser + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

           # If a result is found, then there's a match
            if len(myResults) > 0:
                # Admin found
                returnType = "a"
                myCursor.close()
                mydb.close()
                return returnType
        except Exception as e:
            print("verifyAccount(): Failed to query Admins: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("verifyAccount(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return returnType


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
    if accType == "d":
        return render(request, 'homepage/homepage.html')
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
        if request.POST.get("addBut"):
            addPointsAdmin(adminUser, driverUser, currPoints, nextPoints, True)
        else:
            addPointsAdmin(adminUser, driverUser, currPoints, nextPoints, False)
        return redirect('//54.88.218.67/home/all_drivers/')
    else:
        driverList = pulldownDrivers('%')
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
    if accType == "d":
        return render(request, 'profile/driver_profile.html', {'infoList':infoList})
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
        if dollarValue == "10":
            UpdatePVal(sponsorUser, dollarValue)
            return redirect('//54.88.218.67/home/point_value/')
        else:
            return redirect('//54.88.218.67/logout/')
    else:
        return render(request, 'pointValue/pointVal.html')


def updateMyProfile(request):
    if request.method == 'POST':
        daUser = request.user.username
        user_form = UpdateForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            #Fill in additional information in user database
            fname = user_form.cleaned_data.get('fname')
            lname = user_form.cleaned_data.get('lname')
            email = user_form.cleaned_data.get('email')
            phone = user_form.cleaned_data.get('phone')
            address = user_form.cleaned_data.get('address')
            prefName = user_form.cleaned_data.get('prefName')
            updateUserInfo(daUser, fname, lname, prefName, email, phone, address)
            return redirect('//54.88.218.67/home/profile/')
    else:
        user_form = UpdateForm()
        return render(request, 'profile/update.html', {'user_form':user_form})        


