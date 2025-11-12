from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         """Abstract method for calculating area."""
#         pass

#     @abstractmethod
#     def perimeter(self):
#         """Abstract method for calculating perimeter."""
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         """Implementing the area method for rectangle."""
#         return self.width * self.height

#     def perimeter(self):
#         """Implementing the perimeter method for rectangle."""
#         return 2 * (self.width + self.height)

# # # Usage
# rect = Rectangle(10, 5)
# print("Area of rectangle:", rect.area())
# print("Perimeter of rectangle:", rect.perimeter())

# rect=Shape()
# rect.area()


# class car(ABC):
#     def show(self):
#         print("car....")
#     @abstractmethod
#     def speed(self):
#         pass

# class maruti(car):
#     def speed(self):
#         print("Speed is 100...")

# class suzuki(car):
#     def speed(self):
#         print("Speed is 70....")

# obj=maruti()
# obj.speed()
# obj.show()
# obj1=suzuki()
# obj1.show()
# obj1.speed()

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# dog = Dog()
# print(dog.sound())
# cat = Cat()
# print(cat.sound())


# from abc import ABC,abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def rectangle(self):
#         pass

#     def circle(self):
#         print("circle")  
# class show(shape):
#     def __init__(self,width,height) :
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width *self.height

#     def rectangle(self):
#         return 2*(self.width+self.height)
# obj=show(10,5)
# print("area is",obj.area())
# print("perimeter is",obj.rectangle())
# obj.circle()














############interface
# from abc import ABC , abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def show(self):
#         pass

# class square(shape):
#     def show(self):
#         print("Square")
# class circle(shape):
#     def show(self):
#         print("Circle")

# # k=shape()
# s=square()
# s.show().
# c=circle()
# c.show()

# from abc import ABC, abstractmethod

# class Payment(ABC):
    
#     @abstractmethod
#     def pay(self, amount):
#         pass
# class CreditCard(Payment):
#     def pay(self, amount):
#         return f"Paid {amount} using Credit Card."
# class PayPal(Payment):
#     def pay(self, amount):
#         return f"Paid {amount} using PayPal."

# credit_card = CreditCard()
# paypal = PayPal()
# print(credit_card.pay(100))
# print(paypal.pay(200))       

# from abc import ABC,abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def credit(self):
#         pass

#     @abstractmethod
#     def debit(self):
#         pass


# class show(payment):
#     def credit(self,amount):
#         return (f"{amount} paid by credit card")

#     def debit(self,amount):
#         return (f"{amount} paid by debit card ")

# obj=show()
# print(obj.credit(100))
# print(obj.debit(200))
# # obj.current()

# from abc import ABC
# class car(ABC):
#     def show(self):
#         print("Abstraction...")

#     @abstractmethod
#     def speed(self):
#         pass

#     def color(self):
#         print("white....")
# class maruti(car):
#     def speed(self):
#         print("speed is 100...")

# class suzuki(car):
#     def speed(self):
#         print("speed is 200...")b=20


# obj=suzuki()
# obj.speed()
# obj.show()
# obj.color()

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def rectangle(self):
#         pass

#     def circle(self):
#         print("Shape is circle....")

# class show(shape):
#     def __init__(self,width,height) :
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width*self.height
    
#     def rectangle(self):
#         return 2*(self.width+self.height)
    
# obj=show(10,5)
# print(obj.area())
# print(obj.rectangle())
# obj.circle()


# class shape(ABC):
#     @abstractmethod
#     def show(self):
#         pass

# class square(shape):
#     def show(self):
#         print("Square..")

# class circle(shape):
#     def show(self):
#         print("Circle...")

# # obj=shape()
# s=square()
# s.show()
# c=circle()
# c.show()

# class payment(ABC):
#     @abstractmethod
#     def debit(self):
#         pass

#     @abstractmethod
#     def credit(self):
#         pass

# class show(payment):
#     def debit(self):
#         print("payment debit rs.40000")

#     def credit(self):
#         print("20000 paid by credit card")

# obj=show()
# obj.credit()
# obj.debit()

# obj1=payment()

# from abc import ABC
# class A(ABC):


#     @abstractmethod
#     def credit(self):
#         pass

#     @abstractmethod
#     def debit(self):
#         pass

# class B(A):
#     def credit(self):
#         print("amount receive by creditt card")

#     def  debit(self):
#         print("amount receive by debit card")

# obj=B()
# obj.credit()
# obj.debit()
# obj.a()

    
class A():
    def show(self,__a,__b):
        self.__a=__a
        self.__b=__b

    def get(self):
        print(self.__a+self.__b)

class B(A):
    def hide(self):
         print(self.__a+self.__b)

obj=B()
obj.show(2,4)
obj.get()
obj.hide()