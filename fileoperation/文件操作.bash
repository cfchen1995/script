#!/bin/bash
# 添加文件/文件夹
touch filename			# 添加文件 
      e.g. touch aa.md		# 添加文件名为aa的markdown文件
      e.g. touch aa.txt		# 添加文件名为aa的文本文件
mkdir folderName 		# 添加文件夹
      e.g. mkdir aa  		# 添加名为aa的文件夹

# 重命名|移动 文件/文件夹
mv oldname newname		# 重命名文件/文件夹
   e.g. mv a b			# 将a的名称更改为b
mv FilePath newPath		# 移动文件,注意，如果不是当前目录下的子目录，要写绝对路径
   e.g. mv aa.txt /usr/local/	# 将当前目录下的aa.txt移动到/usr/local/下面.
# 这里同理可以联想下cp的复制指令
cp FilePath newPath #复制文件,注意，如果不是当前目录下的子目录，要写绝对路径

# 复制一个文件的内容到另一个文件
cat file1 > file2	# 将file1里的内容复制到file2里面，并覆盖file2里的内容
cat file1 >> file2	# 将file1里的内容追加到file2的结尾，不覆盖file2里的内容
cat file1 file2 >file	# 依次将file1 file2 的内容添加到file3中
cat file1		# 查看file1的完整内容

# 清空某个文件
cat /dev/null > file1	# 将file1的内容清空，大小为0，但是不删除,原文件被放到回收站
rm  file1		# 删除file1

# 删除文件夹
rmdir  --ignore-fail-on-non-empty folderName 
        # 删除文件夹以及子文件夹和子文件.¬
        # --ignore-fail-on-non-empty是指忽略文件是否为空，已经执行删除
# 本人不喜欢这种删除方式，想删除非空文件夹也可以使用下面的方法
rm -rf folderName #删除文件夹以及子文件夹和子文件.
                 # -r 为递归指令，Linux跟Unix 的系统之间有些会区分大小写.
                 # -f 为强制执行指令，使用需谨慎，有时候需要加上这个指令才能rm成功.
                 # -rf 如果单独使用-r,需要对每一个文件确认后才能删除,所以推荐-rf
#rm 也可以用来删除文件
rm -r fileName	# 删除文件.


# 文件最好来说不要挂载/media的根目录下面，最好新建文件夹挂载。
# 可以尝试使用df命令查看所挂载的磁盘，直接从硬件命令上umount磁盘。

# Sublime Text 3 (推荐)
# 来源：http://ptbsare.org/2014/05/12/ubuntu%E4%B8%8B%E9%83%A8%E7%BD%B2latex%E7%BC%96%E8%AF%91%E7%8E%AF%E5%A2%83/
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install sublime-text-installer





