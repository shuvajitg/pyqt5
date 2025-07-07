from PIL import Image, ImageFilter

with Image.open("/home/shuvajit/dev/python/desktopapp/pyqt5-tutorial/photo-editing/work.jpg") as picture:
    black_white = picture.convert("L")
    black_white.save('black_white.jpg')
    
    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save("mirror.jpg")
    
    blur = picture.filter(ImageFilter.BLUR)
    blur.save("blur.jpg")