import os
from psd_tools import PSDImage
for filename in os.listdir('.'):
	if os.path.isfile(filename) and filename.endswith(".psd") : 
		psd = PSDImage.open(filename)
		psd.composite().save(filename+'.png')
