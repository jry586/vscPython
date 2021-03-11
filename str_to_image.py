import base64
import os


def get_file_list( p ):
        p = str( p )
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[ -1] != "\\":
              p = p+"\\"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isfile( p + x ) ]
        return b
def name_change(source_file):
    strlist=source_file.split('_')
    num = int(strlist[1],16)
    name = "{:0>5d}.jpg".format(num)
    return name
def str_to_image(path,source_file):
    destination_file = name_change(source_file)
    sfile = open(path+source_file,'r')
    dfile = open(path+destination_file,'wb')
    fstr = sfile.read()
    strlist = fstr.split(',')
    image_str = strlist[3][:-1]
    dfile.write(base64.b64decode(image_str))
    sfile.close()
    dfile.close()
    
path = input("请输入源文件夹位置：")
if not (os.path.exists(path) and os.path.isdir(path)):
    print("输入的不是有效目录！")
if path[ -1] != "\\":
        path = path+"\\"
flist=get_file_list(path)

for sfile in flist:
        try:
                str_to_image(path,sfile)
        except:
                continue
    
