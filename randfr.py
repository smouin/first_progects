import random
print("Welcome to the \"random friend will pay\" for us script : ")
ppl = input("pleas enter the names separated by spaces:  ")
list_of_ppl = ppl.split(" ")
random_prs = list_of_ppl[random.randint(0,len(list_of_ppl))-1]
print(f"{random_prs} will pay the bill for you all .")


