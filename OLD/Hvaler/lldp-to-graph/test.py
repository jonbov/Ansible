#!/usr/bin/python

import sys

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print arg
    print ("%s \n" % sys.argv[1])
    print ("%s \n" % sys.argv[2])

if __name__ == "__main__":
    main()

