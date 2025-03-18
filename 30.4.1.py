#Create an empty class 'Car'
class Car():
    pass

#Create an empty class 'Electronics'
class Electronics():
    pass

#Create an empty class 'Animal'
class Animal():
    pass

#Create instances of each class
lamborghini = Car()
playstation = Electronics()
cat = Animal()

#Assigning attributes
lamborghini.colour = "red"
lamborghini.horsepower = 40

playstation.ram = "32GB"
playstation.storage = "5TB"

cat.breed = "Siamese"
cat.eyeColour = "Brown"

#Print the results
print(f"Lamborghini colour: {lamborghini.colour}")
print(f"Playstation ram: {playstation.ram}")
print(f"Cat breed: {cat.breed}")
