import os
from psd_tools import PSDImage
for filename in os.listdir('.'):
    if filename.endswith(".psd") : 
        psd = PSDImage.open(filename)
        os.mkdir('res'+filename)
        for layer in psd:
            if layer.is_group():
                for child in layer:
                    print(child)
                    layer_image = child.composite()
                    layer_image.save('res'+filename+'/%s.png' % child.name)
