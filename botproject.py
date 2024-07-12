print("A SIMPLE PYTHON CHATBOT")

name=input("What is your name? ")
print(f"Hello {name}!! I'm a chatbot")

hobby=input(f"Do you want to share your hobbies with me, {name}?")
print (f"{hobby} is such an interesting thing to do! Would you like to tell me your age?")

age=input()
temp_age=int(age)
print(f"So you're {temp_age} years old. Do you wanna know my age?")

bot_age=2
choice=input()

if choice=='Yes':
    print (f"I'm {bot_age} years old. How about you tell me what are you studying?")
else:
    print ("It's alright. What are you studying?")

study=input()
print(f"{study} is an interesting field, I'm sure you enjoy it!")

print("Let me know if you wanna talk about something else. Bye!!!!")
input("Say Bye?")
