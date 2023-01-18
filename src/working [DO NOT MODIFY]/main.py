import argparse
import sys
import math

class NUM:
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = float('inf')
        self.hi = float('-inf') # Replaced sys.maxsize

    def add(self, n):
        # print("Inside Add", n)
        if n != "?": # Why Question mark
            self.n += 1
            d = n - self.mu
            self.mu += d / self.n
            self.m2 += d * (n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)
        # print(self.n, d, self.mu, self.m2, self.lo, self.hi)

    def mid(self):
        return self.mu

    def div(self): # Removed x
        return (self.m2 < 0 or self.n < 2) and 0 or (self.m2 / (self.n - 1)) ** 0.5





class SYM:
    def __init__(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)  # Return to later for dictionary
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x

    def mid(self):
        return self.mode

    def div(self): # Removed all parameters
        def fun(p):
            return p * math.log(p, 2)
        
        e = 0
        for _, value in self.has.items():
            e += fun(value/self.n)
        return -e


###################################################

the, help = {},"""
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
"""


egs = {}
def eg(key, string, fun):
    global egs
    global help
    egs[key] = fun
    help += f"  -g {key}    {string}"

def shout():
    # First Test Case
    # print("Welcome !!")
    pass


#####################################

args = None
Seed = 937162211

#############################

def rand(low, high):
    global Seed
    low, high = low or 0, high or 1
    Seed = (16807 * Seed) % 2147483647
    return low + (high - low) * Seed / 2147483647


def main(the, funs):
    global args
    # print(funs)
    fails = 0
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-d", "--dump", type=bool, default=False, required=False, help="on crash, dump stack")
    parser.add_argument("-g", "--go", type=str, default="data", required=False, help="start-up action")
    parser.add_argument("-h", "--help", type=bool, default=False, required=False, help="show help")
    parser.add_argument("-s", "--seed", type=int, default=937162211, required=False, help="random number seed")
    args = parser.parse_args()
    if (args.help): print(help)
    else:
        for what, fun in funs.items():
            if args.go == "all" or what == args.go:
                Seed = args.seed
                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:",what)
                else: print("✅ pass:",what)

def randFunc():
    global args
    global Seed
    num1, num2 = NUM(), NUM()
    # Why two Seeds ????
    Seed = args.seed
    # print(Seed)
    for i in range(10**3): # 10 ^ 3 : FAILLL, 10 ^ 5: PASSS
        num1.add(rand(0, 1))
    Seed = args.seed
    # print(Seed)
    for i in range(10**3):
        num2.add(rand(0, 1))
    m1, m2 = round(num1.mid(), 10), round(num2.mid(), 10)
    # print(m1, m2, 0.5, round(m1, 1))
    return m1 == m2 and 0.5 == round(m1, 1)

def symFunc():
    sym = SYM()
    for i in ["a","a","a","a","b","b","c"]:
        sym.add(i)
    return "a" == sym.mid() and 1.379 == round(sym.div(), ndigits=3)

def numFunc():
    num = NUM()
    for element in [1,1,1,1,2,2,3]:
        # print("Inside for loop")
        num.add(element)
    # print(11/7, num.mid(), 0.787, round(num.div(), ndigits=3))
    return 11/7 == num.mid() and 0.787 == round(num.div(), ndigits=3)


eg("the", "sdfsdf", shout)
eg("rand","generate, reset, regenerate same", randFunc)
eg("sym","check syms", symFunc)
eg("num", "check nums", numFunc)


main(the, egs)
