def alg(n):
    res = 0
    for x in range(n):
        if (x % 5 == 0 or x % 3 == 0):
            res += x
    return res

if __name__ == "__main__":
    print "Result (small set): %s" % alg(10)
    print "Result (big set): %s" % alg(1000)
