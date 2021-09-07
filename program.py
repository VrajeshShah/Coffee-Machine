from resourceexceptions import ResourceError
import jsonoperations
from coffeemachine import CoffeeMachine

def refillConsole(coffeeMachine):
        try:
                ingredientName=input("\nEnter Ingredient Name: ")
                ingredientValue=int(input("\nEnter Ingredient Value: "))
                coffeeMachine.reFillSingleIngredient(ingredientName,ingredientValue)
        except:
                print("Something Went Wrong!!Please Enter Try Again!!")
                input()

def printDrinkDetails(coffeeMachine):
        print("\n\nMenu:\n\n")
        for i in coffeeMachine.recipes:
                print(i)
        print("\n\n")

def singleBuyConsole(coffeeMachine):
        try:
                printDrinkDetails(coffeeMachine)
                drinkName=input("\nEnter Drink Name: ")
                print(coffeeMachine.buy(drinkName))
        except:
                print("Something Went Wrong!!Please Enter Try Again!!")
                input()

def multipleBuyConsole(coffeeMachine):
        try:
                printDrinkDetails(coffeeMachine)
                conncurrentUsers=input("\nEnter Drink Name(Comma Seperated): ").split(',')
                coffeMachineOutput=coffeeMachine.buyMultiple(conncurrentUsers)  
                print("\n".join(coffeMachineOutput))
        except:
                print("Something Went Wrong!!Please Enter Try Again!!")
                input()

if __name__ == '__main__':    
    coffeeMachineJson=jsonoperations.readCoffeeMachineJson("data.json")
    coffeeMachine=CoffeeMachine(coffeeMachineJson['machine']['outlets']['count_n'],coffeeMachineJson['machine']['total_items_quantity'],coffeeMachineJson['machine']['beverages'])
    message='''
            1. Refill Coffee Machine
            2. Get Ingredient Status
            3. Single Customer Buy
            4. Multiple Customer Buy
            5. Exit
            '''
    while(True):
                print(message)
                inputValue=int(input("\n\nPlease Enter Your Choice:"))
                try:
                        if inputValue==1:
                                refillConsole(coffeeMachine)
                        elif inputValue==2:
                                coffeeMachine.ingredientStatus()
                        elif inputValue==3:
                                singleBuyConsole(coffeeMachine)
                        elif inputValue==4:
                                multipleBuyConsole(coffeeMachine)
                        elif inputValue==5:
                                break
                        else:
                                print("Invalid Option Selected!!Please Enter Try Again!!")
                                input()
                except:
                        break