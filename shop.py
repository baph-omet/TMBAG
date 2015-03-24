import items
from actors import Player

# Verifies that the item can be bought, then purchases it if it can
# player is of type Player, item is of type Item, and amount is of type Int
def buyItem(player,item,amount):
	# If for some weird reason the cost of an item is negative, sets the cost to 0
	cost = item.buyPrice
	if cost < 0:
		cost = 0
	
	# Makes sure that the player can afford the amount of items they're trying to buy
	if player.money < cost * amount:
		if amount == 1:
			text("You can't afford the " + item.name)
		else:
			text("You can't afford to buy " + str(amount) + " " + item.name + "(s)")
	
	# If they can afford it...
	else:
		# Buy the item
		text(player.name + " bought " + str(amount) + " " + item.name)
		player.giveItem(item.name,amount=amount)
		player.money -= cost
		
	

# Verifies that the item can be sold, then sells it if it can
# Arguments are the same as in buyItem()
def sellItem(player,item,amount):
	# Makes sure that the item isn't a key item (you can't sell those)
	for e in KeyItem.__subclasses__():
		if item.name == e:
			print(item.name,"is a key item. You can't sell it.")
			break
	else:
		player.removeItem(item,amount=amount)
		
		
def shop(player,items):
	