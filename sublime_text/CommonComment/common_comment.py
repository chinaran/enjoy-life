import datetime, getpass
import sublime, sublime_plugin
import datetime
import sys
import os


# 优化文件路径
# 包含 git 仓库的文件路径从 git 仓库开始，否则只保留文件名字
def handle_code_file_path(file_path):
    # 该列表可以自由添加
    l = ["github.com", "git.bdmd.com"]
    for git in l:
        i = file_path.find(git)
        if i != -1:
            return file_path[i:]
    return os.path.basename(file_path)

def getCurDatetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 添加文件开头注释
class AddFileCommentCommand(sublime_plugin.TextCommand):
    def __init__(self, edit):
        settings = sublime.load_settings("CommonComment.sublime-settings")
        author_name = settings.get('author_name', 'Your Name')
        author_email = settings.get('author_email', 'yours@email.com')
        self.comment_author = "%s (%s)" %(author_name, author_email)
        if sys.version_info[0] == 2:
            super(AddFileCommentCommand, self).__init__(edit)
        else:
            super().__init__(edit)

    def run(self, edit):
        settings = sublime.load_settings("CommonComment.sublime-settings")
        file_path = self.view.file_name()
        if file_path is None:
            print("Can not comment without file")
            return
        if file_path.endswith(".py"):
            self.view.run_command("insert_snippet",
                {
                    "contents": '"""' "\n"
                        "    Author:       " + self.comment_author + "\n"
                        "    Created Time: " "%s" %getCurDatetime() + "\n"
                        "    File Name:    " "%s" %handle_code_file_path(file_path) + "\n"
                        "    Description:  " "\n"
                    '"""'
                }
            )
        elif file_path.endswith(".sh"):
            self.view.run_command("insert_snippet",
                {
                    "contents": "##""\n"
                    " # Author:        " + self.comment_author + "\n"
                    " # Created Time:  " "%s" %getCurDatetime() + "\n"
                    " # File Name:     " "%s" %handle_code_file_path(file_path) + "\n"
                    " # Description:   " "\n"
                    " # Usage Example: " "./" + os.path.basename(file_path) +  " \n"
                    " ##\n"
                }
            )
        elif file_path.endswith(".md"):
            self.view.run_command("insert_snippet",
                {
                    "contents":
                    "<!-- Author:       " + self.comment_author + " -->\n"
                    "<!-- Created Time: " "%s" %getCurDatetime() + " -->\n"
                    "<!-- File Name:    " "%s" %handle_code_file_path(file_path) + " -->\n"
                    "<!-- Description:  " " -->\n"
                }
            )
        else: # go c/c++
            self.view.run_command("insert_snippet",
                {
                    "contents": "/**""\n"
                    " * Author:       " + self.comment_author + "\n"
                    " * Created Time: " "%s" %getCurDatetime() + "\n"
                    " * File Name:    " "%s" %handle_code_file_path(file_path) + "\n"
                    " * Description:  " "\n"
                    " */\n"
                }
            )

# 添加代码块注释
class AddCodeBlockCommentCommand(sublime_plugin.TextCommand):
    def __init__(self, edit):
        settings = sublime.load_settings("CommonComment.sublime-settings")
        self.author_name = settings.get('author_name', 'Your Name')
        if sys.version_info[0] == 2:
            super(AddFileCommentCommand, self).__init__(edit)
        else:
            super().__init__(edit)

    def run(self, edit):
        file_path = self.view.file_name()
        if file_path is None:
            print("Can not comment without file")
            return
        if file_path.endswith(".py"):
            self.view.run_command("insert_snippet",
                {
                    "contents": "##  (%s %s) ##" % (self.author_name, getCurDatetime()) 
                }
            )
        elif file_path.endswith(".sh"):
            self.view.run_command("insert_snippet",
                {
                    "contents": "##  (%s %s) ##" % (self.author_name, getCurDatetime())
                }
            )
        elif file_path.endswith(".md"):
            self.view.run_command("insert_snippet",
                {
                    "contents": "<!--  (%s %s) -->" % (self.author_name, getCurDatetime())
                }
            )
        else: # go c/c++
            self.view.run_command("insert_snippet",
                {
                    "contents": "/**  (%s %s) **/" % (self.author_name, getCurDatetime())
                }
            )

# 添加当前时间
class AddCurrentDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": "%s" %getCurDatetime()
            }
        )
