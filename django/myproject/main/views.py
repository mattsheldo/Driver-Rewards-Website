from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
#from UserCreation import addUserInfo
#from AddToTypeTable import addUserTypeInfo
from .forms import UserForm

import mysql.connector

def addUserInfo(userUser,prefName,phoneNum,address):
    # Open connection
    #try:
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )

    myCursor = mydb.cursor()
    query = "UPDATE auth_user SET phone = '"+phoneNum+"', address_ = '"+address+"', preferred_name = '"+prefName+"' WHERE username = '"+userUser+"';"
        #val = (phoneNum,address,prefName,username)

        #try:
    myCursor.execute(query)
    mydb.commit()
        #except Exception:
        #    print("verifyAccount(): Failed to query")
        #finally:
    myCursor.close()
    #except Exception:
    #    print("verifyAccount(): Failed to connect")
    #finally:
    mydb.close()


def addUserTypeInfo(userUser,userType):
    # Open connection
    #try:
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )

    myCursor = mydb.cursor()

    if userType is 'Driver':
        query = "INSERT INTO Drivers (Username, Employer_ID, Point_Total) VALUES ('"+userUser+"', -1, 0);"
        #val = (userUser,-1,0)
    elif userType is 'Sponsor':
        query = "INSERT INTO Sponsors (Username, Employer_ID) VALUES ('"+userUser+"',-1);"
        #val = (userUser,-1)
    else:
        query = "INSERT INTO Admins (Username) VALUES ('"+userUser+"');"
        #val = (userUser)
        #try:
    myCursor.execute(query)
    mydb.commit()
        #except Exception:
        #    print("verifyAccount(): Failed to query")
        #finally:
    myCursor.close()
     
     #except Exception:
       # print("verifyAccount(): Failed to connect")
    #finally:
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

def findUsername():
    # Goal: find username of the most recent login to pass to verifyAccount()
    returnVal = ""
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for the most recent login
        myCursor = mydb.cursor()
        query = "SELECT username FROM auth_user ORDER BY last_login DESC;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Get first result
            for x in myResults:
                returnVal = x[0]
                myCursor.close()
                mydb.close()
                return returnVal
        except Exception as e:
            print("verifyAccount(): Failed to query auth_user: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("verifyAccount(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return returnVal
 

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
            #if uname == "testuser" and phone == "3213214321" and address == "test" and prefName == "test" and userType == "Driver":
            return redirect('//54.88.218.67/')
            #else:
                #return redirect('//54.88.218.67/logout/')
    else:
        user_form = UserForm()
    return render(request, 'createAcc/register.html', {'user_form':user_form})


def home(request):
    loginUsername = findUsername()
    accType = verifyAccount(loginUsername)
    if accType == "d":
        return render(request, 'homepage/homepage.html')
    elif accType == "s":
        return render(request, 'homepage/sponsor_homepage.html')
    elif accType == "a":
        return render(request, 'homepage/admin_homepage.html')
    else:
        return redirect('//54.88.218.67')
