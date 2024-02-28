import argparse
import urllib.request
from PIL import Image


def download_image(url):
    path, _ = urllib.request.urlretrieve(url)
    # print(path)
    return path


def trans2png(path):
    im = Image.open(path).convert("RGBA")
    im.save(path + ".png", "png")
    return path + ".png"


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("input_file", help="输入文件")
    parse.add_argument("output_file", help="输出文件", nargs="?")
    args = parse.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    # if input_file.startswith("http"):
    #     if output_file is None:
    #         output_file = download_image(input_file)
    if input_file.endswith(".webp"):
        if output_file is None:
            output_file = trans2png(input_file)
