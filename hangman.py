import random
def hangman(word_list):
	word = random.choice(word_list)
	wrong = 0
	stages = ["",
	"_________         ",
	"|                 ",
	"|          |      ",
	"|          O      ",
	"|         /|\     ",
	"|         / \     ",
	"|                 "
	]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("Welcome to Hangman")
	while wrong < len(stages) - 1:
		print("\n")
		msg = "Guess a letter"
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print("You win!")
			print(" ".join(board))
			win = True
			break

	if not win:
		print("\n".join(stages[0:wrong]))
		print("You lose! It was {}.".format(word))

hangman(['cat', 'dog', 'bird', 'fish', 'pig'])

