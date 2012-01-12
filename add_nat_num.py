import operator
import inspect

def setunion(max):
    return sum(list(set([i for i in range(3,max,3)]).union(set([j for j in range(5,max,5)]))))

def reduced(max):
    val = reduce(lambda x,y: x+y, filter(lambda x: x % 3 == 0 or x % 5 == 0, range(max)))
    return val

def comprehend(max):
    return sum([x for x in range(max) if x%3 == 0 or x%5 == 0])

def rang(max):
    return sum(range(0,max,3)) + sum(range(0,max,5)) - sum(range(0,max,15))

# implementation of summation formula (currently fastest impl!
def _series(max, multiple):
    return (((int((max-1)/multiple)) * (int((max-1)/multiple)+1)) / 2) * multiple

def series(max):
    return _series(max, 3) + _series(max, 5) - _series(max, 15)

def short(max):
    res = 0
    fivemaxhit = False
    threemaxhit = False
    nums = {}
    for x in range(max):
        if fivemaxhit and threemaxhit: break
        if not fivemaxhit:
            fiver = x * 5
            if fiver < max:
                if not fiver in nums:
                    res += fiver
                    nums[fiver] = 1
            else:
                fivemaxhit = True
        if not threemaxhit:
            threer = x * 3
            if threer < max:
                if not threer in nums:
                    res += threer
                    nums[threer] = 1
            else:
                threemaxhit = True
    return res

# this can be written concisely as:
#    reduce(add,[x for x in range(max) if x % 3 == 0 or x % 5 == 0])
# or:
#    sum([int(n) for n in range(max) if n%3 == 0 or x%5 == 0])
def obvious(max):
    res = 0
    for x in range(max):
        if (x % 5 == 0 or x % 3 == 0): res += x
    return res

def _charles(max,d):
    res = 0
#    i=0
#    while i < max:
#        res += i
#        i += d
    for i in range(0,max,d):
        res += i
    return res
def charles(max):
    res = 0
    res += _charles(max,3)
    res += _charles(max,5)
    res -= _charles(max,15)
    return res

def sumquick(max):
    return sum([int(n) for n in range(max) if n%3 == 0 or n%5 == 0])

def reduceadd(max):
    return reduce(operator.add,[x for x in range(max) if x % 3 == 0 or x % 5 == 0])

def _runtimed(alg, *set):
    from time import clock, time
    algname = alg.__name__
    times = []
    vals = []
    for n in set:
        start = clock()
        res = alg(n)
        elapsed = (clock() - start)
        vals.append(res)
        times.append(elapsed)
        print "Result (%s(%d)): %s" % (algname, n, res)
    return times

if __name__ == "__main__":
    loc = locals()
    names = filter(lambda x: not '_' in x and inspect.isfunction(loc[x]), loc)
    times = [ _runtimed(loc[name], 1000)[0] for name in names]
    time_name = dict(zip([hash(x) for x in times],names))

    for t in sorted(times):
        print "%s ran in %.7f" % (time_name[hash(t)], t)

#    fastest = sorted(times.values())

    
