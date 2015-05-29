import pygame,math,random

class Gun():
	def __init__(self, kind):
		self.coolDown = 0
		if kind == "pistol":
			self.kind = kind
			self.gunSpeed = 10
			self.ammo = None
			self.coolDownMax = 1
			self.life = 500
		if kind == "shot gun":
			self.kind = kind
			self.gunSpeed = 7
			self.ammo = None
			self.coolDownMax = 1
			self.life = 300
		if kind == "uzi":
			self.kind = kind
			self.gunSpeed = 15
			self.ammo = None
			self.coolDownMax = int(60*.1)
			self.life = 500
		if kind == "joker":
			self.kind = kind
			self.gunSpeed = 100
			self.ammo = None
			self.coolDownMax = 1
			self.life = 500
		if kind == "exploder":
			self.kind = kind
			self.gunSpeed = 5
			self.ammo = None
			self.coolDownMax = 5
			self.life = 40
		if kind == "laser":
			self.kind = kind
			self.gunSpeed = 15
			self.ammo = None
			self.coolDownMax = int(60*.000000000000000000000000000000000000000000000000000000000000000000000000000001)
			self.life = 500
