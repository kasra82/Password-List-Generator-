import time
import random
import os
import sys
import string
import winsound
import strings
def passlist(password , len_pass) :
    characters = list(password)
    len_of_password = len(password)
    max_range_of_password = len_of_password ** len_of_password ** len_of_password
    password_list = []
    password_characters = ""
    for i in range(max_range_of_password) :
        for j in range(len_pass) :
            random_choice = random.choice(characters)
            password_characters += random_choice
            if len(password_characters) == len_pass :
                if password_characters not in password_list :
                    password_list.append(password_characters)
                password_characters = ""
        if len(password_list) == len_of_password ** len_pass :
            return password_list
            break
def passlist_1(password , len_pass) :
    characters = list(password)
    len_of_password = len(password)
    max_range_of_password = len_of_password ** len_of_password ** len_of_password
    password_list = []
    password_characters = ""
    for i in range(max_range_of_password) :
        for j in range(len_pass) :
            random_choice = random.choice(characters)
            password_characters += random_choice
        if password_characters not in password_list :
            if len(password_characters) == len_pass :
                password_list.append(password_characters)
            password_characters = ""
        if len(password_list) == len_of_password ** len_pass :
            return password_list
            break
sharp = '#'
example = 0
new_example = 10
sum_of_password = 0
string = input("Enter the String : ")
len_of_string = len(string)
min = input("Enter the Min of String Length : ")
max = input("Enter the Max of String Length : ")
filename = input("Enter the File Name : ")
min_ = int(min)
max_ = int(max)
while min_ <= max_ :
    sum = len_of_string ** min_
    sum_of_password += sum
    min_ += 1
min_ = int(min)
print("[+] { %s } Passwords Can Build [+]" % (sum_of_password))
ask = input("Continue [ Y / N ] : ")
if ask == "Y" or ask == "y" :
    if min_ == max_ :
        password_list = passlist(string , min_)
        file = open(filename , "+a")
        for i in password_list :
            file.write(i + "\n")
        file.close()
        print("Making Passwords...")
        while example <= new_example :
            print(sharp , end = '')
            example += 1
            time.sleep(0.1)
        print("    Done")
        size = os.path.getsize(filename)
        print("Size : {",size,"} Bytes")
    else :
        file = open(filename , '+a')
        for i in range(min_ , max_ + 1) :
            password_list = passlist_1(string , i)
            for i in password_list :
                file.write(i + "\n")
        file.close()
        print("Making Passwords...")
        while example <= new_example :
            print(sharp , end = '')
            example += 1
            time.sleep(0.1)
        print("    Done")
        size = os.path.getsize(filename)
        print("Size : {",size,"} Bytes")
elif ask == "N" or  ask == "n" :
    exit()
