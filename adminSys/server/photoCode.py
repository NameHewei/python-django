from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机大写字母
def upperChar():
    # chr() 方法返回数字对应的英文字母
    return chr(random.randint(65, 90))

# 随机颜色
def randomColor():
    return (random.randint(50,255), random.randint(50,255), random.randint(50,255))

width = 200
height = 50
fontSize = 45

image = Image.new('RGB', (width, height), (255, 255, 255))

# 用 truetype font 创建Font对象:  
# 参数：font=None, size=10, index=0, encoding='', layout_engine=None
font = ImageFont.truetype('Futura LT Bold.ttf', fontSize)
# font = ImageFont.truetype('arial.ttf', fontSize)

# 创建Draw对象:
draw = ImageDraw.Draw(image)

# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=(255,255,255))
        
# 输出文字:
for t in range(4):
    xy = (50 * t + 10, -5)
    draw.text(xy, upperChar(), font=font, fill=randomColor())

draw.line([(0,0), (50,30)],'#223388',3)
draw.line([(70,25), (170,0)],'#223388',2)

# 最后一个参数的值为外边框的宽度
# 以两个点位构成一个矩形，以矩形中点为扇形中心，以向右（3点钟方向）为0度，顺时针旋转
draw.pieslice([(100,5), (140,40)],0, 130, '#223388',1)

# 模糊:
# image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
