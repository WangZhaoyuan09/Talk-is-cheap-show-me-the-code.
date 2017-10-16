#coding:utf-8

from PIL import Image

import argparse


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return " "
    gray = (2126 * r + 7152 * g + 722 * b) / 10000
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    x = int((gray / (alpha + 1.0)) * len(ascii_char))

    return ascii_char[x]


def write_file(out_file_name,content):
    with open(out_file_name,"w") as f:
        f.write(content)


def main(file_name="test.jpg",width=80,height=80,out_file_name="out_file"):
    text = ""
    im = Image.open(file_name)
    im = im.resize((width,height), Image.NEAREST)
    for i in xrange(height):
        for j in xrange(width):
            content = im.getpixel((j, i))
            text += get_char(*context)
        text += "\n"
    print text
    write_file(out_file_name, text)

def parse_param():              
    parser = argparse.ArgumentParser()
    # input_file
    parser.add_argument("input_file")
    parser.add_argument("out_file")

    parser.add_argument("--width", type=int, default=50)
    parser.add_argument("--height", type=int, default=50)

    args = parser.parse_args()
    width, height, in_file, out_file = args.width, args.height, args.input_file, args.out_file
    return width, height, in_file, out_file

if __name__=='__main__':
    width, height, in_f, out_f = parse_param()
    main(file_name="test.png",width=width, hight=heigt, out_file_name=out_f)
