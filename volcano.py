def scale(n):
    if n <= 0:
        print "no volcano for you :-("
        return
    for i in xrange(3 * n):
        print "".join(["".join([" " for x in xrange(((3 * 2 * n) - (2 * i)) / 2)]),
                       "/", "".join(['A' for j in xrange(2 * i)]), "\\"])


scale(25)
