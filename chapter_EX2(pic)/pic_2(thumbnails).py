# 创建缩略图
import glob
import os
from PIL import Image

SIZE = (128,128)

for infile in glob.glob('*.jpg'):
    file_name,ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(SIZE,Image.ANTIALIAS)  #等比例缩放 ANTIALIAS代表抗锯齿
    im.save(file_name+".thumbnail",'JPEG')
    # 缩略图不能直接打开,需要用show()方法查看
    im.show()