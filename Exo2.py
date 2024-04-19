if __name__ == "__main__" :

    print("Calcul du capital acquis et des ses intérêts versés lorsque les intérêts sont calculés une fois par an")
    p=int(input("entrer le placement de départ : "))
    v=int(input("Entrer le montant du versement mensuel :" ))
    t=float(input("Entrer le taux annuel en % :" ))
    a=int(input("Entrer le nombre d'années : "))
    capital_avec_interets = p
    total_interets = 0
    capital_sans_interets = p + v * 12 * a

            ###Calcul###
    for i in range(a):
        capital_avec_interets += (v * 12)
        interets = capital_avec_interets * (t/100)
        capital_avec_interets += interets
        total_interets += interets



            ##affichage##
    print(f"Le capital acquis avec intérêts est de {round(capital_avec_interets, 2)} euros au bout de {a} an(s) avec des versements mensuels de 45 euros. ")
    print(f"Les intérêts gagnés au taux annuel de {t}% sont de {round(total_interets),2} euros.")
    print(f"Sans placements avec intérêts le capital acquit serait de {capital_sans_interets} euros")

