def exponentionRapide(c1, s, mod):
    if (s == 1):
        return c1
    else:
        res = pow(c1, 2, mod)
        if (s % 2 == 0):
            return exponentionRapide(res, s // 2, mod)
        else:
            return (c1 * exponentionRapide(res, s // 2, mod)) % mod


if __name__ == "__main__":
    pass