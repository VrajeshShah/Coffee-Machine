import json
def readJson(fileName):
    rValue={}
    with open(fileName, 'r') as jsonFile:
        rValue = json.load(jsonFile)
    return rValue

def readCoffeeMachineJson(fileName):
    rValue=readJson(fileName)
    if 'machine' not in rValue:
        raise Exception("Invalid Json")
    if 'outlets' not in rValue['machine']:
        raise Exception("Invalid Json") 
    if 'total_items_quantity' not in rValue['machine']:
        raise Exception("Invalid Json")  
    if 'beverages' not in rValue['machine']:
        raise Exception("Invalid Json")    
    return rValue