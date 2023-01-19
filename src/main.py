import test
from test import getCliArgs, printCLIvalues

the = {}

# args = None
# Seed = 937162211

def main(the, funs):
    getCliArgs()
    if (test.args.help):
        print(help)
    else:
        for what, fun in funs.items():
            if test.args.go == "all" or what == test.args.go:
                Seed = test.args.seed
                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:",what)
                else: print("✅ pass:",what)
    printCLIvalues()


main(the, test.egs)
