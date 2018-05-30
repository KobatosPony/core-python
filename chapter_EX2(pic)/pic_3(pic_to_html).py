# 获取像素并写入html
from PIL import Image
import numpy as np
import time

# 获取并加载图像
im = Image.open('test.jpg')

width = im.size[0]
height = im.size[1]

# 太大了不好，缩小一下
im = im.resize((150,int(height*150/width)),Image.ANTIALIAS)
width = im.size[0]
height = im.size[1]

pic = im.load()
# 使用三维的矩阵来储存图片信息
pic_vector = np.zeros((width,height,3))

# 获取并保存
for x in range(width):
    for y in range(height):
        pic_vector[x][y][0],pic_vector[x][y][1],pic_vector[x][y][2]= pic[x,y]


# 转化为html代码
pic_html = []

for y in range(height):
    pic_html.append("<tr>")
    for x in range(width):
        r, g, b = pic[x, y]
        pic_html.append("<td style='background-color: rgb(%d,%d,%d)'></td>" % (r,g,b))
    pic_html.append("</tr>")



start_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<style>
    *{
        margin: 0 auto;
        padding: 0;
    }
    table{
        border-collapse: collapse;
    }
    td{
        width: 1px;
        height: 1px;
    }
</style>
<body>
<table>
"""

end_code = """
</table>
</body>
    </html>
"""

# 写入
with open('pic_to_html.html','w+') as html:
    html.write(start_code)
    for i_code in pic_html:
        html.write(i_code)
    html.write(end_code)