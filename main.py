import random

def processar_escolha(escolha):
	opcao = ['rock', 'paper', 'scissors']

	if escolha in opcao:
		print(f'You chose {escolha}.')
		jogada_computador = random.choice(opcao)
		print(f'I played: {jogada_computador}!')
		if jogada_computador == escolha:
			print('Draw!')
			input()
			quit()
		elif (jogada_computador == 'rock' and escolha == 'scissors') or \
			(jogada_computador == 'scissors' and escolha == 'paper') or \
			(jogada_computador == 'paper' and escolha == 'rock'):
			perdeu()
		else:
			ganhou()
	else:
		print('Please, type a valid option between "rock", "paper" or "scissors".')


def escolher():
	while True:
		print('Rock, paper, scissors!')
		print('Select your choice (rock, paper ou scissors): ')
		escolha = str.lower(input())

		processar_escolha(escolha)


def ganhou():
	print('You won!')
	input()
	quit()


def perdeu():
	print('I win!')
	input()
	quit()


if __name__ == "__main__":
	escolher()
