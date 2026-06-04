from markdown_blocks import *
import os

def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block.startswith("# "):
            return block[2:].strip()
    raise Exception("no h1 header")
'''with open("./content/index.md") as f:
    print(extract_title(f.read()))
print(extract_title("# Hello"))'''

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    mdData = open(from_path)
    mdFile = mdData.read()
    mdData.close()
    templateData = open(template_path)
    template = templateData.read()
    templateData.close()

    pageContent = markdown_to_html_node(mdFile).to_html()
    pageTitle = extract_title(mdFile)

    template = template.replace("{{ Title }}", pageTitle).replace("{{ Content }}", pageContent).replace('href="/', f'href="{basepath}').replace('src="/',f'src"{basepath}')
    print(template)
    destDir = os.path.dirname(dest_path)
    if not os.path.exists(destDir):
        os.makedirs(destDir)
    
    page = open(dest_path, "w")
    page.write(template)
    page.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    '''if not os.path.exists(dir_path_content):
        raise Exception("content path does not exist")
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)'''
    content_files = os.listdir(dir_path_content)
    for file in content_files:
        src = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(src):
            if src.endswith(".md"):
                filename = dest_path.replace(".md",".html")
                generate_page(src, template_path, filename, basepath)
        else:
            generate_pages_recursive(src, template_path, dest_path, basepath)
    


