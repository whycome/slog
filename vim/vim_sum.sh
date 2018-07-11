vim transport
cd ~/.vim
mkdir bundle; mkdir colors
cd bundle
git clone http://github.com/gmarik/vundle.git
cd colors
scp work@106.75.97.4:/home/work/.vim/colors/SerialExperimentsLain.vim .
cp .vimrc
:BundleInstall

youcompleteme
编译: cd ~/.vim/bundle/youcompleteme;
http://valloric.github.io/YouCompleteMe/#ubuntu-linux-x64
python install.py

关于NERDTree插件的使用:
http://www.jianshu.com/p/eXMxGx
\f 绑定:NERDTree
t s i gt gT

ack.vim插件的使用:
http://www.jianshu.com/p/2f1c140c7eb8

一键运行python代码:
au BufRead *.py map <buffer> <F5> :w<CR>:!/usr/bin/env python % <CR>

gd选中当前单词
:noh取消选中

目录树:
https://my.oschina.net/VASKS/blog/388907

u撤销
ctrl+r回复撤销

:news 创建新的空白屏
:sv水平分屏
:vs垂直分屏
ctrl w w 换屏
ctrl w hjkl 换屏
ctrl+w q 关闭当前屏幕
ctrl+w o: 取消其他分屏只保留当前分屏

yy直接复制当前行, p直接粘贴
可以yy+p看看效果
nyy可以复制多行, 然后移动光标, p

滚屏
ctrl+e 向下一行
ctrl+y 向上一行
crtl+o 将光标移动到上次的位置
z. 将光标所在行移动到屏幕中间

标记跳转
ma `a`

整行选中:
shift v

H 将光标移到屏幕上的起始行（或最上行）；
M 将光标移到屏幕中间；
L 将光标移到屏幕最后一行。 

w  右移光标到下一个字的开头；
e  右移光标到一个字的末尾；
b  左移光标到前一个字的开头；
0  数字０，左移光标到本行的开始；
$  右移光标，到本行的末尾；
^  移动光标，到本行的第一个非空字符。

s: 替换
:s/foo/bar/g : 当前行foo替换bar
%s/foo/bar/g : 全文替换
