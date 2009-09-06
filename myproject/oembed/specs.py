from imagekit.specs import ImageSpec 
from imagekit import processors 

# first we define our thumbnail resize processor 
class ResizeThumb(processors.Resize):
    width = 140 
    height = 105 
    crop = True

class EnchanceThumb(processors.Adjustment):
    contrast = 1.2 
    sharpness = 1.1 

class Thumbnail(ImageSpec):
    pre_cache = True 
    processors = [ResizeThumb, EnchanceThumb] 
