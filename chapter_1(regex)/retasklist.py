# 处理dos环节下tasklist命令的输出

import os
import re

# popen 使用一个新的进程来运行系统的命令
# 有三个参数，分别为命令、模式、和缓冲流大小
f = os.popen('tasklist /nh','r')

# \s 匹配非空白自由
for eachLine in f:
    print(
        re.findall(
            '([\w.]+(?:[\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d.]+ K)',
            eachLine.rstrip()
        )
    )

f.close()