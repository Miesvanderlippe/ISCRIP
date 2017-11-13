

def main()->None:
    munt_waardes = [1, 2, 5, 10, 20, 50, 100, 200]
    aant_munt = 0
    totaal = 0.0

    for waarde in munt_waardes:
        inp = int(input("Aantal munten met waarde {0}ct\r\n".format(waarde)))
        aant_munt += inp
        totaal += (waarde * inp) / 100

    print("Aantal munten: {0}\r\nTotale waarde: {1}".format(aant_munt, totaal))


if __name__ == '__main__':
    main()
