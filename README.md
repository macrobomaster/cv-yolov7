# Updated Version of YOLOv7 with CUDA Fix

## Description

- Integrated from yolov7 official repo https://github.com/WongKinYiu/yolov7, fixed the issue on cuda core can't run on yolov7 model. Tested on conda environment with `python3.9, pytorch=1.11.0, cudatoolkit=1.13`

## Performance 

MS COCO

| Model | Test Size | AP<sup>test</sup> | AP<sub>50</sub><sup>test</sup> | AP<sub>75</sub><sup>test</sup> | batch 1 fps | batch 32 average time |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| [**YOLOv7**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) | 640 | **51.4%** | **69.7%** | **55.9%** | 161 *fps* | 2.8 *ms* |
| [**YOLOv7-X**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt) | 640 | **53.1%** | **71.2%** | **57.8%** | 114 *fps* | 4.3 *ms* |
|  |  |  |  |  |  |  |
| [**YOLOv7-W6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6.pt) | 1280 | **54.9%** | **72.6%** | **60.1%** | 84 *fps* | 7.6 *ms* |
| [**YOLOv7-E6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6.pt) | 1280 | **56.0%** | **73.5%** | **61.2%** | 56 *fps* | 12.3 *ms* |
| [**YOLOv7-D6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-d6.pt) | 1280 | **56.6%** | **74.0%** | **61.8%** | 44 *fps* | 15.0 *ms* |
| [**YOLOv7-E6E**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt) | 1280 | **56.8%** | **74.4%** | **62.1%** | 36 *fps* | 18.7 *ms* |

## Installation on Windows 

Conda environment -- Anaconda https://www.anaconda.com/ \
Python -- Python 3.9 installed with Anaconda

### Install Anaconda
Select Installation Type : 'just me' \
Anaconda Install Location : Anywhere you want, doesn't have to be on C drive \
Advanved Installation Options : \
![image](https://user-images.githubusercontent.com/56321690/202285992-e6f95310-7aa7-4997-a186-059bd7886b8d.png)


### Clone yolov7 Repo 
Run `git clone https://github.com/FlyerJB/YOLOv7-RoboMaster.git` on your command prompt to some dir under C:/ drive or your OS drive to avoid Enviornment failure \
    
### Make Conda Environment
Open Conda Command Prompt with Admin Right \
Cd into yolov7 dir with `cd <where you clone your yolov7>` \
And craete Conda Environment
`Conda Create -n <The Name You Like> Python3.9` 

![image](https://user-images.githubusercontent.com/56321690/202287922-1a6b9a71-49ef-4d40-b759-ec4ddd641317.png)
### Activate Conda Environment
Run command `Conda activate <The Name You put from previous step>` 

### pip install required packages
Option 1 : Install yolov7 for training on CPU \
`pip install -r requirements.txt`

Option 2 : Install yolov7 for training on RTX GPU \
`pip install -r requirement_nv_gpu.txt`

### Validate Cuda Installation ( required for nv_gpu training )
Run `python` or `python3` or `py` to run python \
Run `import torch` \
Run `torch.cuda_is_available()` \
If it returns `True`, it means CUDA is successfully install on your device with Pytorch. 


## Training

With GPU training

``` shell
# train p6 models
py train.py --workers 1 --device 0 --batch-size 8 --epochs 50 --img 640 640 --data data/coco_custom.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-(the name you want) --weights yolov7.pt  
```
With CPU training

``` shell
# train p6 models
py train.py --workers 8 --device CPU --batch-size 8 --epochs 50 --img 640 640 --data data/coco_custom.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-(the name you want) --weights yolov7.pt
```

