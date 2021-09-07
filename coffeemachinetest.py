from multiprocessing import RawValue
from resourceexceptions import ResourceError
import jsonoperations
from coffeemachine import CoffeeMachine
import unittest

#Contains Unit Test Cases + Functional Test Cases

class TestStringMethods(unittest.TestCase):

    def test_jsonFileDoNotExists(self):
        self.assertRaises(Exception, jsonoperations.readCoffeeMachineJson,"data1.json")
    
    def test_jsonDoestNotFollowProtocol(self):
        self.assertRaises(Exception, jsonoperations.readCoffeeMachineJson,"wrongdata.json")

    def test_wrongDataProvidedCoffeeMachineClass(self):
        self.assertRaises(Exception, CoffeeMachine,-1,123,None)

    def test_recipeDoNotExists(self):
        coffeeMachine=CoffeeMachine(3,{},{})
        rValue=coffeeMachine.buy("Coffee")
        self.assertEqual(rValue, "Coffee Receipe Do not Exist")

    def test_ingrediantDoesNotExists(self):
        coffeeMachineJson=jsonoperations.readCoffeeMachineJson("data.json")
        coffeeMachine=CoffeeMachine(coffeeMachineJson['machine']['outlets']['count_n'],{},coffeeMachineJson['machine']['beverages'])
        rValue=coffeeMachine.buy("hot_tea")
        self.assertEqual(rValue, "hot_tea cannot be prepared because hot_water is not available")
    
    def test_everyThingWorksForSingleBeverage(self):
        coffeeMachineJson=jsonoperations.readCoffeeMachineJson("data.json")
        coffeeMachine=CoffeeMachine(coffeeMachineJson['machine']['outlets']['count_n'],coffeeMachineJson['machine']['total_items_quantity'],coffeeMachineJson['machine']['beverages'])
        rValue=coffeeMachine.buy("hot_tea")
        self.assertEqual(rValue, "hot_tea is prepared")
    
    def test_everyThingWorks(self):
        actualOutput=['hot_tea is prepared', 'hot_coffee is prepared', 'green_tea cannot be prepared because item sugar_syrup is not sufficient', 'black_tea cannot be prepared because item hot_water is not sufficient']
        coffeeMachineJson=jsonoperations.readCoffeeMachineJson("data.json")
        coffeeMachine=CoffeeMachine(coffeeMachineJson['machine']['outlets']['count_n'],coffeeMachineJson['machine']['total_items_quantity'],coffeeMachineJson['machine']['beverages'])
        conncurrentUsers=["hot_tea", "hot_coffee", "green_tea","black_tea"]
        coffeMachineOutput=coffeeMachine.buyMultiple(conncurrentUsers)  
        self.assertTrue(actualOutput[0] in coffeMachineOutput) 
        self.assertTrue(actualOutput[1] in coffeMachineOutput)
        self.assertTrue(actualOutput[2] in coffeMachineOutput)
        self.assertTrue(actualOutput[3] in coffeMachineOutput) 
    
    def test_everyTypeOfOutput(self):
        actualOutput=['hot_tea is prepared', 'hot_coffee is prepared', 'green_tea cannot be prepared because green_mixture is not available', 'black_tea cannot be prepared because item hot_water is not sufficient']
        coffeeMachineJson=jsonoperations.readCoffeeMachineJson("changeddata.json")
        coffeeMachine=CoffeeMachine(coffeeMachineJson['machine']['outlets']['count_n'],coffeeMachineJson['machine']['total_items_quantity'],coffeeMachineJson['machine']['beverages'])
        conncurrentUsers=["hot_tea", "hot_coffee", "green_tea","black_tea"]
        coffeMachineOutput=coffeeMachine.buyMultiple(conncurrentUsers)  
        self.assertTrue(actualOutput[0] in coffeMachineOutput) 
        self.assertTrue(actualOutput[1] in coffeMachineOutput)
        self.assertTrue(actualOutput[2] in coffeMachineOutput)
        self.assertTrue(actualOutput[3] in coffeMachineOutput)
    
    def test_wrongDataProvidedForOutlet(self):
        coffeeMachineJson=jsonoperations.readCoffeeMachineJson("changeddata.json")
        coffeeMachine=CoffeeMachine(0,coffeeMachineJson['machine']['total_items_quantity'],coffeeMachineJson['machine']['beverages'])
        self.assertEqual(coffeeMachine.noOfOutlets, 1)

if __name__ == '__main__':
    unittest.main()
