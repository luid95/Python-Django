import random
#Get guess
def get_guess():
    return list(input("What's your guess"))

#GENERATE COMPUTER CODE 123
def generate_code():
    digits = [str(num) for num in range(10)]

    #Shuffle the digits
    random.shuffle(digits)
    #The grab the first three
    return digits[:3]

#generate clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

#Run game logic
print("Welcome Code Breaker")

secret_code = generate_code()

clue_report = []
while clue_report != "CODE CRACKED!":

    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess")
    for clue in clue_report:
        print(clue)
