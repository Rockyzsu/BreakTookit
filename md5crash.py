# -*-coding=utf-8-*-
# crash md5 hash password

import hashlib

import os


def md5cracker(hash_string,raw_file):
    count = 1
    hash_string=hash_string.lower()
    try:
        f = open(raw_file, 'r')
        for i in f.readlines():
            if hash_string == hashlib.md5(i.strip()).hexdigest():
                print "Password is {}  !!!  Found on loop {}".format(i.strip(), count)
                return
            else:
                print "Not found on loop {}".format(count)
            count += 1
    except Exception, e:
        print e
        exit()

hash_string = raw_input('Please input hash string that you want to crack: ')
raw_file = os.path.join(os.getcwd(),'dict','rkolin_all.txt')
md5cracker(hash_string,raw_file)
