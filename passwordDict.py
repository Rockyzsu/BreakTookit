#-*-coding=utf-8-*-
import os
dict_folder = os.path.join(os.getcwd(),'dict')

def read_dict():
    fileNumber =  len(os.listdir(dict_folder))
    dict_list=[]
    for i in range(fileNumber):
        filename = os.path.join(dict_folder,'rkolin{}.txt'.format(i))
        print filename
        fp = open(filename,'r')
        line = '1'
        while line:
            line = fp.readline()
            dict_list.append(line.strip())
        print len(dict_list)
        dict_list= list(set(dict_list))
        print len(dict_list)

    #print len(dict_list)

def read_one():
    file='D:\\git\\BreakTookit\\dict\\rkolin_all.txt'
    line = open(file,'r').readlines()
    print len(line)
    line2= list(set(line))
    print len(line2)
#read_dict()
read_one()