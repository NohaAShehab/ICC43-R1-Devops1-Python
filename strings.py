print("----------------------strings------------------")

# coursename = "pythonn"
#
# # print(type(coursename))
# "1- you get the len of the string "
# print(len(coursename))
# "2- string is treated like an array ---> you can access chars using index , start from zero"
# print(coursename[3])
# "3- count number of chars in the string"
# print(coursename.count("n"))
# "4- get index of char in the string "
# print(coursename.index("o"))
"5- concatenate the string"
firstname = "Noha "
midname = "Abd El-Hady "
lastname= "Shehab"

# fullname = firstname + midname + midname + lastname
# print(fullname)

"6- string interpolation"
#
# fullname = firstname + midname * 2 + lastname
# print(fullname)

"7- replace part of the string "
# name= "Nohaaaaaaaa"
# print(name.replace("a", "@"))


"8- format string "
# template = "I love {0}, I studied it at {1}"
# # print(template.format("Python", "iti"))
# # print(template.format("Java", "Engineering"))
# print(template.format("Engineering", "java"))

# template = "I love {coursename}, I studied it at {place}"
# print(template.format(place="iti", coursename="python"))
# "9- f-format string "

# ask use to enter his name then print hello user
# username = input("Please enter your name ")
# print(type(username))
# msg = "Hello " + username
# print(msg)
# msg= f"Hello {username}"
# print(msg)

# work = "Information Technology Institute"
# print(work[2:8])  # from position 2 to n-1

##########################
# "11- capatalize"
# message = "nice to meet you all today."
# print(message.capitalize())
# print(message.upper())
# print(message.lower())
# print(message.isupper())
# print(message.islower())
########################
"12- strip string "
# message = "                           Hello           world                                  "
# print(message)
# print(len(message))
# print(message.strip())  # remove spaces from the beginning and the end of string
# print(len(message.strip()))


# message = "    My name is Noha   @  "
# print(message.strip("@ M"))


# message = "    My name is Noha   @  "
# print(message.lstrip("@ M"))
# print(message.rstrip("@ M"))

################################################################
# "13- check the value of the string "
# name = input("please enter your name ")
# print(type(name))
# age = input("please enter your age")  # Always string
# print(type(age))
#
# ## string, alpha , numeric , spaces
# print(name.isalpha())  ## all char are in [a-z]
#
# print(name.isspace())
#
# print(age.isdigit())
#
# print(age.isnumeric())
##################################### type conversion (casting )#########################################

"--- convert from int to string ----- "
# x = 10
# x = str(x)

"15- ---- convert from str to int------------------------"
# age = input("please enter your age ") #numeric string
# if age.isdigit():
#     age = int(age)
"---------------------Operators ---------------------- "
# x = 10
# x += 5 ## x = x +5  ---> 15

# print(200 and 1000 and "iti")  # 200 ---> represent true
#
# print(100 and False and "iti")
# print(100 and 0 and "iti")

print(200 or 1000 or "iti")  # 200 ---> represent true

print(100 or False or "iti")
print(0 or "iti")

"""
    0 == False
    1 == True
    
    'iti' represent True 
    --------------------------------- Falsy values 
    0 , {}, [], '', False, None , ()
"""
c = 4+5j
c2 = complex(5,6)

#######################################################################



















