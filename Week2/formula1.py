

def main()->None:
    locatie = input("Locatie:\r\n")
    rondetijd = float(input("Rondetijd in minuten:\r\n"))
    afstand = float(input("Afstand in km:\r\n"))

    tijds_limiet = 120
    afstands_limiet = 305

    ronde = 0
    vereden_afstand = 0.0
    vereden_tijd = 0.0

    while vereden_afstand < afstands_limiet and vereden_tijd < tijds_limiet:
        ronde += 1
        vereden_tijd = ronde * rondetijd
        vereden_afstand = ronde * afstand

    print("De grote prijs van {0} wordt verreden over {1} ronden ({2:.3f} km)."
          .format(locatie, ronde, vereden_afstand))


if __name__ == '__main__':
    main()
