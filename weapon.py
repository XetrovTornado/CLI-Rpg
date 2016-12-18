import random as r
class Weapon():
	def __init__(self, player, name, dmg, mana=0, effects=[]):
		self.name = name
		self.damage = dmg
		self.mana_cost = mana
		self.effects = effects
		self.buff = dmg <= 0
		self.player = player
	
	def special(self, player):
		pass
	
	def attack(self, player):
		if self.player.mana >= self.mana_cost:
			player.HP -= self.damage * self.player.multiplier + r.randint(-5, 5)
			self.player.mana -= self.mana_cost
		else:
			print("Need %d mana to use %s" % (self.mana_cost, self.name))
		for effect in self.effects:
			if not effect in player.effects:
				player.effects.append(effect)
		self.special(player)

class Sword(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Sword", dmg=25)

class Fireball(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Fireball", dmg=50, mana=40, effects=["burning"])

class Heal(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Heal", dmg=-30, mana=30)

class RegenMana(Weapon):
	def __init__(self, player):
		Weapon.__init__(self, player, "Mana", dmg=0)
	
	def special(self, player):
		player.mana += 50