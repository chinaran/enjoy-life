# git standard commit

git 标准化 commit message 工具  
灵感来源于[这篇文章](https://github.com/superhj1987/pragmatic-java-engineer/blob/master/book/chapter2-project/vcs.md#223-%E6%8F%90%E4%BA%A4%E6%97%A5%E5%BF%97 "提交日志")  

## 1. 标准化 commit message
规范且有意义的提交记录，有助于追踪代码修改和查看历史记录  
现在支持以下九种类型（参考 Angular 规范的 commit message）

* **feat**：     新功能（feature）
* **fix**：      修补bug
* **docs**：     文档（documentation）
* **style**：    格式（不影响代码运行的变动）
* **refactor**： 重构（即不是新增功能，也不是修改bug的代码变动）
* **test**：     增加测试
* **chore**：    构建过程或辅助工具的变动
* **perf**：     性能优化（performance）
* **tmp**：      临时提交（可用于非 master 分支）

## 2. 使用效果

![工具使用示例](./src/img/git-std-commit-msg.gif "工具使用示例")

## 3. 安装
shell 切换成 zsh，使用 oh-my-zsh 更佳

* 方法一

  把 [git_std_commit.sh](./git_std_commit.sh) 文件内容拷贝到 ~/.zshrc 中

* 方法二

  下载 [git_std_commit.sh](./git_std_commit.sh) 到某个路径(dir)，  
  在 ~/.zshrc 末尾添加 source dir/git_std_commit.sh

工具生效都需要执行 source ~/.zshrc

## 4. 使用方法

在终端输入 `gcmm` 后，使用 Tab 键选择 commit 类型，然后输入提交信息

```Bash
gcmm-xxx msg1 msg2 ...
```

当 `msg` 参数多于一个时，信息会按照列表提交，如 `xxx 1.msg1; 2.msg2.`  
除了 `gcmm-tmp`，其他命令必须包含提交信息

## 5. 其他

使用 shell 函数是最简单的实现方法  
因为 zsh 就可以使用 Tab 进行选择了  
更好的实现应该使用 zsh 提供的命令提示模块
