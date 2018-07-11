yarn 类似于npm的包管理工具，
优点：
1，速度快
npm会等一个包完全安装完才跳到下一个包，但yarn会并行执行包，因此速度会快很多；		
2，离线模式
安装过的包会保存进缓存目录，以后安装就直接从缓存中复制多来
3，版本控制
npm的一个痛点就是当包的依赖层次表深时，版本控制不够精确。会出现相同package.json，
但不同人的电脑上安装出不同版本的依赖包，出现类似 “我电脑上是好的，没问题呀”的bug很
难查找， 可以使用npm-shrinkwrap来实现版本固化，版本信息会写入npm-shrinkwrap.json
文件中，但它毕竟不是npm的标准配置。yarn天生就能实现版本固化，还会锁定所有他依赖包的
版本号。yarn.lock用开存储每个包的确切依赖版本，确保从本地开发到生产环境，所有机器上
都有精确相同的依赖版本

安装
mac
brew install yarn

工作流
1，创建一个新项目
2，增加/更新/删除依赖
3，安装/重装你的依赖
4，引入版本控制系统
5，持续集成

1，创建一个新项目
不论是已经有了现成的代码仓库（目录），还是正着手启动一个全新项目，
都可以使用同样的方法引入Yarn。
yarn init
打开一个yarn项目的交互式表单，其中包含一下问题:
'''
question name (slog):
question version (1.0.0):
question description:
question entry point (index.js):
question repository url (git@github.com:whycome/slog.git):
question author (wawa <whying100@163.com>):
question license (MIT):
question private:
success Saved package.json
'''
会在项目根目录生成package.json, 存储项目的有关信息，包括项目名称，维护者信息，
代码托管地址，以及项目依赖
2，管理依赖
可以通过以下命令来管理依赖
# 添加项目依赖, 痛死yarn.lock也会被更新
yarn add [package]
yarn add [package]@[version]
yarn add [package]@[tag]
# 更新依赖包，同时会更新package.json, yarn.lock
yarn upgrade [package]
yarn upgrade [package]@[version]
yarn upgrade [package]@[tag]
# 删除依赖包, 同时会更新package.json, yarn.lock
yarn remove [package]
3, 安装依赖
# 安装一个项目的所有依赖。 Yarn会从package.json中读取依赖，并将依赖信息存储到yarn.lock中。
yarn 或者 yarn install  # 安装所有
yarn install --flat   # 安装一个包的单一版本
yarn install --force  # 强制重新下载所有包
yarn install --production. # 只安装生产环境依赖
4， 版本控制
package.json, yarn.lock 提交到版本控制

yarn init # 初始化项目
# 添加依赖包

# 安装项目的全部依赖
yarn 或 yarn install
