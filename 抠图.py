from removebg import RemoveBg
import os

rmbg = RemoveBg('tQ7dLhmar9UzpXbPJDQa1kRi','error.log')

rmbg.remove_background_from_img_file(r'C:\Users\myco\desktop\test.png')

#path = '%s/picture' % os.getcwd()
#for pic in os.listdir(path):
#    rmbg.remove_background_from_img_file('%s/%s'%(path,pic))