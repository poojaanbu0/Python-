class Animal():
	pass
   
class Dog(Animal):
	pass
   
   
sparky = Dog()
print(isinstance(sparky, Dog))
print(isinstance(sparky, Animal))
print(isinstance(sparky,(int , str, Animal)))
print("\n")
print(type(sparky) is Animal)
print(type(sparky) == Dog)
print(type(sparky)== Animal)
print(type(sparky))
print(type(Dog))
print(type(Animal))
print("\n")
bo = True
print(isinstance(bo,int))
print(type(bo) is int)