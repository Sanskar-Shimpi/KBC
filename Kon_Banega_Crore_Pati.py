from inputimeout import inputimeout
from termcolor import colored
import time as t


print("Note: 30 seconds for each question\n")
print("------------------------------------------------------------\n")


def question_1():
	"""QUESTION ONE"""

	
	print(f"★First Question For 1 Lakh\n")

	q1=["What is capital of India?"]
	print(q1)

	options=["\n1] New Delhi", "2] Mumbai", "3] Assam", "4] Madhya Pradesh\n"]

	for items in options:
		print(items)

	try:	
		user_ans_1= 								int(inputimeout(prompt='Enter Option Number: ', timeout=30))
	except:
		user_ans_1 = ''

	if (user_ans_1 == 1):
		print(colored(f"\nCorrect! You Won 1,00,000\n", "green"))

	elif (user_ans_1 == 2 or user_ans_1==3 or user_ans_1 == 4):
		print(colored("\nWrong Option Selected\n", "yellow"))

	else:
		print(colored("\nOut Of Time!\n", "yellow"))

#question_1()
#print(question_1.__doc__)




#-----------------------------------------------------------"




def question_2():
	"""Question 2"""
	
	print("\n★Second Question For 2 Lakh\n")
	q2= ["India lies in which continent?"]
	print(q2)
	
	option_2= ["\n1] North American Continent", "2] European Continent", "3] Asian Continent", "4] South American Continent"]
	
	for items in option_2:
		print(items)
		
	try:	
		user_ans_2= int(inputimeout(prompt="\nEnter Option Number: ", timeout=30))
	except:
		user_ans_2=""
	
	if (user_ans_2 == 1 or user_ans_2 == 2 or user_ans_2 == 4):
		print(colored("\nWrong Option Selected", "yellow"))
	elif(user_ans_2==3):
		print(colored("\nCorrect Answer! You Won 2,00,000", "green"))
	else:
		print(colored("\nOut Of Time!", "yellow"))
		


#question_2()
		


#"------------------------------------------------------------"



def question_3():
	"""Question 3"""
	
	print("\n★Third Question For 3.5 Lakh\n")
	q3= ["GST is implemented in India from..."]
	print(q3)
	
	option_3= ["\n1] March 2017", "2] June 2017", "3] July 2017", "4] August 2017"]
	
	for items in option_3:
		print(items)
		
	try:
		user_ans_3= int(inputimeout(prompt="\nEnter Option Number: ", timeout=30))
	except:
		user_ans_3=""
	
	if (user_ans_3 == 1 or user_ans_3 == 2 or user_ans_3 == 4):
		print(colored("\nWrong Option Selected", "yellow"))
	elif(user_ans_3==3):
		print(colored("\nCorrect Answer! You Won 3,50,000", "green"))
	else:
		print(colored("\nOut Of Time!", "yellow"))
		
#question_3()



#"------------------------------------------------------------"

def question_4():
	"""Question 4"""
	
	print("\n★Fourth Question For 5 Lakh\n")
	q4= ["Which port is called 'Queen Of Arabian Sea'?"]
	print(q4)
	
	option_4= ["\n1] Kochi", "2] Mumbai", "3] Surat", "4] Kandla"]
	
	for items in option_4:
		print(items)
	try:	
		user_ans_4= int(inputimeout(prompt="\nEnter Option Number: ", timeout=30))
	except:
		user_ans_4=""
	
	if (user_ans_4 == 2 or user_ans_4 == 36 or user_ans_4 == 4):
		print(colored("\nWrong Option Selected", "yellow"))
	elif(user_ans_4==1):
		print(colored("\nCorrect Answer! You Won 5,00,000", "green"))
	else:
		print(colored("\nOut Of Time", "yellow"))



#("------------------------------------------------------------")


def question_5():
	"""Question """
	
	print("\n★Fifty Question For 7 Lakh\n")
	q5= ["Who invented/designed Python?"]
	print(q5)
	
	option_5= ["\n1] Guido van Rossum", "2] Tim Berners-Lee", "3] Bjarne Stroustrup", "4] Non Of Above"]
	
	for items in option_5:
		print(items)
	try:	
		user_ans_5= int(inputimeout(prompt="\nEnter Option Number: ", timeout=30))
	except:
		user_ans_5=""
	
	if (user_ans_5 == 2 or user_ans_5 == 3 or user_ans_5 == 4):
		print(colored("\nWrong Option Selected", "yellow"))
	elif(user_ans_5 ==1):
		print(colored("\nCorrect Answer! You Won 7,00,000", "green"))
	else:
		print(colored("\nOut Of Time", "yellow"))
		
		
#-----------------------------------------------------------------------------------------------------------------------------------------

question_1()

print("------------------------------------------------------------")

question_2()

print("------------------------------------------------------------")

question_3()

print("------------------------------------------------------------")

question_4()

print("------------------------------------------------------------")

question_5()

print("------------------------------------------------------------")

#currently coding on mobile, python-3.9 therefore can't use match-case method!


print("Wait a moment! Don't press any key!")

for i in range(5):
	t.sleep(1)

print("\nWe will shortly mail, total amount you won!")
inpt=(input("\nEnter your mail adderess: "))

if (inpt.__contains__("@")):
	print("\nThank You!")
	exit()
else:
	print("\nInvalid E-mail")
	exit()
#Project By ~Sanskar Shimpi
