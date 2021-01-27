#!/usr/bin/python3 
#Function that prints the solution to send to the judge
def imprimirsolucion(deliveries):
    
    # We print number of shipments
    print (len (deliveries))
    for between in deliveries:
        #We print each shipment generating a string and finally printing it
        #First, we put the shipment if it goes to a group of 4, 3 or 2
        cad = str (between [0])
        # We will go through the list to print which pizzas were in that shipment
        for element in between [1:]:
            cad = cad + "" + str (element)
        #We print the solution
        print (cad)


#Main program
def main ():
    # We declare variables to read total pizzas and total of each type of equipment
    nPizzas = 0
    nEq2 = 0
    nEq3 = 0
    nEq4 = 0
    # We read number of pizzas, teams of 2, 3 and 4 members
    nPizzas, nEq2, nEq3, nEq4 = map (int, input (). split ())
    # We declare a list with the pizzas that we will read
    pizzas = []
    # We read all the pizzas. We put them in a list each, ignoring the first element
    # The reason for ignoring the first element is that it tells us how many ingredients there are, but for 
    # save space we do not put it and we can always calculate with the "len" function
    for _ in range (nPizzas):
        pizzas.append (input (). split () [1:])

    #List that will contain the result of assigned pizzas
    res = []

    #As long as there are Pizzas and groups left, I create deliveries
    pizzaActual = 0
    
    #We assign pizzas first to groups of 4
    while (pizzaActual + 4 <= nPizzas and nEq4> 0):
        # Add the result
        res.append ([4, pizzaActual, pizzaActual + 1, pizzaActual + 2, pizzaActual + 3])
        pizzaActual = pizzaActual + 4
        nEq4 = nEq4-1
        
    #Then groups of 3
    while (pizzaActual + 3 <= nPizzas and nEq3> 0):
        res.append ([3, pizzaActual, pizzaActual + 1, pizzaActual + 2])
        pizzaActual = pizzaActual + 3
        nEq3 = nEq3-1

    #last groups of 2
    while (pizzaActual + 2 <= nPizzas and nEq2> 0):
        res.append ([2, pizzaActual, pizzaActual + 1])
        pizzaActual = pizzaActual + 2
        nEq2 = nEq2-1
    #print the result of res
    imprimirsolucion (res)
# Code to execute initial
main ()
