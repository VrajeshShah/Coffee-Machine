from threading import Thread
from resourceexceptions import NotEnoughSupplyError, RecipeNotFound, ResourceError
from multiprocessing import Lock, Manager, Pool


class CoffeeMachine():
    noOfOutlets=1
    ingredients={}
    recipes={}
    minimumIngrediantRequired=1
    running=False
    lock = Lock()
    def __init__(self,outlets,ingreds,recipe):
        if outlets>0:
            self.noOfOutlets=outlets
        self.ingredients=Manager().dict(ingreds)
        self.recipes=Manager().dict(recipe)
        for i in self.recipes:
            for j in self.recipes[i]:
                self.minimumIngrediantRequired=min(self.minimumIngrediantRequired,int(self.recipes[i][j]))

        if self.minimumIngrediantRequired<1:
            self.minimumIngrediantRequired=1
    
    def reFill(self,reFillIngredients):
        rValue=True
        if self.running:
            print("Machine Is Running!Please Try Again")
            return False
        if not isinstance(reFillIngredients,dict):
            raise Exception("Invalid Argument Type")
        
        for i in reFillIngredients:
            if i not in self.ingredients:
                self.ingredients[i]=0
            self.ingredients[i]+=reFillIngredients[i]
        return rValue
        
    def reFillSingleIngredient(self,ingredientName,ingredientValue):
        rValue=True
        reFillIngredients={}
        if ingredientValue>0:
            reFillIngredients[ingredientName]=ingredientValue
            rValue=self.reFill(reFillIngredients)
        return rValue
    
    def ingredientStatus(self):
        if self.running:
            print("Machine Is Running!Please Try Again")
            return
        for i in self.ingredients:
            if self.ingredients[i]<self.minimumIngrediantRequired:
                print(i+"\t\t\t"+"Low")
            else:
                print(i+"\t\t\t"+"Ok")
    
    def checkIngredientAvailability(self,receipeName):
        for i in self.recipes[receipeName]:
            if i not in self.ingredients:
                raise ResourceError(None,i)
            if self.recipes[receipeName][i]>self.ingredients[i]:
                raise NotEnoughSupplyError(None,i)
    
    def consumeIngredients(self,receipeName):
        for i in self.recipes[receipeName]:
            self.ingredients[i]=self.ingredients[i] - self.recipes[receipeName][i]
                
    def buy(self,beverage):
        rValue=''
        self.running=True
        try:
            if beverage not in self.recipes:
                raise RecipeNotFound("{0} Receipe Do not Exist".format(beverage))
            self.lock.acquire()
            self.checkIngredientAvailability(beverage)
            self.consumeIngredients(beverage)
            self.lock.release()
            rValue ="{0} is prepared".format(beverage)
        except ResourceError as ex:
            rValue="{0} cannot be prepared because {1} is not available".format(beverage,ex.resourceName)
            self.lock.release()
        except NotEnoughSupplyError as ex:
            rValue="{0} cannot be prepared because item {1} is not sufficient".format(beverage,ex.resourceName)
            self.lock.release()  
        except RecipeNotFound as ex:
            rValue=str(ex)
        self.running=False
        return rValue
    
    def buyMultiple(self,beverages):
        rValue=[]
        with Pool(self.noOfOutlets) as p:
            rValue=p.map(self.buy, beverages)
        return rValue
        
        

