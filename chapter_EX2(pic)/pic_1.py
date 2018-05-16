# 使用PIL库进行图片处理
from PIL import Image

# 简单的开篇
im = Image.open('test.jpg')
# 将图片旋转45度，并用系统自带的图片工具显示图片
im.rotate(45).show()