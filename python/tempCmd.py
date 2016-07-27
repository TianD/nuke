#coding:utf-8
'''
Created on 2016年6月27日 下午3:12:52

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description:

'''

import os, os.path

import nuke

def tempCmd():
    reads = nuke.allNodes('Read')
    no = []
    for read in reads:
        file = read['file'].getValue()
        dir = os.path.dirname(file)
        filename = os.path.basename(file)
        dir_last = os.path.basename(dir)
        dir_prefix = os.path.dirname(dir)
        newpath = os.path.join(dir_prefix, 'stereoCameraLeft', 'c001', dir_last)
        if os.path.exists(newpath):
            newfile = os.path.normpath(os.path.join(newpath, filename)).replace('\\','/')
            read['file'].setValue(newfile)
        else :
            no.append(read.name())
    if no:
        raise WindowsError, "{0} are not changed!!!".format(','.join(no))
        