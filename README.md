<h2 align="center"> Motorbike-Helmet_detection-using-ssd_mobilenet_v1</h2>

<h3 align="left"> I built the system in such a way Firstly, It will be able to detect the motorbike after that It will detect who driving the bike finally, It will detect wheater that person is wearing a helmet or not.  For that, I have trained  SSD-Mobilenet-V1 and SSD-Mobilenet-V1 pre-trained model for detect Motorbike as well as human.</h3>


<p align="center">
  <img width="300" src="https://user-images.githubusercontent.com/74568334/121785707-a4d9eb80-cbbb-11eb-8085-14edab126732.jpg">
</p> 


<h3 align="center"> <span style="color:green">Motor Bike detection/ Helmet detection/ Person detection system built with OpenCV, Keras/TensorFlow using Deep Learning and Computer Vision concepts like SSD-mobilenet-v1</span></h3>


<p align="left">
  <img width="500" src="https://user-images.githubusercontent.com/74568334/121785810-3ba6a800-cbbc-11eb-9140-ac220fca83f0.jpg">
  <img width="300" src="https://user-images.githubusercontent.com/74568334/121785807-3a757b00-cbbc-11eb-9db7-7838ec2af5eb.jpg">
</p> 


### 🔑 Prerequisites

* All the dependencies and required libraries are included in the file [requirements.txt](https://raw.githubusercontent.com/KrishArul26/Motorbike-Helmet_detection-using-ssd_mobilenet_v1/main/requirements.txt)


### 📁 Data Collection & prepration

* 2000 helmet images were collected and used those images for trained the SSD-Mobilenet-V1.
* This project has done up to 50000 epochs with error 0.08 values.

* **Labelling the images** - Generate the XML files based on original images, which means you indicate the object in images and find the coordinates of the object in the particular image. and record the information into XML files.

### 🚀 Installation

1. Clone the repo

```
git clone https://github.com/KrishArul26/Motorbike-Helmet_detection-using-ssd_mobilenet_v1.git

```

2. Change your directory to the cloned repo

```
cd Motorbike-Helmet_detection-using-ssd_mobilenet_v1
```


3. Create a Python 3.6 version of  virtual environment named 'motorbike' and activate it

```
pip install virtualenv

```

```
virtualenv mask

```

```
mask\Scripts\activate

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

* For this motorbike helmet detection, I used computer vision trained net work which is SSD-mobilenet-v1

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

### Additional Task
<h3 align="left"> Also, we can develop the system in such a way It has to able to extract the Number plate information.  In case, the person is not wearing the helmet then our system will be able to store number plate information. And backend, It will find, Registration of that number plate and send the penalty details through the letter.</h3>

