# install pillow
# import pillow
# open up the image we want to resize using python
# print the current size of the image
# specify the size we want to change it to
# save the new resized image


from PIL import Image


def resize_image(size1, size):
    image = Image.open('UPWORK_PICTURE.PNG')

    print(f"Current size : {image.size}")

    resized_image = image.resize((size1, size2))

    resized_image.save('UPWORK_PICTURE-' + str(size1) + '.PNG')


size1 = int(input("Enter Width: "))
size2 = int(input("Enter Length: "))
resize_image(size1, size2)
