class vending_machine:
    def __init__(self,soda,water,coffee):
        self.soda=soda
        self.water=water
        self.coffee=coffee

    def buy(self):
        print('Please select an option')
        print('1 - Soda')
        print('2 - Water')
        print('3 - Coffee')

        option=int(input('Enter your option: '))
        if option==1:
            if self.soda>0:
                self.soda-=1
            else:
                print('Soda out of stock')
        elif option==2:
            if self.water>0:
                self.water-=1
            else:
                print('Water out of stock')
        elif option==3:
            if self.coffee>0:
                self.coffee-=1
            else:
                print('Coffee out of stock')
        else:
            print('Invalid option')

    def inventory(self):
        print("Inventory")
        print(f'Soda: {self.soda}')
        print(f'Water: {self.water}')
        print(f'Coffee: {self.coffee}')

    def restock(self):
        print('Please select an option')
        print('1 - Soda')
        print('2 - Water')
        print('3 - Coffee')

        option=int(input('Enter your option: '))
        restock_amt=int(input('Please enter the amount: '))

        if option==1:
            self.soda+=restock_amt
        elif option==2:
            self.water+=restock_amt
        elif option==3:
            self.coffee+=restock_amt
        else:
            print('Invalid option')
    

def main():
    vending_machine1=vending_machine(5,5,5)
    while True:
        user_input=input(':>')
        if user_input in ['q','quit','exit','e']:
            break
        if user_input=='buy':
            vending_machine1.buy()
        elif user_input=='inventory':
            vending_machine1.inventory()
        elif user_input=='restock':
            vending_machine1.restock()
        else:
            print('Invalid option')

main()