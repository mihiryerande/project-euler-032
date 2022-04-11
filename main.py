# Problem 32:
#     Pandigital Products
#
# Description:
#     We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
#       for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
#     The product 7254 is unusual, as the identity, 39 × 186 = 7254,
#       containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#     Find the sum of all products whose multiplicand/multiplier/product identity
#       can be written as a 1 through 9 pandigital.
#
#     HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from itertools import permutations


def main():
    """
    Returns a list of all pandigital product identities
      (as 3-tuples (m1, m2, p), where m1 × m2 = p)
      and the sum of all pandigital identity products (unique values of p) in that list.

    Returns:
        (Tuple[List[Tuple[int, int, int]], int]):
            Tuple of ...
              * List of all pandigital product identities (m1, m2, p)
              * Sum of all unique values of p
    """
    # Idea:
    #     Could probably be done more efficiently but shouldn't be terrible.
    #
    #     Check all permutations of the digits 1 through 9
    #       => 9! = 362,880 permutations
    #
    #     For each permutation `s` as a string, slice s = < m1|m2|p > into m1, m2, and p.
    #     For example, start with string '123456790' and slice into 1 × 2 = 3456789.
    #     Check if m1, m2, and p form a valid identity.
    #       => Sum(i) for i in [1,7] = 7*(7+1)/2 = 28 ways to slice `s`
    #
    #     Total number of candidates searched = 9! * 28 = 10,160,640
    #
    #     Possible improvement(s):
    #       * For some `s`, check a smaller set of slices based on the numbers of digits.
    #         For example, s = '123456789' shouldn't get sliced to 1 × 2345678 = 9
    pandigital_str = ''.join([str(i + 1) for i in range(9)])

    identities = []
    products = set()
    for s in permutations(pandigital_str):
        # Slice `s` into m1, m2, and p
        ds = ''.join(s)
        for i in range(1, 8):
            for j in range(i+1, 9):
                m1 = int(ds[:i])
                m2 = int(ds[i:j])
                p = int(ds[j:])
                if m1 < m2 and m1 * m2 == p:
                    # Constrain m1 < m2 to avoid unnecessary duplicate identities
                    identity = (m1, m2, p)
                    print(identity)
                    identities.append(identity)
                    products.add(p)
    identities.sort()
    return identities, sum(products)


if __name__ == '__main__':
    pandigital_identities, pandigital_product_sum = main()
    print('Pandigital product identities:')
    for pandigital_identity in pandigital_identities:
        print('  {:2d} × {:4d} = {:4d}'.format(*pandigital_identity))
    print('Sum of pandigital products:')
    print('  {}'.format(pandigital_product_sum))
