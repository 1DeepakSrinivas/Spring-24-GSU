def pos():
    menu_items = ['Hot Dog','Slice of Pizza','Whole Pizza','Soft Drink']
    price_item=[1.50,1.99,9.95,0.59]
    menu=dict(zip(menu_items,price_item))

    qty_hd=int(input('Please enter the number of Hot Dogs: '))
    qty_sp=int(input('Please enter the number of Slices of Pizza: '))
    qty_wp=int(input('Please enter the number of Whole Pizzas: '))
    qty_sd=int(input('Please enter the number of Soft Drinks: '))

    total_cost=(qty_hd*menu['Hot Dog'])+(qty_sp*menu['Slice of Pizza'])+(qty_wp*menu['Whole Pizza'])+(qty_sd*menu['Soft Drink'])
    print('The total cost of the order is $',total_cost)
pos()