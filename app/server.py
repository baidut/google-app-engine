import io
import json

from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request, make_response

from PIL import Image as PIL_Image
from fastiqa.basics import *
from fastiqa.models.bunches import Im2MOS
from fastiqa.models._body_head import BodyHeadModel

app = Flask(__name__)

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # file = request.files['file']
        #img_bytes = file.read()
        img = PIL_Image.open(request.files['file'].stream)
        print(img.mode)
        print(img.size)
        
#         data = {'score': img.mode, 
#                 'message': 'Created', 'code': 'SUCCESS',
#                 'success': True, 'status': 'OK',
#                 'ContentType':'application/json'
#                }
#         return make_response(jsonify(data), 200) # 201
        im = Image(pil2tensor(img, dtype=np.float32))
        
        data = Im2MOS(TestImages)
        model = BodyHeadModel() # RoIPoolModel()

        learn = IqaLearner(data, model, path='.') 
        #learn.load('RoIPoolModel-fit(10,bs=120)')

        # im = open_image(file)
        score = learn.predict(im)[0].obj[0]
        data = {'score': score, 
                'message': 'Created', 'code': 'SUCCESS',
                'success': True, 'status': 'OK',
                'ContentType':'application/json'
               }
        # class_id, class_name = get_prediction(image_bytes=img_bytes)
        return make_response(jsonify(data), 200) # 201
        


if __name__ == '__main__':
    app.run()