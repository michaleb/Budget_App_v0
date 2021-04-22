class Category:
    
    #constructor
    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount
    
    #methods
    def deposit(self, amount):
        self.amount += amount
        return "'\nYou have successfully deposited ${} into the {} budget".format(amount, self.category)

    def budget_balance(self):
        return "The current balance for the {} budget is ${}".format(self.category, self.amount)

    def check_balance(self, amount):
        #this should return a True or False, it checks if amount is less or greater than self.amount
        good_balance = False
        if amount <= self.amount:
            good_balance = True
            #print("Funds available, transfer approved!!")
        
        return good_balance


    def withdraw(self, amount):
        #reverse of deposit
        self.amount -= amount
        return "You have successfully withdrawn {} from {} category".format(amount, self.category)


    def transfer(self, amount, other):
        #transfer between two instantiated categories
        print("\n###############################")
        print("###        TRANSFERS        ###")
        print("###############################\n")
        funds_available = self.check_balance(amount)
        
        if funds_available:
            self.withdraw(amount)
            #print(self.budget_balance())
            other.deposit(amount)
            print("You have successfully transferred ${} from {} to {} budget".format(amount, self.category, other.category))
            
        else:
            print("Insufficient funds, Transfer not completed")

        mesg = [self.budget_balance(), other.budget_balance()]
        return '\n'.join(mesg)
        


food_category = Category("Food", 500)
clothing_category = Category("Clothing", 300)
car_category = Category("Car Expenses", 600)

print(food_category.deposit(250))
print(food_category.budget_balance())
print(food_category.transfer(400, clothing_category))