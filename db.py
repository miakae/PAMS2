import sys
import random

import mysql.connector
from mysql.connector import errorcode

from dbSecrets import *

from ErrorBoxes import ErrorMessage

isUsingDev = True

host = ""
user = ""
password = ""
dbName = ""

def GetConnection():
    if isUsingDev:
        host = devHost
        user = devUser
        password = devPassword
        dbName = devName
    else: 
        host = prodHost
        user = prodUser
        password = prodPassword
        dbName = prodName

    try:
        conn = mysql.connector.connect(host = host, user = user, password =password)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('User name or password is not working')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        if conn.is_connected():
            print('MySQL Connection is established')
            return conn


def GetLocation(locationName: str):
    query = "SELECT * FROM locations WHERE locations.location_name = %s;"

    conn = GetConnection()    
    
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database") 

    dbcursor.execute(query, (locationName,))
    location = dbcursor.fetchone()
    if(location is None):
        dbcursor.close()
        conn.close()
        print("Database Closed")
        return None
    else:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        return location

def GetApartmentsFromLocation(Id : str):
    query2 = "SELECT * from apartments WHERE location_id = %s"
    
    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database") 
    
    dbcursor.execute(query2, (Id,))
    apartments = dbcursor.fetchall()

    dbcursor.close()
    conn.close()
    print("Database Closed")

    if apartments is None:
        return None
    else: 
        return apartments



def GetTenants():

    query = "SELECT * FROM tenants"

    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query)
    records = dbcursor.fetchall()
    conn.commit()

    conn.close()
    dbcursor.close()
    print("Closed Database")
    return records

def GetLocations():

    query = "SELECT * FROM locations"

    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query)
    records = dbcursor.fetchall()
    conn.commit()

    conn.close()
    dbcursor.close()
    print("Closed Database")
    return records

# Gets all the headers from a table in the database
def GetHeaders(table : str):
    query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = %s;"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")
    dbcursor.execute(query, (table,))
    headers = dbcursor.fetchall()
    dbcursor.close()
    conn.close()
    print("Closed Database")
    return headers

def CheckEmailIsValid(email : str):
    query = "SELECT * FROM tenants WHERE email = %s"

    conn = GetConnection()
    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")
    dbcursor.execute(query, (email,))
    user = dbcursor.fetchone()
    
    if user is not None:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        title = "Tenant Already Exists"
        description = "This email has already been used to sign up a user. Please try a different email."
        error = ErrorMessage(title, description)
        return (error)
    else:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        return None

#This assumes that the email has already been checked
def SignUpUser(fName : str, lName : str, email : str, password : str, NINumber : str, phoneNum : int, job: str):
    #TODO do SQL injection protection
    query = "INSERT INTO tenants (first_name,last_name,national_insurance, email,password,phone_number,occupation) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query, (fName,lName,NINumber,email,password,phoneNum,job,))
    conn.commit()


    conn.close()
    dbcursor.close()
    print("Closed Database")
    return None
def LoginUser(email : str, hashedPassword : str):
    query = "SELECT * FROM tenants WHERE email = %s AND password =%s"
    conn = GetConnection()

    dbcursor = conn.cursor()    #Creating cursor object
    dbcursor.execute('USE {};'.format(devName)) #use database'
    print("Entered Database")   
    dbcursor.execute(query, (email, password ,))
    tenant = dbcursor.fetchone()
    if tenant is None:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        title = "Failure To Login"
        description = "No user matches the credentials provided."
        error = ErrorMessage(title, description)
        return (error)
    else:
        dbcursor.close()
        conn.close()
        print("Database Closed")
        return None

# Returns the ids of the unoccupied apartments in a location matching the locationName value.
def GetUnoccupiedApartmentsForLocation(locationName : str):
    query = "SELECT apartments.apartment_id from apartments WHERE location_id = %s AND occupancy_status = 0;"

    location = GetLocation(locationName)
    if location == None:
        return None
    else:
        conn = GetConnection()
        dbcursor = conn.cursor()    #Creating cursor object
        dbcursor.execute('USE {};'.format(devName)) #use database'
        print("Entered Database") 

        dbcursor.execute(query, (location[0],))
        unoccupiedApartments = dbcursor.fetchall()

        return unoccupiedApartments

# def GetPaymentInsights(locationName : str):
#     query = "SELECT locations.location_id FROM locations WHERE locations.location_name = %s;"
#     query2 = "SELECT "
#     conn = GetConnection()

#     dbcursor = conn.cursor()    #Creating cursor object
#     dbcursor.execute('USE {};'.format(devName)) #use database'
#     print("Entered Database") 
#     dbcursor.execute(query, (locationName,))
#     id = dbcursor.fetchone()
#     if(id is None):
#         dbcursor.close()
#         conn.close()
#         print("Database Closed")
#         return ErrorMessage("No Data", "There is no location by this name")
#     else:
#         pass

# def GetMainanenceInsights(locationName : str):
#     query3 = "SELECT * from maintenance_requests WHERE apartment_id = %s"

#     apartments = GetApartmentsFromLocation(GetLocation(locationName)[0])

#     conn = GetConnection()
#     dbcursor = conn.cursor()
#     dbcursor.execute('USE {};'.format(devName)) #use database'
#     print("Entered Database") 
    
#     requests = []

#     for apartment in apartments:
#         dbcursor.execute(query3, (id[0],))

