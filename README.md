<h2 align="center"> Motorbike-Helmet_detection-using-YOLOV3</h2>

<h3 align="left"> YOLOV3</h3>

 <p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/74568334/140792130-bfefeb77-c557-4332-bd5b-9a66cf24cc0e.png">
</p> 

<p style= 'text-align: justify;'> YOLO stands for "You Only Look Once" which uses Convolutional Neural Networks for Object Detection. On a single image, 
           YOLO may detect multiple objects. It implies that, in addition to predicting object classes, YOLO also recognises its positions in the image. 
           The entire image is processed by a single Neural Network in YOLO. The picture is divided into regions using this Neural Network, 
           which generates probabilities for each region. YOLO predicts multiple bounding boxes that cover some regions of the image and then based on
           the probabilities, picks the best one. Moreover, 
  
               1. YOLOv3 has a total of 106 layers where detections are made at 82, 94 and 106 layers.

               2. It consists of a residual blocks, skip connections and up-sampling.

               3. Each convolutional layer is followed by batch normalization layer and Leaky ReLU activation function.

               4. There are no pooling layers, but instead, additional convolutional layers with stride 2, are used to down-sample feature maps.

</p>

<h3 align="left">Problems Statment </h3>

<p style= 'text-align: justify;'> When riding a motorcycle, we must We have to wear a helmet according to the rules of the road. Therefore, these rules are monitored by the police. Due to the invention of high quality cameras and the development of the state of the art in AI, the surveillance system willing to use AI systems to detect whether the occupants are wearing a helmet or not. In this category, I have developed a model that can first detect the motorcycle and then find out who is sitting on the motorcycle. Finally, it will determine whether the person is wearing a helmet or not. For this purpose, I trained the pre-trained model YOLOV3 to recognise motorcycles and people.</p>

<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/74568334/121785707-a4d9eb80-cbbb-11eb-8085-14edab126732.jpg">
</p> 


<h4 align="center"> <span style="color:green">Motor Bike detection/ Helmet detection/ Human detection system built with OpenCV, Keras/TensorFlow using Deep Learning and Computer Vision concepts like YOLOV3</span></h4>


<p align="left">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/121785810-3ba6a800-cbbc-11eb-9140-ac220fca83f0.jpg">
  <img width="300" src="https://user-images.githubusercontent.com/74568334/121785807-3a757b00-cbbc-11eb-9db7-7838ec2af5eb.jpg">
</p> 


<h2 align="center"> Technologies Used </h2>
 
 ```
                    1. IDE - Pycharm
                    2. YOLOV3 - Pre-Trained Object Detection Model
                    3. GPU - P-4000
                    4. Google Colab - Just for Image analysis
                    5. OpenCV - Just for the continious image and To draw boxes
                    6. labelimg - Just for labeling images
                    7. TensorFlow - For Tensor Analysis 
                    
 ```

### 🔑 Prerequisites

* All the dependencies and required libraries are included in the file [requirements.txt](https://raw.githubusercontent.com/KrishArul26/Motorbike-Helmet_detection-using-ssd_mobilenet_v1/main/requirements.txt)


### 📁 Data Collection & prepration

* 2000 helmet images were collected and used those images for trained the YOLOV3.
* This project has done up to 50000 epochs with error 0.08 values.

* **Labelling the images** - Generate the XML files based on original images, which means you indicate the object in images and find the coordinates of the object in the particular image. and record the information into XML files.

### 🚀 Installation

1. Clone the repo

```
git clone https://github.com/KrishArul26/Motorbike-Helmet_detection-using-YOLOV3.git

```

2. Change your directory to the cloned repo

```
cd Motorbike-Helmet_detection-using-YOLOV3
```


3. Create a Python 3.6 version of  virtual environment named 'motorbike' and activate it

```
pip install virtualenv

```

```
virtualenv motorbike

```

```
motorbike\Scripts\activate

```

4. Now, run the following command in your Terminal/Command Prompt to install the libraries required

```
pip install -r requirements.txt

```

### 💡 Working

1. Open terminal. Go into the cloned project directory and type the following command:

```
python motorbike_helmet_detection.py

```

### 🔑 Results 

* For this motorbike helmet detection, I used computer vision trained net work which is YOLOV3

### Testing-1

<p align="left">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/121786102-1a46bb80-cbbe-11eb-9993-34126b93e444.jpg">
  <img width="350" src="https://user-images.githubusercontent.com/74568334/121786103-1adf5200-cbbe-11eb-89ad-29d50c8332e0.jpg">
</p> 

### Testing-2

<p align="left">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/121786147-5bd76680-cbbe-11eb-9a8f-931a4eed85a3.jpg">
  <img width="350" src="https://user-images.githubusercontent.com/74568334/121786145-5b3ed000-cbbe-11eb-861f-f0d98d10f3ad.jpg">
</p> 

### Testing-3

<p align="left">
  <img width="450" src="https://user-images.githubusercontent.com/74568334/121786194-8de8c880-cbbe-11eb-943a-8bcab7581ae1.jpg">
  <img width="350" src="https://user-images.githubusercontent.com/74568334/121786192-8cb79b80-cbbe-11eb-9a0c-cbb5ffef314d.jpg">
</p> 


<h3 align="left">Further Improvements</h3>
<p style= 'text-align: justify;'> We can also develop the system to be able to extract the license plate information. In case the person is not wearing a helmet, then our system will be able to store the license plate information. And backend, it will find the registration of that license plate and send the penalty details by letter.</p>

