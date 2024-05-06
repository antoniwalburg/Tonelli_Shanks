# Antoni Walburg Matematyka Dyskretna Projekt Mwt 2024

# OPIS
# Projekt numer 5 (średnie)
# 1 Użytkownik podaje dwie liczby n oraz nieparzystą liczbę pierwszą p.
# 2 Program najpierw sprawdza, za pomocą kryterium Eulera, czy n jest  resztą kwadratową modulo p (https://pl.wikipedia.org/wiki/Reszta_kwadratowa_modulo).
# 3 Jeżeli jest to, za pomocą algorytmu Tonelliego-Shanksa (https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm) znajduje jej pierwiastek mod p,
# tj taką liczbę x, że x^2=n mod p.

# funkcje

def is_prime(k):
    if k <= 1:
        return False

    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False

    return True


def is_quadratic_residues(a, k):
    # ef -> euler formula
    ef = int((a ** ((k - 1) / 2)) % k)
    if ef == 1:
        return True
    elif -1 % k == ef:
        return False


# inputy i walidacje

n = int(input("Podaj liczbę naturalna n: "))
if n <= 0:
    raise ValueError("Podaj liczbę naturalną n > 0")
p = int(input("Podaj nieparzystą liczbę pierwszą p: "))
if not is_prime(p) or p % 2 == 0:
    raise ValueError("Podaj nieparzysztą liczbę pierwszą p")


# kryterium Eulera, sprawdzenie czy n jest resztą kwadratową modulo p + algorytm Tonelliego-Shanksa jeżeli spełnia kryterium Eulera

def Tonelli_Shanks_algorithm(n, p):
    if not is_quadratic_residues(n, p):
        print("n nie jest resztą kwadratową")
        return None
    else:
        print("n jest resztą kwadratową")

    # Tonelli_Shanks
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        S += 1
        Q //= 2
    print("Q=",Q)
    print("S=",S)
    # Szukanie kwadratowych niereszt p
    z = 2
    while is_quadratic_residues(z, p):
        z += 1
    print("z=", z)
    # tworznie zmiennych
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q + 1) // 2, p)

    while t != 1:
        print("Loop")
        # obliczanie i
        i = 0
        temp = t
        while temp != 1:
            i += 1
            temp = (temp * temp) % p
        print("i=", i)

        # Obliczanie b, M, c, t, R
        pow2 = 2 ** (M - i - 1)
        b = pow(c, pow2, p)
        M = i
        c = (b * b) % p
        t = (t * b * b) % p
        R = (R * b) % p
        print("b=", b)
        print("M=", M)
        print("c=", c)
        print("t=", t)
        print("R=", R)

    # szukany pierwiastek
    return R


print(Tonelli_Shanks_algorithm(n,p))
