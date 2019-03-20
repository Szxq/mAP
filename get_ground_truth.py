#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
'''
Created on 2019年3月19日

@author: yaoyf
'''

import os

classes = ["eye","mouth","nose","chin"]

if __name__ == '__main__':
    truth = "./ground-truth"
    with open("new.txt") as lines:    # 训练集
        for line in lines:
            aaa = line.strip().split(" ")
            imagefile = os.path.split(aaa[0])[1]
            truthfile = truth + os.sep + imagefile.split(".")[0]+".txt"
            print(truthfile)
            truthfiles = open(truthfile, "w")
            for i, a in enumerate(aaa):
                if i != 0:
                    cc = classes[int(a.split(",")[-1])] + " " +" ".join([i for i in a.split(",")[0:4]])
                    truthfiles.write(cc + "\n")
            truthfiles.close()
            print("*" * 20)
