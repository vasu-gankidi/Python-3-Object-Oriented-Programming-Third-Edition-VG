from importlib.machinery import FrozenImporter
import requests
import json


# end point url - https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD
# API KEY - 
# Base currency code - USD 
# API functionality - base currency and the Standard endpoint will 
# simply return the conversion rates from your base currency code
# to all the others we support in an easy to parse JSON format.
# 4c5a346356651dbf491d2cff

# Returns a response.
response = requests.get("https://v6.exchangerate-api.com/v6/4c5a346356651dbf491d2cff/latest/USD")

# extract the json from the response object.
data  = response.json()

#print(data)

# serialize the obj as json formatted stream to file pointer fp.
with open(r"C:\Users\vasu\OneDrive\Documents\PythonoopsDustinPhilips\PythonPractice\CurrencyConverter.json", "w") as fp:
    json.dump(data,fp)

# deserialize the json formatted stream and store into ResData variable.
with open(r"C:\Users\vasu\OneDrive\Documents\PythonoopsDustinPhilips\PythonPractice\CurrencyConverter.json",'r') as fp:
    ResData = json.load(fp)
    print(ResData)

# print(ResData["conversion_rate"]["USD"])

#FrmDumpData = json.dump(ResData)

# serialize python object to json formatted string for readability.
FrmDumpsData = json.dumps(ResData, indent = 2)

print("**************************************/n")

print(FrmDumpsData)

print("***********JSONEncoder****************/n")

# JSON Encoding Custom Objects
# JSONEncoder and JSONDecoder. custom serialization and deserialization.

# To extend this to recognize other objects, subclass and implement a
# *default)" method with another method that retums a serializable object for "o'" if possible, otherwise it should call the superclass implementation (to raise TypeError).

class Student:
    """Register Eid and name for the Student"""
    def __init__(self, name, Sid):
        self.name = name
        self.id = Sid

# TODO@vgankidi - Encoder class for Student returns Non serialized obj.    

class Employee:
    """Register Eid and name for the Employee"""
    def __init__(self, name, Eid):
        self.name = name
        self.id = Eid

# To serialize the class Employee.
class EmployeeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o , Employee):
            return { 'name' : o.name , 'id' : o.id }
        return super().default(o)

if __name__ == "__main__":
    e1 = Employee('vasu','1')
    print (json.dumps(e1, cls = EmployeeEncoder))
    try:
        e2 = Student('vasu','1')
        json.dumps(e2, cls = EmployeeEncoder) # How does this calls the defualt method in Employee class. Imp?
    except TypeError as e:
        print (f"Exception error {e}")