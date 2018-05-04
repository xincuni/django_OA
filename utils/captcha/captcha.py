# coding=utf-8
from random import randint, choice
from PIL import Image, ImageDraw, ImageFont
from cStringIO import StringIO
from string import printable


# def create_captcha():
#     font_path = "utils/captcha/font/Arial.ttf"
#     img = Image.open('files/upload_files/1.jpg')
#     # font = ImageFont.truetype(font_path, 100)
#     # draw = ImageDraw.Draw(img)
#     # draw.text((0, 0), 'abcd', font=font, fill=(0,255,0))
#     out = StringIO()  # 内存文件
#     img.save(out, format='jpeg')
#     content = out.getvalue()
#     out.close()
#     return '', content
#     # pillow
#     font_color = (randint(150, 200), randint(0, 150), randint(0, 150))
#     line_color = (randint(0, 150), randint(0, 150), randint(150, 200))
#     point_color = (randint(0, 150), randint(50, 150), randint(150, 200))
#     width, height = 100, 40
#     image = Image.new('RGB', (width, height), (200, 200, 200))  # 创建画布
#     font = ImageFont.truetype(font_path, height - 10)  # 创建文字
#     draw = ImageDraw.Draw(image)  # 创建画笔
#     # #生成验证码
#     text = ''.join([choice(printable[:62]) for i in xrange(4)])
#
#     # #font_width, font_height = font.getsize(text)
#     # #把验证码写到画布上
#     draw.text((10, 10), text, font=font, fill=font_color)
#     # #绘制线条
#     for i in xrange(0, 5):
#         draw.line(((randint(0, width), randint(0, height)),
#                    (randint(0, width), randint(0, height))),
#                   fill=line_color, width=2)
#     # 绘制点
#     for i in xrange(randint(100, 1000)):
#         draw.point((randint(0, width), randint(0, height)), fill=point_color)
#     # 输出
#     out = StringIO()
#     image.save(out, format='jpeg')
#     content = out.getvalue()
#     out.close()
#     print '图型验证码', text
#     return text, content

def create_captcha():
    font_path = "utils/captcha/font/Arial.ttf"
    # img = Image.open('files/upload_files/1.jpg')
    # font = ImageFont.truetype(font_path, 100)
    # draw = ImageDraw.Draw(img)
    # text = 'aa'
    # draw.text((20, 20), text=text, font=font, fill=(255, 0, 0))
    # out = StringIO()
    # img.save(out, format('jpeg'))
    # content = out.getvalue()
    # out.close()

    font_color = ((randint(150, 200)), (randint(0, 150)), (randint(0, 255)))
    line_color = ((randint(150, 200)), (randint(0, 150)), (randint(0, 255)))
    point_color = ((randint(150, 200)), (randint(0, 150)), (randint(0, 255)))

    width, height = 100, 40
    img = Image.new('RGB', (width, height), (200, 200, 200))  # 颜色类型,宽高,底色

    font = ImageFont.truetype(font_path, height - 10)  # 创建文字
    draw = ImageDraw.Draw(img)  # 创建画笔
    """
    验证码
    """
    text = ''.join([choice(printable[0:62]) for i in xrange(4)])

    draw.text((10, 10), text, font=font, fill=font_color)
    draw.line(((20, 10), (100, 100)), fill=line_color, width=2)
    for i in xrange(0, 5):
        draw.line((randint(0, width), (randint(0, height)),
                   randint(0, width), (randint(0, height))),
                  fill=line_color)

    for i in xrange(100,500):
        draw.point((randint(0, width), (randint(0, height))),fill=point_color)
    print 'adsa', text
    out = StringIO()
    img.save(out, format('jpeg'))
    content = out.getvalue()
    out.close()
    return text, content
