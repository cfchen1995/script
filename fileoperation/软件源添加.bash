sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/	# 谷歌源
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -	# 谷歌证书
sudo add-apt-repository ppa:webupd8team/sublime-text-3	# subline源
sudo add-apt-repository ppa:webupd8team/atom		# atom源
sudo add-apt-repository ppa:lyx-devel/release		# LyX源
