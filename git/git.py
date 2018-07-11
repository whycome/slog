git生成公钥私钥
ssh-keygen -t rsa -C "wanhuiying@thunder.com.cn" 

----------------------git回退---------------------------
git log : 查看提交信息
'''
 git log
commit 41675e6eab6e13d94da45e4160d91de847932623 (HEAD -> master)
Author: wanhuiying <wanhuiying@thunder.com.cn>
Date:   Thu Nov 23 13:07:05 2017 +0800

    udpate from why

commit 412e8fb293ea097a19151f7e17276f761037afa5 (origin/master, origin/HEAD)
Author: wanhuiying <wanhuiying@thunder.com.cn>
Date:   Mon Nov 20 15:39:47 2017 +0800

    udpate from why

commit 1b8b3e647e9840a569907be680651721da59f35e
Author: wanhuiying <wanhuiying@thunder.com.cn>
Date:   Fri Nov 17 16:57:40 2017 +0800

    udpate from why

'''
git reset --hard  412e8fb293ea097a   # 回退
git diff : 查看
git reset --soft 91e14856200  # commit 之后回退commit
________________________________________________________________
# branch wanhuiying
git checkout master
git pull origin  master
git merge wanhuiying
git status
git push origin master
----------------------------git冲突-----------------------------
git冲突:
Your local changes to 'handler/wawa_supervise.py' would be overwritten by merge.  Aborting.
<解决>： 
git stash // 将工作区恢复到上次提交的内容
git pull 
git stash pop  // 从Git栈中读取最近一次保存的内容，恢复工作区的相关内容

'-----------补充'
git stash list  // 显示Git栈内的所有备份，可以利用这个列表来决定从那个地方恢复
git stash clear: 清空Git栈。

----------------------git错误-----------------------------
git 错误 fatal: Not a valid object name: 'master'.

问题： 新建git 项目或者刚为已存在的项目创建了git仓库， 创建分支
原因： 刚建立的git仓库默认的mastqer分支要在第一次commit之后才会真正的建立
<解决>： 
	git add .  // 添加所有项目文件到本地仓库缓存，
	git commit -m 'init commit'  // 提交到本地仓库
	git branch wanhuiying  // 可以创建分支  
	git push origin wanhuiying:wanhuiying  // 本地分支发送到远程, 冒号前为本地分支， 后为线上

-----------------------git分支----------------------------------------
git branch 分支名  // 分支创建
git branch     // 查看本地分支
git branch -r  // 查看所有远程分支
git fetch      // 从远程获取其他用户push上来的新分支
git remote -v  // 即可查看远程所有的版本信息
git checkout -b dev  // 切换到远程中的一个分支
git branch --set-upstream-to=origin/分支名  // 建立本地到远端的连接
git branch --set-upstream-to origin/wanhuiying wanhuiying
-------------------------------------------------------------
git merge --abort  // 撤销上一次的合并分支
git fetch // 刷新刚提交的git分支
git branch -d wanhuiying  // 删除分支
git branch -r -D origin/wanhuiying  // 删除本地远程分支
git push origin -d wanhuiying  // 远程删除git 服务器上的分支
--------------------------------------------------------------
'gitlab: 建立分支 '
gitlab创建分支： Repository -> + -> New branch,
然后本地分支与远程分支建立连接
通过命令： git branch --set-upstream-to=origin/分支名 

#	查看commit 里面的内容, 做了哪些修改
git show com_id
git show com_id filename 查看某次commit 的某个文件进行了哪些修改

# 取消已暂存的文件
git reset HEAD <file>


# 撤销本地修改
git checkout .  //撤销对所有已修改但未提交的文件的修改，但不包括新增的文件
git checkout [fiename] // 撤销对指定文件的修改

# 从远程拉去分支到本地
git checkout -b 本地分支 origin/远程分支

https://mapi.ktvsky.com/api/macopen/get_mac_open?sd=2018-05-23&macs_id=00E07E00AF55,&ed=2018-05-24


工作区 add to 版本库 commit to 暂存区

git commit -a -m 'update' 将所有修改放进暂存区,这个命令在涉及文件路径或者文件名改变的前提下格外有用

git diff 查看工作区与当前版本区的差别, 把修改后的文件add至版本区之后显示自然为空

git status 查看目前版本库与origin master的版本对比

git log 查看当前分支的版本日志

git reset --hard b52a8fbeb4300a30fc4157c6323bebce71a720b3 版本区强制回退, 不保存工作区
git reset --soft b52a8fbeb4300a30fc4157c6323bebce71a720b3 版本区强制回退, 保存工作区

git pull 是将本地版本区和远端版本区合并, 不影响工作区
合并冲突的最合理规则：
<<<head 表示远端版本
===分割冲突内容
>>>b52a8fbeb4300a30fc4157c6323bebce71a720b3 表示本地版本
先确定保留哪一步分，删除另一部分，删除三行提示

关于git stash: git stash 用于回退工作区,
1.初始化仓库，进行一次提交, 提交到暂存区:
git init xinghanggogogo
cd xinghanggogogo && echo 'hello'> readme
git add . && git commit -m "init"
2.修改工作区内容, 查看diff
echo 'need to be stashed' >> readme
git diff(看到差别)
3.使用stash命令, 保存当前工作区
git stash
git diff(显示没有差别)
4.恢复代码
git stash list
git stash apply stash@{0} or git stash pop (这一步可能会冲突, 直接根据提示修改冲突文件即可)
git stash clear 命令用于清空stash-list

关于git branch命令:
git branch
git branch -v
git branch -r

本地创建分支并推送至远端
git checkout -b test or git branch test //从master分支创建test分支，并切换至此
git branch -r //远端分支信息（此时远端还没有test分支）
git push origin test:test(将本地test分支推送到远端)
git branch -r (验证)

拉取远端分支至本地:
git checkout -b test origin/test
或者:
git fetch origin master:test
git diff test
git merge test

关于git fetch: fetch只拉取不合并, 使用场景只有一个, fetch远端分支到本地临时分支, 然后diff查看差别确定是否合并, 然后merge
git fetch origin master:tmp
git diff tmp
git merge tmp

删除本地分支：git branch -d name
删除远端分支：git push origin :name

一个标准的git仓库的配置文件（首先需要添加公钥）
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github.com:xinghanggogogo/Slog.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[user]
	name = xinghang
	email = xinghang@thunder.com.cn

一次实例, 上线后发现代码有误:
服务器运行代码版本回退: make thunder_online commit=e9cbc24aedd0d458d78069902d0adb0eb0bdca05
服务器本地代码强制回退: git reset --hard e9cbc24aedd0d458d78069902d0adb0eb0bdca05

强制拉取, 覆盖本地版本:
git reset --hard
git pull
或者:
git fetch
git reset --hard origin/master

全部提交之后的回退部分文件版本再次提交并且保存上次提交提交的修改:
(http://blog.sina.com.cn/s/blog_68af3f090100rp5r.html)
cd Slog
echo '111' >> gitsum/git.sh
echo '222' >> work/spider/table
git add .
git commit -m 'update'
git push
然后发现内容已经提交至github, 此时想撤销对gitsum/git.sh文件修改的提交, 并且在本地保存此次修改
git log
git reset **** -- gitsum/git.sh (这里修改的版本库)
git diff
发现gitsum/git.sh文件修改还在,说明工作区没有被覆盖
git commit -m 'update'
注意这里没有使用add
git push
完成

查看两个版本指定文件的差异:
git diff 5381dc6c3 9416d240b -- handler/song.py

.gitignore失效的例子:
git rm -r --cached .
git add .
git commit -m 'update .gitignore'



t.ktvsky.com/wow/stat?use_cache=0


工作区 add to 版本库 commit to 暂存区

git commit -a -m 'update' 将所有修改放进暂存区,这个命令在涉及文件路径或者文件名改变的前提下格外有用

git diff 查看工作区与当前版本库的差别，commmit至版本库之后显示自然为空

git status 查看目前版本库与origin master的版本对比

git log 查看当前分支的版本日志

git reset --hard b52a8fbeb4300a30fc4157c6323bebce71a720b3 本地版本强制回退, 不保存工作区
git reset --soft b52a8fbeb4300a30fc4157c6323bebce71a720b3 本地版本撤销, 保存工作区

合并冲突的最合理规则：
<<<head 表示远端版本
===分割冲突内容
>>>b52a8fbeb4300a30fc4157c6323bebce71a720b3 表示本地版本
先确定保留哪一步分，删除另一部分，删除三行提示

关于git stash
git stash 用于回退工作区,
1.初始化仓库，进行一次提交, 提交到暂存区:
git init xinghanggogogo
cd xinghanggogogo && echo 'hello'> readme
git add . && git commit -m "init"
2.修改工作区内容, 查看diff
echo 'need to be stashed' >> readme
git diff(看到差别)
3.使用stash命令, 保存当前工作区
git stash
git diff(显示没有差别)
4.恢复代码
git stash list
git stash apply stash@{0}
git stash clear 命令用于清空stash-list

关于分支操作, 假定当前在master分支
1.本地创建分支并推送至远端
git checkout -b test or git branch test //从master分支创建test分支，并切换至此
git branch -r //远端分支信息（此时远端还没有test分支）
git push origin test:test(将本地test分支推送到远端)
git branch -r (验证)
2.拉取远端分支至本地:
git fetch //将远端分支fetch到当前主机
git checkout -b test origin/test
或者:
git fetch origin master:test

删除本地分支：git branch -d name
删除远端分支：git push origin :name

一个标准的git仓库的配置文件（首先需要添加公钥）
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github.com:xinghanggogogo/Slog.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[user]
	name = xinghang
	email = xinghang@thunder.com.cn

关于fetch:
git fetch：相当于是从远程获取最新版本到本地，不会自动merge
git fetch orgin master:test
git diff test
git merge test

一次实例, 上线后发现代码有误:
服务器运行代码版本回退: make thunder_online commit=e9cbc24aedd0d458d78069902d0adb0eb0bdca05
服务器本地代码强制回退: git reset --hard e9cbc24aedd0d458d78069902d0adb0eb0bdca05

强制拉取, 覆盖本地版本:
git reset --hard
git pull

全部提交之后的回退部分文件版本再次提交并且保存上次提交提交的修改:
(http://blog.sina.com.cn/s/blog_68af3f090100rp5r.html)
cd Slog
echo '111' >> gitsum/git.sh
echo '222' >> work/spider/table
git add .
git commit -m 'update'
git push
然后发现内容已经提交至github, 此时想撤销对gitsum/git.sh文件修改的提交, 并且在本地保存此次修改
git log
git reset **** -- gitsum/git.sh (这里修改的版本库)
git diff
发现gitsum/git.sh文件修改还在,说明工作区没有被覆盖
git commit -m 'update'
注意这里没有使用add
git push
完成

查看两个版本指定文件的差异:
git diff 5381dc6c3 9416d240b -- handler/song.py

>>> git stash 使用情景
当我们正在dev分支开发新功能时， 有人反馈一个bug，让我们马上修改，
但是新功能做到了一半，又不想提交

git stash
保存当前工作进度，会把暂存区和工作区的改动保存起来，执行完这个命令后，就会发现当前是一个干净地工作区，没有任何改动
使用 git stash save 'message...'可以添加注释
git stash list
可以显示保存进度的列表
修改完bug之后，我们可以切换到dev并恢复工作区: git stash pop

git stash clear 删除说有存储的进度
git stash drop [stash_id] 删除一个存储进度， 如果不指定id则默认删除最新进度

