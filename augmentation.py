from data_aug.data_aug import *
from data_aug.bbox_util import *
import cv2 
import pickle as pkl
import numpy as np 
import matplotlib.pyplot as plt
from os.path import exists
from tqdm import tqdm
import os
from save_files import *

class Augmentation:
    def  __init__(self, params):
        self.params = params
    
    
    def Create(self):

        params = self.params
        print(params)
        files = os.listdir('sample/labels')
        for f in tqdm(files):
            
            filename = f.split('.')[0]
            img_name = 'sample/images/' + filename
            txt_name = 'sample/labels/' + filename


            img = cv2.imread(img_name + ".jpg")[:,:,::-1]   #opencv loads images in bgr. the [:,:,::-1] does bgr -> rgb
            # dimensions = img.shape
            
            
            # height, width, number of channels in image
            height = img.shape[0]
            width = img.shape[1]


            bboxes = []
            classes = []

            file = open(txt_name +'.txt', 'r')
            lines = file.readlines()
            for line in lines:
                line = line[:-2]
                classes.append(line.split()[0])
                box = line.split()[1:]
                for i in range(len(box)):
                    box[i] = float(box[i])
                x1 = (float(box[0]) - float(box[2]) / 2) * width   
                x2 = (float(box[0]) + float(box[2]) / 2) * width
                y1 = (float(box[1]) - float(box[3]) / 2) * height
                y2 = (float(box[1]) + float(box[3]) / 2) * height
                box = [x1, y1, x2, y2]
                # print(box)
                bboxes.append(box)
            bboxes = np.array(bboxes)
            
            ##first
            if params['RandomHorizontalFlip']:
                img_, bboxes_ = RandomHorizontalFlip(1)(img.copy(), bboxes.copy())
                savefile(classes, filename, "RandomHorizontalFlip", img_, bboxes_, img.shape)

            ###second
            if params['RandomScale']:
                img_, bboxes_ = RandomScale(0.3, diff = True)(img.copy(), bboxes.copy())
                savefile(classes, filename, "RandomScale", img_, bboxes_, img.shape)

            ###third
            if params['RandomTranslate']:
                img_, bboxes_ = RandomTranslate(0.3, diff = True)(img.copy(), bboxes.copy())
                savefile(classes, filename, "RandomTranslate", img_, bboxes_, img.shape)

            ###fourth
            if params['RandomRotate']:
                img_, bboxes_ = RandomRotate(20)(img.copy(), bboxes.copy())
                savefile(classes, filename, "RandomRotate", img_, bboxes_, img.shape)

            ###fifth
            if params['RandomShear']:
                img_, bboxes_ = RandomShear(0.2)(img.copy(), bboxes.copy())
                savefile(classes, filename, "RandomShear", img_, bboxes_, img.shape)
            
            ###sixth
            if params['RandomHSV']:
                img_, bboxes_ = RandomHSV(100, 100, 100)(img.copy(), bboxes.copy())
                savefile(classes, filename, "RandomHSV", img_, bboxes_, img.shape)

            ##seventh
            if params['Sequence']:
                seq = Sequence([RandomHSV(40, 40, 30),RandomHorizontalFlip(), RandomScale(), RandomTranslate(), RandomRotate(10), RandomShear()])
                img_, bboxes_ = seq(img.copy(), bboxes.copy())
                savefile(classes, filename, "Sequence", img_, bboxes_, img.shape)