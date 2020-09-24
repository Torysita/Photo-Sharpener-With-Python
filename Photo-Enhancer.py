
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

imageObject = Image.open("/System/Volumes/Data/Users/torywhite/Downloads/VINONE.jpeg");
imageObject.show()

# Apply sharp filter
sharpened1 = imageObject.filter(ImageFilter.SHARPEN);
sharpened2 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened3 = sharpened2.filter(ImageFilter.SHARPEN);
sharpened4 = sharpened3.filter(ImageFilter.SHARPEN)

# Show the sharpened images
sharpened4.show()


#image brightness enhancer
enhancer = ImageEnhance.Contrast(sharpened2)


factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.show()


#image brightness enhancer
brighten = ImageEnhance.Brightness(im_output)


factor = 1.8 #brightens the image
bright_output = enhancer.enhance(factor)
bright_output.show()


sharpen = ImageEnhance.Sharpness(bright_output)

factor = 2
sharpen_image = enhancer.enhance(factor)
sharpen_image.show()

