# 比赛数据将图片里的人脸分成4种目标
# mask是正确佩戴口罩1，head是没有佩戴口罩2，back是人脸模糊不能判断3，mid_mask是戴口罩戴错了4
# 现在有的mask数据集是xml标准一样，但是face_mask是戴口罩1，face是没戴口罩2
# -*- coding:utf-8 -*-

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import os
import xml.etree.ElementTree as ET

MASK_ROOT = '../drive/My Drive/face_dectect'


def get_data():
    dir_datanames = os.listdir(MASK_ROOT)
    fw = open('mask_train.txt', 'w')
    fw1 = open('mask_val.txt', 'w')
    index = 0
    for dataname in dir_datanames:
        prefix, suffix = os.path.splitext(dataname)
        if suffix == '.xml':
            img_dir = os.path.join(MASK_ROOT, dataname)
            tree = ET.parse(img_dir)
            root = tree.getroot()
            node = root.find('filename')
            line = os.path.join(MASK_ROOT, node.text)
            line += '|'
            node = root.findall('object')
            for n in node:
                x1 = n.find('bndbox').find('xmin')
                y1 = n.find('bndbox').find('ymin')
                x2 = n.find('bndbox').find('xmax')
                y2 = n.find('bndbox').find('ymax')
                label = n.find('name')
                line += x1.text + ',' + y1.text + ',' + x2.text + ',' + y2.text + ','
                if label.text == 'face_mask':
                    line += '1'
                else:
                    if label.text == 'face':
                        line += '2'
                if n != node[-1]:
                    line += ','
            if index <= 5092:
                fw.write(line+'\n')
            else:
                fw1.write(line+'\n')
            index += 1



if __name__ == '__main__':
    get_data()
