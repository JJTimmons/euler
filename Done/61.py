# -*- coding: utf-8 -*-

"""
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal)
numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	    P4,n=n*n	 	    1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

1. The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
2. Each polygonal type: triangle (P3,P3v127=8128), square (P4,P4v91=8281), and pentagonal (P5,P5v44=2882), is represented by a different number in the set.
3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""

def cyclical_figurate_numbers(target_count=3):
    """
        1. build all arrays up to 4-digits
        2. for each list (6x)
            2.1 add to list of sets wherever the last 2 digits are the first 2 digits of number being tested
            2.2 create a new list of sets that have been added to
    """

    def create_figurate(func):
        """
        params:
            func -- function to apply to index to get number
        """
        index = 1
        curr_digit = func(index)
        while curr_digit < 10000:
            if curr_digit > 999:
                yield curr_digit
            index += 1
            curr_digit = func(index)

    # 1.
    figs = [
        list(create_figurate(lambda n: n * (n + 1) / 2)),
        list(create_figurate(lambda n: n * n)),
        list(create_figurate(lambda n: n * (3 * n - 1) / 2)),
        list(create_figurate(lambda n: n * (2 * n - 1))),
        list(create_figurate(lambda n: n * (5 * n - 3) / 2)),
        list(create_figurate(lambda n: n * (3 * n - 2))),
    ][:target_count]
    # store once the type of fig it came from, and split into first and second half
    all_figs = [
        (i + 3, int(str(f)[:2]), int(str(f)[2:]))
        for (i, fs) in enumerate(figs)
        for f in fs
        if int(str(f)[2:]) != 0
    ]

    # 2.
    # for storing last two digits added to a linked list of tuples
    # tuple is (fig_type, first two digits, last two digits)
    # stored by last two digits in cache for easy lookup with first two of next
    cache = {n: [] for n in range(1, 100)}
    for (type, f_half, s_half) in all_figs:
        cache[s_half].append([(type, f_half, s_half)])  # store by second half

    for count in range(1, target_count + 1):
        # add back onto the list
        for (type, f_half, s_half) in all_figs:
            # match second half to first half
            for possible_match in cache[f_half]:
                if not any([f[0] == type for f in possible_match]):
                    # create a new list if it's a new type
                    cache[s_half].append(possible_match + [(type, f_half, s_half)])

        # remove all those that aren't the length of current index
        for s_half in cache.keys():
            cache[s_half] = [fs for fs in cache[s_half] if len(fs) == count]
    
    # keep only those that loop back around
    answer = None
    for s_half in cache.keys():
        for fig_set in cache[s_half]:
            if fig_set[-1][2] == fig_set[0][1]:
                answer = fig_set # okay to overwrite, will be the same
    digits = [a[1] * 100 + a[2] for a in answer]
    print digits, sum(digits)
    return sum(digits)



# cyclical_figurate_numbers() # 0.045 seconds
cyclical_figurate_numbers(6) # 28684 in 0.089 seconds