import sys
import os
# print(sys.copyright)
# sys.path被执行文件的当前路径 + 其他python自定的路径
print(sys.path)
# python path/filename 执行时后面带的被执行文件名包括路径:path/filename
print(__file__)
# python path/filename 执行时所在的目录，及pwd值
print(os.getcwd())