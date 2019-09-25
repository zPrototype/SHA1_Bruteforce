#!/usr/bin/python3
import sys
import hashlib
import time

ts = time.time()

if len(sys.argv) != 3:
    print("Usage:")
    print("./sha1_cracker.py [HASHFILE] [WORDLIST] \n")
    sys.exit

hashes = set()
with open(sys.argv[1], "r") as hashfile:
    for line in hashfile:
        hashes.add(line.strip())

print("Start cracking...")
with open(sys.argv[2], "r") as wordlist:
    for password in wordlist:
        password = password.strip('\n')
        sha1_hash = hashlib.sha1(password.encode()).hexdigest()
        if sha1_hash in hashes:
            print("Found matching hash: " + sha1_hash)
            print("Password is: " + password)

td = time.time() - ts
print("Done in " + str(td) + " sec.")
