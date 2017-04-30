#!/bin/bash
cat /etc/shells		# /etc/shells: valid login shells/bin/sh/bin/dash/bin/bash/bin/rbash
sudo apt-get install zsh git wget
wget --no-check-certificate https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
# 配置完了需要重啓系統
# 命令自动补全
# http://mimosa-pudica.net/zsh-incremental.html
# 在 oh-my-zsh 目录的插件目录下
.oh-my-zsh/plugins/
上面的操作有几个注意点: 创建文件夹用sudo 权限.
# 创建完的 shell 文档要给赋 777 权限.
# 然后是配置 .zshrc 文件:
nano .zshrc
然后插入一句下面的 shell 脚本:
source ~/.oh-my-zsh/plugins/incr/incr*.zsh
# 注意上面的路径地址,你要改成你的 incr*.zsh 所在的目录
# 然后保存 .zshrc 配置文件,这时如果你想让它立即生效
source .zshrc
# 这样就可以了.其他 shell 窗口可以关闭重新打开及有了补全提示.
