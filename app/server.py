from flask import Flask, jsonify, request, make_response
from PIL import Image as PIL_Image

app = Flask(__name__)


@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        return '<h1>hello world</h1>'
    elif request.method == 'POST':
        return '<h1>POST</h1>'
    else:
        return '<h1>Else</h1>'

@app.route('/predict', methods=['GET','POST'])
def predict():
    # file = request.files['file']
    #img_bytes = file.read()
    img = PIL_Image.open(request.files['file'].stream)
    print(img.mode)
    print(img.height)

    data = {'mode': img.mode, 'height': img.height, 
            'message': 'Created', 'code': 'SUCCESS',
            'success': True, 'status': 'OK',
            'ContentType':'application/json'
           }
    # class_id, class_name = get_prediction(image_bytes=img_bytes)
    return make_response(jsonify(data), 200) # 201  


if __name__ == '__main__':
    app.run()