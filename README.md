# <div align="center">Data Augmentation For Object Detection</div>
Toolkit to augmentate data using six different methods

## <div align="center">Documentation</div>

### Installation
Clone repo and install [requirements.txt](https://github.com/EdgeOfAI/DataAugmentationForObjectDetection/blob/main/requirements.txt) in a
[**Python>=3.9.0**](https://www.python.org/) environment

```bash
git clone https://github.com/EdgeOfAI/DataAugmentationForObjectDetection.git  # clone
cd DataAugmentationForObjectDetection
pip3 install -r requirements.txt  # install
```
### Data augmentation

Move your images to sample/images/ folder

Move your annonation files to sample/labels/ folder

There are seven augmentation methods as optional arguments:
  - RandomHorizontalFlip
  - RandomScale
  - RandomTranslate
  - RandomRotate
  - RandomShear
  - RandomHSV
  - Sequence 

All arguments have True value and script uses all seven methods. You can remove any method by providing False value to them.


Run main.py to augmentate data
```bash
python3 main.py  # data augmentation with default parameters
```
```bash
python3 main.py --no-RandomScale  # data augmentation without RandomSclae method
```

The algorithm will take care to create all the necessary files and build the directory structure like this:
```
main_folder
│   main.py
│
└───sample
    │   
    │
    └───images
    |    │   0fdea8a716155a8e.jpg
    |    │   2fe4f21e409f0a56.jpg
    |    |   ...
    |
    └───labels
        |    0fdea8a716155a8e.txt
        |    2fe4f21e409f0a56.txt
        |    ...
    │   
    │
    └───generated_images
    |    │   0fdea8a716155a8e_HorizontalFlip.jpg
    |    │   0fdea8a716155a8e_RandomScale.jpg
    |    |   ...
    |
    └───generated_labels
        |    0fdea8a716155a8e_HorizontalFlip.txt
        |    0fdea8a716155a8e_RandomScale.txt
        |    ...
```  
