import re
import sys

def main(argv):
    dict = {}
    with open("sample.txt", "r") as file:
        for line in file:
            for word in line.split():
                if (len(argv)>0 and argv[0] == '-n'):
                    if re.search("@",word) != None: print(word)
                else:
                    if re.search("\w+@[a-z\-]+\.[a-z]+\.?[a-z]+$",word) != None:
                        #print(word)
                        domain = word.split("@")
                        if domain[1] in dict:
                            dict[domain[1]] += 1
                        else: dict[domain[1]] = 1
    for key in list(dict):
        print(key + ": " + str(dict[key]))


if __name__ == "__main__":
    main(sys.argv[1:])
