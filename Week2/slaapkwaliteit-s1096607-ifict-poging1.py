from datetime import datetime, timedelta


def wekker(slaap_uur: int, slaap_minuut: int, ontwaak_uur: int, ontwaak_minuut: int) -> str:
    """
    Geeft een slimme wekkertijd

    :param slaap_uur: uur van in slaap vallen
    :param slaap_minuut: minuut van in slaap vallen
    :param ontwaak_uur: minimaal uur van ontwaken
    :param ontwaak_minuut: minimale minuut van ontwaken

    :return: De beste tijd om wakker te worden
    """
    # Deze strings zijn makkelijk te interpeteren als datetime
    slaap_tijd_str = '01/01/2000 {}:{}'.format(slaap_uur, slaap_minuut)
    minimale_ontwaak_tijd_str = '02/01/2000 {}:{}'.format(ontwaak_uur,
                                                          ontwaak_minuut)

    # Omzetten naar datetime
    wekker_tijd = datetime.strptime(slaap_tijd_str, '%d/%m/%Y %H:%M')
    minimale_ontwaak_tijd = datetime.strptime(minimale_ontwaak_tijd_str,
                                              '%d/%m/%Y %H:%M')
    # De optimale duur van een periode slaap
    interval = timedelta(minutes=90)

    # Zolang we nog niet op willen staan
    while wekker_tijd < minimale_ontwaak_tijd:
        # Tellen we de interval op bij de wekker
        wekker_tijd += interval

    return wekker_tijd.strftime('%H:%M')


def main() -> None:
    # Slaap uur, slaap minuut
    slp_u, slp_m = input('Tijd van in slaap vallen (hh:mm):\r\n').split(":")
    # Ontwaak uur, ontwaak minuut
    ont_u, ont_m = input('Tijd om wakker worden (hh:mm):\r\n').split(":")

    print(wekker(slp_u, slp_m, ont_u, ont_m))


if __name__ == '__main__':
    main()