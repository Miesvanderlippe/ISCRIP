

def main()->None:
    locatie = input("Locatie:\r\n")
    rondetijd = float(input("Rondetijd in minuten:\r\n"))
    afstand = float(input("Afstand in km:\r\n"))

    # Tijd in minuten, maximale race duur
    tijds_limiet = 120
    # Afstandslimiet in kilometers
    afstands_limiet = 305

    # Aantal verreden rondes
    ronde = 0
    # Afgelegde afstand
    vereden_afstand = 0.0
    # Tijd die de race duurt
    vereden_tijd = 0.0

    # Zolang de verreden afstand onder de limiet ligt
    # En de verreden tijd onder de limiet ligt
    while vereden_afstand < afstands_limiet and vereden_tijd < tijds_limiet:
        # Rijden wij rondes
        ronde += 1
        # En berekenen we daarmee de nieuwe tijd en afstand
        vereden_tijd = ronde * rondetijd
        vereden_afstand = ronde * afstand

    # En dat geven we netjes weer
    print("De grote prijs van {0} wordt verreden over {1} ronden ({2:.3f} km)."
          .format(locatie, ronde, vereden_afstand))


if __name__ == '__main__':
    main()
