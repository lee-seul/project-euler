# coding: utf-8
# play_poker.py

from poker_rule import poker, high_card


game_list = open('game_list.txt').read().split('\n')
del game_list[-1]

for x in range(len(game_list)):
	game_list[x] = game_list[x].split(' ')


win = 0
for game in game_list:
	player1 = game[:5]
	player2 = game[5:]
	if poker(player1) > poker(player2):
		win += 1
	elif poker(player1) == poker(player2):
		if high_card(player1) > high_card(p_2):
			win+=1

print(win)




