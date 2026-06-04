#./main.sh
from textnode import *
from extract_markdown import *
import os
import shutil
import sys

def main():
    basepath = "/"
    if len(sys.argv)>1:
        basepath = sys.argv[1]
    #node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(node)
    copy("./static", "./docs")
    #generate_page("./content/index.md","./template.html","public/index.html")
    generate_pages_recursive("./content", "./template.html","./docs", basepath)

def copy(src, dest):
    if not os.path.exists(src):
        raise Exception("source does not exist")
    if not os.path.exists(dest):
        os.mkdir(dest)
    else:
        print(f"deleting {dest}")
        shutil.rmtree(dest)
        os.mkdir(dest)
    copy_dir(src, dest)
    
def copy_dir(src, dest):
    print(f"{src} -> {dest}")
    children = os.listdir(src)
    for child in children:
        print(child)
        new_src = os.path.join(src, child)
        new_dest = os.path.join(dest, child)
        if os.path.isfile(new_src):
            shutil.copy(new_src, new_dest)
        else:
            os.mkdir(new_dest)
            copy_dir(new_src, new_dest)

main()