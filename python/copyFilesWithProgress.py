#coding:utf-8
'''
Created on 2015/7/18

@author: TianD

description: shutil.copytree module doesn't support progress updates, so I'll have to write our own copying function.
'''

import os,os.path
import shutil
import threading

import sys
 
class ProgressBar(object):
    def __init__(self, message, width=20, progressSymbol=u'.', emptySymbol=u'.'):
        self.width = width
 
        if self.width < 0:
            self.width = 0
 
        self.message = message
        self.progressSymbol = progressSymbol
        self.emptySymbol = emptySymbol
        
    def update(self, progress):
        totalBlocks = self.width
        filledBlocks = int(round(progress / (100 / float(totalBlocks)) ))
        emptyBlocks = totalBlocks - filledBlocks
 
        progressBar = self.progressSymbol * filledBlocks + \
                      self.emptySymbol * emptyBlocks
 
        if not self.message:
            self.message = u''
 
        progressMessage = u'\r{0} {1}  {2}%'.format(self.message,
                                                    progressBar,
                                                    progress)
 
        sys.stdout.write(progressMessage)
        sys.stdout.flush()
 
 
    def calculateAndUpdate(self, done, total):
        progress = int(round( (done / float(total)) * 100) )
        self.update(progress)



p = ProgressBar('Copying files...')

#First, define a function to count all of the files
def countFiles(directory):
    files = []
 
    if os.path.isdir(directory):
        for path, dirs, filenames in os.walk(directory):
            files.extend(filenames)
 
    return len(files)



#Second, define a function to make directories that don't exist yet. This will allow us to create the directory structure of the source directory.
def makedirs(dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
        
#Third, define copy function
def copyFilesWithProgress(src, dst):
    numFiles = countFiles(src)
 
    if numFiles > 0:
        makedirs(dst)
 
        numCopied = 0
 
        for path, dirs, filenames in os.walk(src):
            for directory in dirs:
                dstDir = path.replace(src,dst)
                makedirs(os.path.join(dstDir, directory))
            
            for sfile in filenames:
                srcFile = os.path.join(path, sfile)
 
                dstFile = os.path.join(path.replace(src, dst), sfile)
                
                shutil.copy(srcFile, dstFile)
                
                numCopied += 1
                
                p.calculateAndUpdate(numCopied, numFiles)
        print "ok"
        
if __name__ == "__main__":
    copyFilesWithProgress("E:/Scripts", "D:/Scripts")