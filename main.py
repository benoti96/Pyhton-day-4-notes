#To first begin using the random module which we can use to generate random numbers, we need to import it 
import random
import my_module #I need to import a module before I can use it

random_integer = random.randint(20,40)
print(random_integer) # gives us any random number between 20 to 40
print(my_module.salary) # in my module module I have a piece of data called salary. This is how I print it.

random_float = random.random()
print(random_float) # This code generates random float numbers


#==================================
#Below is a code showing us how to get computer to randomly generate heads or tails
random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

#===============================================
#List is a set of square bracket with any data type stored inside it.
#currencies = "Bitcoin, XRP, Matic"
#currencies_in_a_list = currencies.split(",")
#print(currencies_in_a_list) #Computer generates: ['Bitcoin', ' XRP', ' Matic']


#print(isinstance(1,int))


#=======================

#This code gives us a random name from a list we write which tells us who pays the bill
names_string  = input("Write out the names of everyone & seperate it with commas. ")
name = names_string.split(",") #this split function puts things into a list.

#number_of_name = len(name) # tells us number of names written in line 33

#random_name = random.randint(0, number_of_name - 1) # generates a random name from 0 to the last item list in line 33

#person_who_will_pay = name[random_name]

#print(f"Person who will pay is {person_who_will_pay}")

#Another way to write this code is:
person_who_will_pay = random.choice(name) # the choice function generates a random name in a list

print(f"Person who will pay is {person_who_will_pay}")





