#coding:utf-8
'''
Created on 2015/7/16

@author: TianD
'''

#import quickwrite
#import quickwrite_LandR
import quickwrite_new
#import autoUploadFootage
import quickSubmit
import autoStereoSetting
import tempCmd
import stereoCombine

menuDic = {
    ("TenQing", "TenQingLogo.png"): [["Quick Write", "quickwrite_new.quickWrite()", "alt+w", "quickwrite.png"],\
                                     ["Quick Submit Tool", "quickSubmit.quickSubmit()", "alt+r", "quickSubmit.png"],\
                                     ["Auto Set Stereo", "autoStereoSetting.setStereo()", "alt+l", "LeyeR.png"],\
                                     ["Stereo Vertical Combination", "stereoCombine.main()", "alt+b", "StereoVerticalCombination.png"],\
                                     ["Temp", "tempCmd.tempCmd()", "", ""]]
}

toolbar = nuke.menu("Nodes")
for key, value in menuDic.iteritems():
    tdMenu = toolbar.addMenu(*key)
    for v in value:
        tdMenu.addCommand(*v)
