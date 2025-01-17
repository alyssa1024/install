# -*- coding: utf-8 -*-
from .base import BaseTool
from .base import PrintUtils,CmdTask,FileUtils,AptUtils,ChooseTask
from .base import osversion,osarch
from .base import run_tool_file

class Tool(BaseTool):
    def __init__(self):
        self.name = "Quick-Install:Vscode"
        self.type = BaseTool.TYPE_INSTALL
        self.autor = '小鱼'

    def install_vscode(self):
        PrintUtils.print_info("开始根据系统架构,为你下载对应版本的vscode~")
        # 根据系统架构下载不同版本的安装包
        if osarch=='amd64':
            CmdTask('sudo wget http://vscode.cdn.azure.cn/stable/5554b12acf27056905806867f251c859323ff7e9/code_1.64.0-1643863948_amd64.deb -O /tmp/vscode.deb',os_command=True).run()
        elif osarch=='arm64':
            CmdTask('sudo wget http://vscode.cdn.azure.cn/stable/5554b12acf27056905806867f251c859323ff7e9/code_1.64.0-1643862176_arm64.deb -O /tmp/vscode.deb',os_command=True).run()
        else:
            return False
        PrintUtils.print_info("下载完成,接下来为你安装Vscode~")
        CmdTask("sudo dpkg -i /tmp/vscode.deb").run()
        CmdTask("rm -rf /tmp/vscode.deb").run()
        PrintUtils.print_info("安装完成~")

    def run(self):
        self.install_vscode()

