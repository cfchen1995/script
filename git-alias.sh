# Git别名(oh-my-zsh)
# 通过网络及相关资源整理收集

alias g='git'
alias ga='git add'                   # 添加至暂存区
alias gaa='git add --all'            # 添加所有至暂存区
alias gapa='git add --patch'         # 添加修改并对比
alias gb='git branch'                # 列出本地已经存在的分支，并且在当前分支的前面加“*”号标记
alias gba='git branch -a'            # 列出本地分支和远程分支
alias gbr='git branch --remote'      # 列出远程分支
alias gbnm='git branch --no-merged'  # 显示没有合并到当前分支的

# 删除本地所有分支
alias gbda='git branch --merged | command grep -vE "^(\*|\s*master\s*$)" | command xargs -n 1 git branch -d'
alias gbl='git blame -b -w'   # 查看某个文件具体修改的作者时间等
alias gbs='git bisect'
alias gbsb='git bisect bad'
alias gbsg='git bisect good'
alias gbsr='git bisect reset'
alias gbss='git bisect start'
alias gc='git commit -v'                                   # 当你用－v参数的时候可以看commit的差异
alias gcam='git commit -a -m'                              # 提交修改和新增的文件到缓存区
alias gc!='git commit -v --amend'                          # commit --amend可以修改最后一次commit信息
alias gca='git commit -v -a'                               # 一般提交命令
alias gcn!='git commit -v --no-edit --amend'
alias gca!='git commit -v -a --amend'
alias gcan!='git commit -v -a --no-edit --amend'
alias gcans!='git commit -v -a -s --no-edit --amend'
alias gcb='git checkout -b'                               # 新建一个分支并切换到新建分支
alias gcf='git config --list'                             # 查看所有用户
alias gcl='git clone --recursive'                         # 克隆项目                 
alias gclean='git clean -fd'                              # 删除一些没有Git add的文件
alias gpristine='git reset --hard && git clean -dfx'      # 回滚上一版本并且删除没有git add的文件
alias gcm='git checkout master'                           # 切换 master 主干分支
alias gcmsg='git commit -m'                               # 提交修改
alias gco='git checkout'                                  # 切换分支
alias gcount='git shortlog -sn'
compdef gcount=git
alias gcp='git cherry-pick'                               # <commit id>:单独合并一个提交
alias gcs='git commit -S'
alias gd='git diff'                                       # 比较文件间的差异
alias gdca='git diff --cached'                            # 比较两个commit之间的区别
alias gdct='git describe --tags `git rev-list --tags --max-count=1`'
alias gdt='git diff-tree --no-commit-id --name-only -r'
gdv() { git diff -w "$@" | view - }
compdef _git gdv=git-diff
alias gdw='git diff --word-diff'
alias gf='git fetch'
alias gfa='git fetch --all --prune'
function gfg() { git ls-files | grep $@ }
compdef gfg=grep
alias gfo='git fetch origin'
alias gl='git pull'
alias glg='git log --stat'
alias glgp='git log --stat -p'
alias glgg='git log --graph'
alias glgga='git log --graph --decorate --all'
alias glgm='git log --graph --max-count=10'
alias glo='git log --oneline --decorate'
alias glol="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
alias glola="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --all"
alias glog='git log --oneline --decorate --graph'
alias gloga='git log --oneline --decorate --graph --all'
alias glp="_git_log_prettily"
compdef _git glp=git-log
alias gm='git merge'
alias gmom='git merge origin/master'
alias gmt='git mergetool --no-prompt'
alias gmtvim='git mergetool --no-prompt --tool=vimdiff'
alias gmum='git merge upstream/master'

alias gp='git push'
alias gpd='git push --dry-run'
alias gpoat='git push origin --all && git push origin --tags'
compdef _git gpoat=git-push
alias gpu='git push upstream'
alias gpv='git push -v'

alias gr='git remote'
alias gra='git remote add'
alias grb='git rebase'
alias grba='git rebase --abort'
alias grbc='git rebase --continue'
alias grbi='git rebase -i'
alias grbm='git rebase master'
alias grbs='git rebase --skip'
alias grh='git reset HEAD'
alias grhh='git reset HEAD --hard'
alias grmv='git remote rename'
alias grrm='git remote remove'
alias grset='git remote set-url'
alias grt='cd $(git rev-parse --show-toplevel || echo ".")'
alias gru='git reset --'
alias grup='git remote update'
alias grv='git remote -v'
alias gsb='git status -sb'
alias gsd='git svn dcommit'
alias gsi='git submodule init'
alias gsps='git show --pretty=short --show-signature'
alias gsr='git svn rebase'
alias gss='git status -s'
alias gst='git status'
alias gsta='git stash save'
alias gstaa='git stash apply'
alias gstd='git stash drop'
alias gstl='git stash list'
alias gstp='git stash pop'
alias gsts='git stash show --text'
alias gsu='git submodule update'
alias gts='git tag -s'
alias gtv='git tag | sort -V'

alias gunignore='git update-index --no-assume-unchanged'
alias gunwip='git log -n 1 | grep -q -c "\-\-wip\-\-" && git reset HEAD~1'
alias gup='git pull --rebase'
alias gupv='git pull --rebase -v'
alias glum='git pull upstream master'

alias gwch='git whatchanged -p --abbrev-commit --pretty=medium'
alias gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit -m "--wip--"'
alias gg='git gui citool'
alias gga='git gui citool --amend'
ggf() {
	[[ "$#" != 1 ]] && local b="$(git_current_branch)"
	git push --force origin "${b:=$1}"
}
compdef _git ggf=git-checkout
ggl() {
	if [[ "$#" != 0 ]] && [[ "$#" != 1 ]]; then
		git pull origin "${*}"
	else
		[[ "$#" == 0 ]] && local b="$(git_current_branch)"
		git pull origin "${b:=$1}"
	fi
}
compdef _git ggl=git-checkout
alias ggpull='git pull origin $(git_current_branch)'
compdef _git ggpull=git-checkout
ggp() {
	if [[ "$#" != 0 ]] && [[ "$#" != 1 ]]; then
		git push origin "${*}"
	else
		[[ "$#" == 0 ]] && local b="$(git_current_branch)"
		git push origin "${b:=$1}"
	fi
}
compdef _git ggp=git-checkout
alias ggpush='git push origin $(git_current_branch)'
compdef _git ggpush=git-checkout
ggpnp() {
	if [[ "$#" == 0 ]]; then
		ggl && ggp
	else
	ggl "${*}" && ggp "${*}"
fi
}
compdef _git ggpnp=git-checkout
alias ggsup='git branch --set-upstream-to=origin/$(git_current_branch)'
ggu() {
	[[ "$#" != 1 ]] && local b="$(git_current_branch)"
	git pull --rebase origin "${b:=$1}"
}
compdef _git ggu=git-checkout
alias ggpur='ggu'
compdef _git ggpur=git-checkout
alias gignore='git update-index --assume-unchanged'
alias gignored='git ls-files -v | grep "^[[:lower:]]"'
alias git-svn-dcommit-push='git svn dcommit && git push github master:svntrunk'
compdef git-svn-dcommit-push=git

alias gk='\gitk --all --branches'
compdef _git gk='gitk'
alias gke='\gitk --all $(git log -g --pretty=format:%h)'
compdef _git gke='gitk'

