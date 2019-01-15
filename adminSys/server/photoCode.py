from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机大写字母
def upperChar():
    # chr() 方法返回数字对应的英文字母
    return chr(random.randint(65, 90))

# 随机颜色
def randomColor():
    return (random.randint(50,255), random.randint(50,255), random.randint(50,255))

width = 360
height = 50

image = Image.new('RGB', (width, height), (255, 255, 255))

# 用 truetype font 创建Font对象:  
font = ImageFont.truetype('arial.ttf', 40)

# 创建Draw对象:
draw = ImageDraw.Draw(image)

# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=(255, 255,255))
        
# 输出文字:
for t in range(4):
    a = (40 * (2*t + 1) , 5)
    draw.text(a, upperChar(), font=font, fill=randomColor())

# 模糊:
# image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
