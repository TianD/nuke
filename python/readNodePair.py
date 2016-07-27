import re
import nuke
from duplicateNode import duplicateNode

def getAnotherSource(source):
    new_source = source.replace("stereoCameraLeft","stereoCameraRight")
    if new_source == source:
        new_source = source.replace("stereoCameraRight","stereoCameraLeft")
    return new_source

def readPair(readNodes):
    readPair = {}

    for readNode in readNodes:
        filePath = readNode['file'].getValue()
        regex_str = re.sub('(stereoCameraLeft|stereoCameraRight)', 'stereoCamera(Left|Right)', filePath)
        if 'stereoCamera(Left|Right)' in regex_str:
            readPair.setdefault(regex_str, list()).append(readNode)

    return readPair

def gernerateLRPair(readPair):
    lrPairs = []
    for key, value in readPair.items():
        if len(value) == 1:
            filePath = value[0]['file'].getValue()
            another_filePath = getAnotherSource(filePath)
            another_node = duplicateNode(value[0])
            another_node['file'].setValue(another_filePath)
            if "stereoCameraLeft" in filePath:
                lrPair = [value[0], another_node]
            else :
                lrPair = [another_node, value[0]]
        else :
            if "stereoCameraLeft" in value[0]['file'].getValue():
                lrPair = value
            else :
                lrPair = value[::-1]
        lrPairs.append(lrPair)
    
    return lrPairs