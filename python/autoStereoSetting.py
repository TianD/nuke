#coding:utf-8
'''
Created on 2016年6月24日 上午11:23:57

@author: TianD

@E-mail: tiandao_dunjian@sina.cn

@Q    Q: 298081132

@Description:

'''
import os.path
import nuke, nukescripts

def setStereo():
      
    # set view for stereo
    nukescripts.stereo.setViewsForStereo()
    
    # split file value
    selectedNodes = nuke.selectedNodes('Read')
    if  selectedNodes:
        for node in selectedNodes:
            file_value = node['file'].getValue()
            if 'stereoCameraLeft' in file_value:
                node['file'].splitView('left')
                l_value = file_value
                r_value = l_value.replace('stereoCameraLeft', 'stereoCameraRight')
                node['file'].setValue(r_value)
            elif 'stereoCameraRight' in file_value:
                node['file'].splitView('right')
                r_value = file_value
                l_value = r_value.replace('stereoCameraRight', 'stereoCameraLeft')
                node['file'].setValue(l_value)
            else :
                pass
    else :
        raise NameError, "请先选择read节点"
    
     