from module import gui
import random


def words1(score,guess_num):
    file = open('words.txt', 'r')
    infile = file.read().split()
    wordlist = []
    wordlist1 = []
    for word1 in infile:
        wordlist1.append(word1)
    word = random.choice(wordlist1)
    print('Enter difficulty level, 1 for Easy, 2 for Medium, 3 for Hard: ',end='')
    difficulty = input("")
    print()
    # easy difficulty
    if difficulty == '1':
        while not len(word) <= 7:
            word = random.choice(wordlist1)
            file.close()
    # medium difficulty
    elif difficulty == '2':
        while not 7 < len(word) <= 10:
            word = random.choice(wordlist1)
            file.close()
    # hard difficulty
    elif difficulty == '3':
        while not len(word) > 10:
            word = random.choice(wordlist1)
            file.close()

    while guess_num > 0:
        if guess_num == 9:
            for x in range(len(word)):
                wordlist.append('_')
            print("word: ", end="")
            for i in range(len(wordlist)):
                print(wordlist[i], end=" ")
            print('\n')
            guess = input("Enter your guess: ")
            inputs = [guess]

        if guess_num <= 8:
            guess = input("Enter your guess: ")
            try:
                inputs.index(guess)
                print("\nInput already given")
                continue
            except ValueError:
                inputs = [guess]
            '''for i in range(len(inputs)):
                if inputs[i] == guess:
                    print("Input already given\n")
                    continue
                else:
                    inputs = [guess]'''
        if guess_num == 9:
            guess_num -= 1
        count = 0
        for i in range(len(wordlist)):
            if word[i] == guess:
                wordlist[i] = guess
                count+=1
        if count>0:
            print("\nGood choice! %s is in the word %d times\n" %(guess,count))
        if guess not in word:
            print('\nIncorrect guess')
            guess_num -= 1

        if '_' not in wordlist:
            print('Correct answer')
            print("The word was %s\n" %word)
            score += 1
            break
        print("word : ", end="")
        for i in range(len(wordlist)):
            print(wordlist[i], end=" ")
        print()
        gui(guess_num,word)

    return(score)
