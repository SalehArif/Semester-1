from words import words1

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("This program plays a game of hangman.")
print("Guess letters in the mystery world.")
print("You can only make 8 incorrect guesses before you lose.")
print("See if you can guess the word before you run out of guesses...")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print()
name = input("Enter your name: ")
run = 'y'

score = 0
attempts = 0

while run == "y":
    guess_num = 9
    attempts += 1
    score1 = words1(score, guess_num)
    run = input("Do you want to play again? (y/n): ")
    if run != 'y':
        print(name, ', you scored ', score1, ' in %d attempts' %attempts)
        file = open('record.txt','a')
        file.write("\n%s\t%d\t%d" %(name,score1,attempts))
        file.close()
