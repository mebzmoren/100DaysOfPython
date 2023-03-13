#extend
watches = ['Casio', 'Seiko', 'Orient']
swiss_watches = ['Jaeger-LeCoultre', 'Omega', 'Patek Philippe']
watches.extend(swiss_watches)                                   #concatinates two lists to create one list
print(watches)

#operators
numbers = [1, 2, 3]
print(sum(numbers)) #sums up the value of the list
watches.remove('Omega')   #removes an element
print(watches)