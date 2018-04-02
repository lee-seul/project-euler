# coding: utf-8
# poker_rule.py


#class poker():
#	cards = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8,'T':9,'J':10, 'Q':11, 'K':12, 'A':13}
#	def __init__(self, game):
#		player1 = self.game[:5]
#		player2 = self.game[5:]
#		
#	def flush(self):
#		suits = self.suits
#		return ssuits


def flush(suits):
	return suits.count(suits[0]) == 5

def straight(number_cards):
	l = []
	cards = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8,'T':9,'J':10, 'Q':11, 'K':12, 'A':13}
	for number in number_cards:
		l.append(cards[number])
	l.sort()
	if 'A' not in number_cards:
		for i in range(0, 5):
			if l[i] != l[0] + i:
				return False
	else:
		if l[1] == 12:
			for i in range(0, 5):
				if l[i] != l[0] + i:
					return False
		else:
			l[0] = 1
			for i in range(0, 5):
				if l[i] != l[0] + i:
					return False
	return l[0]

def four_cards(number_cards):
	for i in number_cards:
		if number_cards.count(i) == 4:
			return high_card(number_cards)
	return False

def full_house(number_cards):
	l = list(set(number_cards))
	if len(l) == 2:
		if number_cards.count(l[0]) == 3 and number_cards.count(l[1]) == 2:
			return high_card([l[0]])
		elif number_cards.count(l[1]) ==3 and number_cards.count(l[0]) == 2:
			return high_card([l[1]])	
	return False

def triple(number_cards):
	for i in number_cards:
		if number_cards.count(i) == 3:
			return high_card([i])
	return False

def two_pair(number_cards):
	num = 0
	l = []
	for i in number_cards:
		if number_cards.count(i) == 2:
			l.append(i)
			num += 1
	if num == 4:
		return high_card(l)
	else:
		return False

def one_pair(number_cards):
	for i in number_cards:
		if number_cards.count(i) == 2:
			return high_card([i])
	return False
			
def high_card(number_cards):
	cards = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8,'T':9,'J':10, 'Q':11, 'K':12, 'A':13}
	l = []
	for i in number_cards:
		l.append(cards[i])
	return max(l)

def poker(player_card):	
	number_cards = []
	card_suits = []
	for card in player_card:
		number_cards.append(card[0])
		card_suits.append(card[1])
	number_cards.sort()
	royal_flush = ['A', 'J', 'K', 'Q', 'T']
	royal_flush.sort()
	if number_cards == royal_flush and flush(card_suits):
		return 10000
	elif number_cards != royal_flush and straight(number_cards) and flush(card_suits):
		return 9000 + straight(number_cards)
	elif four_cards(number_cards):
		return 8000 
	elif full_house(number_cards):
		return 7000 + full_house(number_cards) 
	elif flush(card_suits):
		return 6000 + high_card(number_cards) 
	elif straight(number_cards):
		return 5000 + straight(number_cards)
	elif triple(number_cards):
		return 4000 + triple(number_cards)
	elif two_pair(number_cards):
		return 2000 + two_pair(number_cards)
	elif one_pair(number_cards):
		return 1000 + one_pair(number_cards) 
	else:
		return high_card(number_cards)	


