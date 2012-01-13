def sumsquares(n):
    return n * (n + 1) * (2*n + 1) / 6

def squaresums(n):
    return int(n * (n + 1) / 2) ** 2

if __name__ == "__main__":
    import sys
    n = len(sys.argv) > 1 and int(sys.argv[1]) or 10
    print "Result(%d): %d" % (n, abs(sumsquares(n) - squaresums(n)))
