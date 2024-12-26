
#import ota api for microfocus alm to use the tdconnection object
from comtypes.client import CreateObject
from datetime import date

#credenttials to login to alm
url = "http://dev-testalm.cytiva.net/qcbin"
username ="admin.user" #"Alm.opshubuser"
password ="5QWU&.vW4$" #"DS%@dvk4ULc7Nt3#"
#ota connection object
#ota_connection = CreateObject("TDApiOle80.TDConnection")
ota_connection = CreateObject("TDAPIOLE80.TDConnection")
#project list
project_list =['MAGIC_GxP']
domain = "ENGINEERING"

#function to login to alm
def login_to_alm():
    ota_connection.InitConnectionEx(url)
    ota_connection.Login(username, password)
    return ota_connection.LoggedIn

#function to connect to project
def connect_to_project(domain, project):
    try:
        ota_connection.Connect(domain, project)
        print("Logged into to Project " + project)
        create_defect()        
    except Exception as e:
        print("Failed to login to Project " + project)
        print(e)

#function to create defect in ALM
def create_defect():
    i = 0    
    
    #    instance.post()
    #for oTestInstance in allTests:
    #    oTest = ota_connection.TestFactory.Item(oTestInstance.Field("TC_TEST_ID"))        
    #    print(oTest.id , ":", oTest.name)
    

#function to logout from alm
def logout_from_alm():
    ota_connection.Logout()
    ota_connection.Disconnect()
    print("Logged out from ALM")    

#function to get physical name of the field
def get_field_name(Fieldname):
    fieldlist = ota_connection.fields("Bug")
    for field in fieldlist:
        fieldprop = field.Property
        if fieldprop.userlabel == Fieldname:
            return fieldprop.dbcolumnname


if __name__ == "__main__":   
    login_result = login_to_alm()
    if login_result == True:
        print("Connected to ALM")
        for project in project_list:
            connect_to_project(domain, project)
    else:
        print("Not Connected to ALM")
    logout_from_alm()
