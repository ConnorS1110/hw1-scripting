import testfile as test
from testfile import getCliArgs, printCLIvalues

def main(funs):
    """
    Function:
        main
    Description:
        Main function that tests to see if examples pass. If help command is used, the help string is printed and tests are not run
    Input:
        funs - Dictionary of callback functions
    Output:
        0 - Tests passed
        1 - 1 or more tests failed
    """
    fails = 0
    getCliArgs()
    if (test.args.help):
        print(test.help)
    else:
        for what, _ in funs.items():
            if test.args.go == "all" or what == test.args.go:
                if funs[what]() == False:
                    fails += 1
                    print("❌ fail:",what)
                else: print("✅ pass:",what)
    printCLIvalues()
    if (fails == 0): return 0
    else: return 1


if __name__ == "__main__":
    main(test.egs)
