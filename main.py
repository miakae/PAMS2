import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import * 
from uiMainWindow import Ui_MainWindow
from db import *
from ErrorBoxes import *
from MyWidgets import *

class mainScreen(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PAMS")
        self.setMaximumSize(self.size())
#region Testing Section
        self.switchTestingPage()

        #self.switchFrontDeskDashboard()
#endregion

#region Connecting Interactivity 
        #Welcome Page

        self.Welcome.loginCustomerBtn.clicked.connect(lambda : self.switchCustomerLoginPage())
        self.Welcome.loginAdminBtn.clicked.connect(lambda : self.switchAdminLoginPage())

        #Customer Page

        self.CustLogin.loginBtn.clicked.connect(lambda : self.LoginTenantBTN(self.CustLogin.emailInput.toPlainText(),self.CustLogin.passwordInput.toPlainText()))
        self.AdminLogin.loginBtn.clicked.connect(lambda : self.switchFrontDeskDashboard())

        self.CustLogin.signUpBtn.clicked.connect(lambda : self.switchCustomerSignUp())
        self.CustSignUp.submitBtn.clicked.connect(lambda : self.SignUpUser(self.CustSignUp.emailInput.toPlainText()))

        #Testing Page
        self.TestingPage.testBtn1.clicked.connect(lambda : self.MakePieChartUnoccupied("Madrid"))
        self.TestingPage.testBtn2.clicked.connect(lambda : self.MakePieChartUnoccupied("London"))
        self.TestingPage.testBtn3.clicked.connect(lambda : self.MakeLineChartMaintanenceRequests("London"))
        #self.TestingPage.testBtn4.clicked.connect(lambda : )

        #Front Desk Page
        self.FrontDeskDash.submitButton.clicked.connect(lambda : self.RegisterTenant(self.FrontDeskDash.Submit()))
#endregion

#region Page Functions
    def switchWelcomePage(self):
        self.stackedView.setCurrentIndex(0)
    
    def switchCustomerLoginPage(self):
        self.stackedView.setCurrentIndex(1)
    
    def switchAdminLoginPage(self):
        self.stackedView.setCurrentIndex(2)
    
    def switchCustomerView(self):
        #Change when page is implemented to customer dashboard
        self.stackedView.setCurrentIndex(3)

    def switchAdminView(self):
        #Change when page is implemented to customer dashboard
        self.switchWelcomePage()
    
    def switchCustomerSignUp(self):
        self.stackedView.setCurrentIndex(4)


    def switchTestingPage(self):
        self.stackedView.setCurrentIndex(5)
    
    def switchCustomerSignUpDetailed(self, email : str):
        self.stackedView.setCurrentIndex(6)
        self.DetailedSignUp.emailInput.setText(email)
    
    def switchFrontDeskDashboard(self):
        self.stackedView.setCurrentIndex(7)
        self.FrontDeskDash.UpdateTenants(GetTenants(),GetHeaders("tenants"))
        self.FrontDeskDash.searchBar.textChanged.connect(lambda : self.FrontDeskDash.tenantTable.search(self.FrontDeskDash.searchBar.text()))
#endregion

#region Interaction Functions
    def SignUpUser(self, email : str):
        error = CheckEmailIsValid(email)
        if error is not None:
            #Must be set to self to allow for this box to be made
            title = "Tenant Already Exists"
            description = "This email has already been used to sign up a user. Please try a different email."
            error = ErrorMessage(title, description)
            self.errorBox = self.errorBox(error)
            self.errorBox.show()
        else: 
            #Changes the page to the detailed sign up
            self.switchCustomerSignUpDetailed(email)

    def RegisterTenant(self, user):
        error = CheckEmailIsValid(user[2])
        if error is not None:
            title = "Tenant Already Exists"
            description = "This email has already been used to sign up a user. Please try a different email."
            error = ErrorMessage(title, description)
            self.errorBox = self.errorBox(error)
            self.errorBox.show()
        else: 
            SignUpUser(user[0], user[1],user[2],user[3],user[4],user[5],user[6])
            self.switchFrontDeskDashboard()

    def LoginTenantBTN(self, email: str, password : str):
        user = LoginUser(email,password)

        if user is None:
            self.errorBox = ErrorBox(ErrorMessage("No User Found", "The credentials do not match any known user"))
            self.errorBox.show()

    def getTenantsTable(self):
        records = GetTenants()
        headers = GetHeaders("tenants")
        return Table(records,headers)

    def getLocationsTable(self):
        records = GetLocations()
        headers = GetHeaders("locations")
        self.table = Table(records,headers)
        self.table.show()
    def OccupancyLevelsTesd(self):
        print(GetUnoccupiedApartmentsForLocation("London"))
        print(GetUnoccupiedApartmentsForLocation("Madrid"))
        print(GetUnoccupiedApartmentsForLocation("Spain"))
    
    def MakePieChartUnoccupied(self, locationName : str):
        location = GetLocation(locationName)
        if location is None:
            self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
            self.error.show() #Change to ann error manager
        else:
            apartments = GetApartmentsFromLocation(location[0])
            if apartments != None:
                total = len(apartments)
                unoccupied = GetUnoccupiedApartmentsForLocation(location[0])
                if unoccupied is None:
                    self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
                    self.error.show() #Change to ann error manager
                else:
                    unoccupied = len(unoccupied)
                    self.pie = PieChart(("Occupied","Unoccupided") , (total - unoccupied, unoccupied) , "Occupied vs Unoccupided of " + locationName)
                    self.pie.show()
        print("Done")

    def MakeLineChartMaintanenceRequests(self, locationName : str):
        location = GetLocation(locationName)
        if location is None:
            self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
            self.error.show() #Change to ann error manager
        else:
            requests = GetMainanenceRequestsForLocation(location[0])
            apartments = GetApartmentsFromLocation(location[0])
            print(len(requests))
            print(len(apartments))
            self.pie = PieChart(labels= ("Repairs In Progress", "Functional"),numData= ((len(requests)), len(apartments) - len(requests)) ,title= "Repairs in progress vs functional rooms")
            self.pie.show()
        print("Done")
#endregion

#region App
app = QApplication()

#Creates a main window and places the ui created in designer onto it 
mainWindow = mainScreen()

mainWindow.show()

app.exec()

#endregion




#TODO Have a look over and see if you can swap around how the mainwindow works its a tad inconsisitent