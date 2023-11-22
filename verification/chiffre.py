def demander_chiffre():
    age_int = 0
    while age_int == 0 :
        age_str = input(" Quel est votre ages ? :")
        try :
            age_int = int(age_str)
        except :
            print("Erreur: veuillez entrez les nombre")
    return age_int