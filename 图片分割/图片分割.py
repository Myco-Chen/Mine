from PIL import Image

def fill_image(img):
    width, height = img.size
    new_image_length = width if width> height else height
    new_image = Image.new(img.mode,(new_image_length,new_image_length),color='white')
    if width > height:
        new_image.paste(img,(0,int((new_image_length-height)/2)))
    else:
        new_image.paste(img,(int((new_image_length-width)/2),0))
    return new_image

def cut_image(img):
    width,height = img.size
    item_width = int(width/3)
    box_list = []
    for i in range(0,3):
        for j in range(0,3):
            print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)
    img_list = [img.crop(box) for box in box_list]

    return img_list

def save_images(img_list):
    index = 1
    for img in img_list:
        img.save("./"+str(index)+'.png','PNG')
        index += 1

if __name__ == '__main__':
    image = Image.open('./mv.jpg')
    image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)