import os, os.path
import re
import nuke
from readNodePair import readPair, gernerateLRPair   

def stereoVerticalCombineOutput(readNodes, fps=24, outDir = "e:/nuke/mov"):
    
    root = nuke.root()
    rockFormat = "2048 1716 Rock"
    nuke.addFormat(rockFormat)
    root['format'].setValue('Rock')

    mynode = nuke.nodes.StereoVerticalCombination(inputs=readNodes)

    filePath = readNodes[0]['file'].getValue()
    fileName = os.path.basename(filePath).split(".")[0]
    if not os.path.exists(outDir):
        try:
            os.makedirs(outDir)
        except Exception, e:
            raise e, "Create Folder {0} failure!!!".format(outDir)
    output = nuke.nodes.Write(file="{0}/{1}.mov".format(outDir, fileName), inputs=[mynode], file_type=7, meta_codec=22, meta_encoder=0, mov64_fps=fps)

    return output


def main():
    readNodes = nuke.allNodes('Read')

    readNodePair = readPair(readNodes)

    lrPairs = gernerateLRPair(readNodePair)
        
    for lrPair in lrPairs:
        output = stereoVerticalCombineOutput(lrPair)
        startframe = lrPair[0]['first'].getValue()
        endframe = lrPair[0]['last'].getValue()

        nuke.execute( output, int(startframe), int(endframe) )
    
    os.startfile("e:/nuke")

if __name__ == "__main__":
    main()