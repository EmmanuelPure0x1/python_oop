# using __name__ and __main__

print("this is mod_1 name -->" + __name__)


def main():
    return "from mode1 function"


# Syntax if __name__ == "__name__":

# check whether the code is run from current file
if __name__ == "__main__":
    main()
