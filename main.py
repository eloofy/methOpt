import math
from config import inputs

from scheme import calc_sheme_1, calc_sheme_2


def calc_rolling_reservation(lam: float, m: int, t: int):
    p_probability = []
    for i in range(m):
        p_probability.append(
            pow(lam * t, i) / math.factorial(i)
        )

    return math.exp(-lam * t) * sum(p_probability)


def main():
    p_i = []
    for lam_i, res_i in zip(inputs["lam"], inputs["reserve"]):
        p_i.append(calc_rolling_reservation(lam_i, res_i, inputs["t"]))

    print(f"Схема 1: {calc_sheme_1(p_i)}")
    print(f"Схема 2: {calc_sheme_2(p_i)}")


if __name__ == '__main__':
    main()
