def calc_sheme_2(P_i):
    P1_total = 1
    for i in range(3):
        P1_total *= P_i[i]

    P2_total = 1
    for i in range(3, 6):
        P2_total *= P_i[i]

    P3_total = 1
    for i in range(6, 10):
        P3_total *= P_i[i]

    P_paralell = 1 - (1 - P1_total) * (1 - P2_total)

    return P3_total * P_paralell


def calc_sheme_1(P_i):
    P1_total = 1
    for i in range(5):
        P1_total *= P_i[i]

    P2_total = 1
    for i in range(5, 8):
        P2_total *= P_i[i]

    P3_total = 1
    for i in range(8, 10):
        P3_total *= P_i[i]

    P_paralell = 1 - (1 - P3_total) * (1 - P2_total)

    return P1_total * P_paralell