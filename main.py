print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

first_name = name1.upper()
second_name = name2.upper()
T = first_name.count("T") + second_name.count("T")
R = first_name.count("R") + second_name.count("R")
U = first_name.count("U") + second_name.count("U")
E = first_name.count("E") + second_name.count("E")
Total = T + R + U + E