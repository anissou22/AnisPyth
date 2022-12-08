print('Menu:')
print('1-pour ajouter un étudiant.')
print('2-pour choisir un étudiant au hazard.')
print('0- Exit.')

choix = {"1": "pour ajouter un étudiant.", "2": "pour choisir un étudiant au hazard."}
while True: 
    n = input("Veuillez insérer votre choix.") 
    if n == '0':
        break
    print(choix.get(n,'Pas possible'))

