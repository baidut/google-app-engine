%matplotlib inline
from fastiqa.all import *

path = '.' # path to model file
file = 'images/Picture1.jpg'
im = open_image(file)

data = Im2MOS(TestImages)
model = RoIPoolModel()

learn = RoIPoolLearner(data, model, path='.') 
learn.load('RoIPoolModel-fit(10,bs=120)')

# qmap = learn.predict_quality_map(im, [32, 32])
qmap = learn.predict_quality_map(im, [32, 32])
print(qmap.global_score)