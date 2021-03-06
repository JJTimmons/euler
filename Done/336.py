import utils
"""
A train is used to transport four carriages in the order: ABCD. However, sometimes when the train arrives to collect the carriages they are not in the correct order. 
To rearrange the carriages they are all shunted on to a large rotating turntable.
After the carriages are uncoupled at a specific point the train moves off the turntable pulling the carriages still attached with it.
The remaining carriages are rotated 180 degrees.
All of the carriages are then rejoined and this process is repeated as often as necessary in order to obtain the least number of uses of the turntable.
Some arrangements, such as ADCB, can be solved easily: the carriages are separated between A and D, and after DCB are rotated the correct order has been achieved.

However, Simple Simon, the train driver, is not known for his efficiency, so he always solves the problem by initially getting carriage A in the correct place,
then carriage B, and so on.

Using four carriages, the worst possible arrangements for Simon, which we shall call maximix arrangements,
are DACB and DBAC; each requiring him five rotations (although, using the most efficient approach, they could be solved using just three rotations).
The process he uses for DACB is shown below.

It can be verified that there are 24 maximix arrangements for six carriages, of which the tenth lexicographic maximix arrangement is DFAECB.

Find the 2011th lexicographic maximix arrangement for eleven carriages.
"""
"""
D|ACB 3021
|DBCA 3120
AC|BD 0213
A|CDB 0231
AB|DC 0132
"""
"""
DF|AECB
|DFBCEA
AEC|BFD
A|ECDFB
ABFD|CE
AB|FDEC
ABCE|DF
ABC|EFD
"""
"""
    Notes: need to make sure that, after each flip, the next number that is ordered is not last
"""

CACHE = {}


def mix_count(word, ordered):
    """
        figure out how many times n has to be "flipped" to be ordered
    """
    flips = 0
    i = 0
    while i < len(word):
        c = word[i]
        if c is not ordered[i]:
            pos = word.index(ordered[i])
            if pos == len(word) - 1:
                word = word[:i] + list(reversed(word[i:]))
                flips += 1
                for k in currFlips:
                    currFlips[k] += 1
            else:
                word = word[:pos] + list(reversed(word[pos:]))
                word = word[:i] + list(reversed(word[i:]))
                flips += 2

        i += 1

    return flips


print mix_count(["D", "A", "C", "B"], ["A", "B", "C", "D"])
assert mix_count(["D", "A", "C", "B"], ["A", "B", "C", "D"]) == 5
assert mix_count(["D", "B", "A", "C"], ["A", "B", "C", "D"]) == 5


def mixmax_count(limit=5):
    word = [chr(n) for n in range(65, 65 + limit)]
    ordered = [chr(n) for n in range(65, 65 + limit)]

    max_count = 0
    valid_words = []
    words = utils.permute(word)
    for w in words:
        count = mix_count(w, ordered)
        if count > max_count:
            max_count = count
            valid_words = [w]
        elif count == max_count:
            valid_words.append(w)
    return sorted(["".join(word) for word in valid_words])


# print mixmax_count(11)[2010]  # outputs CAGBIHEFJDK in 22 minutes...

print mixmax_count(9)[10]  # outputs CAGBIHEFJDK in 22 minutes...
