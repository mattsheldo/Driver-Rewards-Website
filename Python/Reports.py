import mysql.connector

class ReportItem:
    def __init__(self, name, cost, datePurchased):
        self.name = name
        self.cost = cost
        self.datePurchased = datePurchased

# monthInt is the month number (1-12)
# V IMPORTANT: monthInt does NOT start at 0, meaning January = 1
def getSalesBySponsor(compID, monthInt, year):
    report = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Assemble the proper time frame
        # monthBegin = "2020-"
        monthBegin = str(year) + "-"
        if monthInt < 10:
            # monthBegin = "2020-09"
            monthBegin += "0" + str(monthInt)
        else:
            # monthBegin = "2020-11"
            monthBegin += str(monthInt)
        # monthBegin = "2020-11-00 00:00:00"
        monthBegin += "-00 00:00:00"

        # monthEnd will go exactly one month later
        # This way, we don't have to worry about months having a different number of days
        monthInt = (monthInt + 1) % 12
        # If the next month is January, increment the year and make sure the month gets set to 1 for January, not 0
        if monthInt == 0:
            monthInt += 1
            year += 1

        # monthEnd = "2020-"
        monthEnd = str(year) + "-"
        if monthInt < 10:
            # monthEnd = "2020-09"
            monthEnd += "0" + str(monthInt)
        else:
            # monthEnd = "2020-11"
            monthEnd += str(monthInt)
        # monthEnd = "2020-11-00 00:00:00"
        monthEnd += "-00 00:00:00"

        # Acquire each item purchased from the given company during the given month
        myCursor = mydb.cursor()
        query = "SELECT Product_Name, Point_Total, PointsPerDollar, Date_ FROM Purchase_History JOIN Employers as E ON Employer_ID = E.ID WHERE E.ID = " + str(compID) + " AND Date_ > '" + monthBegin + "' AND Date_ < '" + monthEnd + "' ORDER BY Date_;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for item in myResults:
                itemName = item[0]
                # Divide the point cost by the point/dollar ratio to get cost in USD
                itemCost = round(item[1] / item[2], 2)
                # Just take the "Date" part of the Datetime obj, no need for the full timestamp
                itemDate = str(item[3])[0:10]               
                report.append(ReportItem(itemName, itemCost, itemDate))
        except Exception as e:
            print("getSalesBySponsor(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("getSalesBySponsor(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return report