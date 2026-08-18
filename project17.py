import random
username = input("Enter your username: ")
vibes = ["its_","nigger_","bitch_","ass_","dumb_","stupid_"]
for i in range(5) :
    print(username + random.choice(vibes)+str(random.randint(5, 10)))