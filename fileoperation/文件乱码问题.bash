#!/bin/bash

# linux主机的默认中文字符集是UTF-8而windows系统一般是GB2312或GB18030这样就会出问题，解决办法是把xManager、putty等工具的字符改为UTF-8
echo $LANG $LANGUAGE		# 查看Linux系统的字符编码格式
# 针对具体的会话项目，修改终端下的字符格式
# 确保两个系统的中文字符的编码格式一致

# 对于文本文件，Windows下的编码格式默认为ANSI，因此在保存时需要另存为UTF-8，保证在Linux下可以正常打开。

