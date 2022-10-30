from PIL import Image

def resize_img(file_name: str, whidth: int, length: int)-> new_file_name:str, new_resolution:int
    # # for print banner
    # if resolution > 72:
    #     # уменьшаем
    #     if resolution < 72
    img = Image.open(file_name)
    s = img.size
    resolution = round(img.info['dpi'][0], 0)
            width = round(2.54 * s[0] / resolution, 0)
            length = round(2.54 * s[1] / resolution, 0)