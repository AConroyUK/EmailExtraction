import re
import sys

def main(argv):
    with open("sample.txt", "r") as file:
        for line in file:
            for word in line.split():
                if (len(argv)>0 and argv[0] == '-n'):
                    if re.search("\w*@\w*",word) != None: print(word)
                else:
                    if re.search("\w*@[a-z]*(.com|.net)$|\.co\.[a-z]{2}$",word) != None: print(word)

if __name__ == "__main__":
    main(sys.argv[1:])
