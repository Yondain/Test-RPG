#coding:utf-8

import time

import Joueur

import Monstre


def fight(main, adv):
	
	print("Debut du combat.....")
	time.sleep(2)

	print("Voici vos stat:", main.stat,"\tpts d'exp:", main.exp,"\n")
	time.sleep(2)

	print("Vous combattez un ", adv.name,"qui a pour stat:", adv.stat,"\n")
	pv_adv=adv.stat["Pv"]
	pv_main=main.stat["Pv"]
	def_main=main.stat["Def"]
	nb_tour=0
	time.sleep(2)
	
	while pv_main!=0 or pv_adv!=0 :
		print("Attaquer\tDefendre\tFuir\n")
		nb_tour=nb_tour+1

		rep=input()
		time.sleep(2)

		while rep!="Attaquer" and rep!="Fuir" and rep!="Defendre":
			print("Erreur de saisie, vous ne pouvez qu'Attaquer, Defendre ou Fuir (Veuillez respectez l'ecriture avec les maj)\n")
			rep=input()
		
		if rep=="Attaquer":
			print("Vous infligez {}pts de dgts et recevez {}pts de dgts\n".format(main.stat["Atk"],adv.stat["Atk"]))
			pv_main= pv_main-adv.stat["Atk"]
			pv_adv= pv_adv-main.stat["Atk"]
			if pv_main<=0 or pv_adv<=0:
				break
			print("Il vous reste ", pv_main, "Pv\n")
			print("Il reste ", pv_adv, "Pv a votre adversaire\n")


		elif rep=="Defendre":
			if def_main<=0:
				print("Vous ne pouvez defendre\nVeuillez choisir une autre option\n")
			elif def_main>0:
				print("Vous defendez et recevez {}pts de dgts.\n".format(adv.stat["Atk"]))
				def_main=def_main-adv.stat["Atk"]
				
				if def_main<0 and (def_main+pv_main)>0:
					print("Votre defense est brisee, vous perdez ", -def_main,"Pv\n")
					pv_main=def_main+pv_main
					print("Il vous reste ", pv_main, "Pv\n")
				elif def_main<0 and (def_main+pv_main)<=0:
					if nb_tour==1:
						print("L'attaque est si puissante que vous mourrez du premier coup malgre que vous vous soyez defendu vaillamment\n")
					print("Vous mourrez\n")
					pv_main=0
					break
				else:
					if def_main>0:
						print("Vous encaissez, il vous reste ", def_main, "Points de defense\n")


		elif rep=="Fuir":
			if nb_tour%2 ==1 :
				print("Fuite reussie\n")
				z="Fuite"
				main.gainexp(result_fight=z)
				break

			elif nb_tour%2 ==0 :
				print("Fuite echouee\n")
				pv_main= pv_main-adv.stat["Atk"]          
				print("Vous recevez {}pts de dgts\n".format(adv.stat["Atk"]))
				if pv_main>0:
					print("Il vous reste ", pv_main, "Pv\n")
					print("Il reste ", pv_adv, "Pv a votre adversaire\n")
				if pv_main<=0:
					print(main.nom, " est mort\n")

	if pv_main<=0 and pv_adv<=0:
		print(main.nom, "meurt vaillamment au combat en emportant son adversaire avec lui\n")
		z="Win"
		main.gainexp(result_fight=z)

	elif pv_main<=0 and pv_adv>0:
		print(main.nom, " est mort\n")
		z="You are dead"
		main.gainexp(result_fight=z)


	elif pv_main!=main.stat["Pv"] and pv_main>0 and rep !="Fuir":
		z="Win"
		main.gainexp(result_fight=z)
		
	print("Regeneration en cours\n")
	time.sleep(4)
	print("Voulez vous refaire un combat ?(Oui ou Non)")
	reponse=input()
	start_fight(reponse)


def start_fight(rep):
	while rep!="Oui" and rep !="Non":
		print("Erreur de saisie, veuillez saisir Oui ou Non")
		rep=input()

	if rep=="Oui":
		stat_adv=Monstre.randstat(joueur.level)
		adv  = Monstre.creation(stat_adv)
		fight(joueur, adv)
	elif rep=="Non":
		print("Fin du jeu.....\n(Desole il n'y a pas encore assez de fonctionnalites)\n")

ph=" Lancement du jeu "
print(ph.center(100, "~"))
time.sleep(2)

joueur = Joueur.creation() 
time.sleep(2)
joueur.getclass()

print(joueur.nom, "voulez-vous combattre ? (Oui ou Non)")
answer=input()

start_fight(answer)

