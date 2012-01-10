def alg(max):
    res = 0
    iterations = 0
    fivemaxhit = False
    threemaxhit = False

    
    for x in range(max):
        if fivemaxhit and threemaxhit: break

        if not fivemaxhit:
            fiver = x * 5
            if fiver < max: 
                res += fiver
            else:
                fivemaxhit = True
        if not threemaxhit:
            threer = x * 3
            if threer < max: 
                res += threer
            else:
                threemaxhit = True
        iterations += 1
    return (res, iterations)

if __name__ == "__main__":
    print "Result (small set): %s, iterations: %d" % alg(10)
    print "Result (big set): %s, iterations: %d" % alg(1000)
