#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:27:55 2018

@author: fubao
"""



# drop rain     sidewalk        google


'''
others: 
给一个sidewalk（1m），随机落下雨滴，每一个雨滴可以打湿一个固定的长度（1cm）。
给一个getRaindrop() ，每调用一次就自动生成一个雨滴，位置范围在-0.01到1.01。

问多久可以把整个sidewalk打湿。

我觉得本质是insert interval & merge interval, 但是要考虑的地方特别多，整个写完代码量应该也不少。
我只写了主函数，一些function都没来得及写，然后跟他说了思路，时间就到了。主要是理解题目也花了不少功夫。


给一段距离（比如100），随机落下雨滴，每一个雨滴可以打湿一个固定的宽度（比如1）。雨滴有overlap的时候不会扩散，
比如[1, 2]和[1.5, 2.5]两个雨滴打湿的[1, 2.5]。求多少雨滴可以打湿整片区域。

# https://www.zhihu.com/question/40075198

'''



