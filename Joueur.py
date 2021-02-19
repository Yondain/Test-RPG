#coding:utf-8

import time

class Player():

	def __init__(self, stat={"Atk":200 , "Def":150, "Pv":1500}):

		print("Creation du personnage...")
		time.sleep(1)
		
		self.nom = input("Entrez votre pseudo\n")
		time.sleep(1)
		
		self.race = input("Veuillez choisir une race parmis :\n\t'Humain' ; 'Orc' ; 'Elfe' ; 'Demon' ; 'Ange' ; 'Elementaire' \n")	
		
		while self.race != "Humain" and self.race != "Orc" and self.race != "Elfe" and self.race != "Elementaire" and self.race != "Ange" and self.race != "Demon" :
			try :
				assert(self.race == "Humain" or self.race == "Orc" or self.race == "Elfe" or self.race == "Elementaire" or self.race == "Ange" or self.race == "Demon")
			except AssertionError:
				print("La race choisie n'existe pas veuillez reessayer")
				self.race=input()
			except :
				print("La race choisie n'existe pas veuillez reessayer")
				self.race=input()	
	
		self.stat = stat
		
		self.classe = "Assassin" or "Mage" or "Berserk" or "Seraphin" or "Diablotin" or "Esprit"
		
		self.alreadyClassed = False

		self.exp = 0

		self.level = 1


	def gainexp(self, result_fight=None):

		if result_fight=="Win" :
			time.sleep(1)
			print("Vous gagnez ", (50*(self.level/3)), "pts d'exp")
			exp= self.exp+ (50*(self.level/3))

		elif result_fight=="You are dead":
			exp= self.exp + (5*self.level)
			time.sleep(1)
			print("Vous gagnez ", (5*self.level), "pts d'exp")

		elif result_fight== "Fuite":
			time.sleep(1)
			print("Fuite.... Vous ne gagnez pas d'exp")
			exp=self.exp
			
		self.exp= exp
		self.gainlevel(exp)


	def gainlevel(self, exp):

		self.getclass()

		exp_max=30
		exp_max = exp_max*self.level

		if exp >= exp_max :
			self.level+=1
			time.sleep(2)
			phrase=" FELICITATIONS (o^-^o) "
			print(phrase.center(100, "!"), "\n\t\t\tVous etes maintenant Level {}".format(self.level))
			
			self.stat["Atk"]=self.stat["Atk"] + (10*self.level)
			self.stat["Def"]=self.stat["Def"] + (10*self.level)
			self.stat["Pv"]=self.stat["Pv"] + (25*self.level)
			self.exp= exp - exp_max

		self.getclass()


	def getclass(self):

		if self.alreadyClassed == False : 
			if self.level == 15:
				print("Bravo, maintenant vous pouvez choisir une classe parmis:\n\t'Assassin' ; 'Mage' ; 'Berserk' ; 'Seraphin' ; 'Diablotin' ; 'Esprit'")
				classe= str(input())
				
				while classe != "Assassin" and classe != "Mage" and classe != "Berserk" and classe != "Seraphin" and classe != "Diablotin" and classe != "Esprit" :
					print("La classe choisie n'existe pas veuillez reessayer")
					classe=input()

				self.classe= classe
				self.updateStats()
				self.alreadyClassed = True


	def updateStats(self):

		if self.classe == "Assassin":
			print("Vous etes desormais de la classe ", self.classe)
			self.stat["Atk"]=self.stat["Atk"] + (400)
			self.stat["Pv"]=self.stat["Pv"] + (100)

		elif self.classe == "Mage":
			print("Vous etes desormais de la classe ", self.classe)
			self.stat["Atk"]=self.stat["Atk"] + (200)
			self.stat["Pv"]=self.stat["Pv"] + (300)

		elif self.classe == "Berserk":
			print("Vous etes desormais de la classe ", self.classe)
			self.stat["Atk"]=self.stat["Atk"] + (300)
			self.stat["Pv"]=self.stat["Pv"] + (200)

		elif self.classe == "Seraphin" or self.classe == "Diablotin":
			print("Vous etes desormais de la classe ", self.classe)
			self.stat["Atk"]=self.stat["Atk"] + (250)
			self.stat["Pv"]=self.stat["Pv"] + (250)

		elif self.classe == "Esprit":
			print("Vous etes desormais de la classe ", self.classe)
			self.stat["Atk"]=self.stat["Atk"] + (150)
			self.stat["Pv"]=self.stat["Pv"] + (350)

		print(self.stat)



def creation():
	p1=Player()
	return p1

