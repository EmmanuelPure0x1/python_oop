# using __name__ and __main__

print("this is mod_1 bane -->" + __name__)

def main():
    return "from mode1 function"
    #pass #helps to not NEED code directly when having defined a function or class

# Syntax if __name__ == "__name__":

if __name__ == "__name__": # check whether the code is run from current file
    main()