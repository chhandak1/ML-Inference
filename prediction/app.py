from flask import Flask, jsonify,request
import io
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models
import json

app=Flask(__name__)

labels = json.load(open('./imagenet_class_index.json'))

# load model from pytorch
model=models.densenet121(pretrained=True)
model.eval()

#image transformations
def image_transformation(image_bytes):
    transform_img = transforms.Compose([transforms.Resize(255),transforms.CenterCrop(224),transforms.ToTensor(),transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])
    img = Image.open(io.BytesIO(image_bytes))
    return transform_img(img).unsqueeze(0)

#prediction results
def predict_label(image_bytes):
	img=image_transformation(image_bytes=image_bytes)
	outputs_from_model=model.forward(img)
	tmp,y_pred=outputs_from_model.max(1)
	y_pred_id = str(y_pred.item())
	return labels[y_pred_id]

@app.route('/')
def root():
    return "0"

#post request to run prediction on image
@app.route('/run_inference', methods=['POST'])
def run_inference():
    if request.method == 'POST':
        img = request.files['file']
        bytes_from_img = img.read()
        identifier, label_name = predict_label(image_bytes=bytes_from_img)
        return jsonify({'class_id':identifier, 'class_name': label_name})

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)