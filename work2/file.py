#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

#定义函数
def modifyFiles(_oldStr, _newStr, *_files):
    for f in _files:
        count = 0;
        #处理文件
        fo = open(f, 'r', encoding='utf-8')
        fo_new = open('newFile', 'w', encoding='utf-8')
        for line in fo:
            if(_oldStr in line):
                count += line.count(_oldStr)
                new_line = line.replace(_oldStr, _newStr)
            else:
                new_line = line
            #写入新文件
            fo_new.write(new_line)
        fo.close()
        fo_new.close()

        os.replace(fo_new.name, fo.name)  #更换名字，覆盖原文件
        print('文件%s替换了%s处'% (fo.name, count))

modifyFiles(sys.argv[1], sys.argv[2], sys.argv[3])