def decimal_to_base_k(n, k):
    """Converts a given decimal (i.e. base-10 integer) to a list containing the
    base-k equivalant.
    For example, for n=34 and k=3 this function should return [1, 0, 2, 1]."""

    base_k = []
    while n != 0:
        base_k.append(int(n % k))
        n //= k

    base_k.reverse()
    return base_k
