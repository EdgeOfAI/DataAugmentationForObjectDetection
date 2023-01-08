import argparse
from save_files import *
from augmentation import *




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Data augmentation for object detection')
    parser.add_argument('--RandomHorizontalFlip', action=argparse.BooleanOptionalAction, default=True, help='Description ')
    parser.add_argument('--RandomScale', action=argparse.BooleanOptionalAction, default=True, help='Description ')
    parser.add_argument('--RandomTranslate', action=argparse.BooleanOptionalAction, default=True, help='Description ')
    parser.add_argument('--RandomRotate', action=argparse.BooleanOptionalAction, default=True, help='Description ')
    parser.add_argument('--RandomShear', action=argparse.BooleanOptionalAction, default=True, help='Description ')
    parser.add_argument('--RandomHSV', action=argparse.BooleanOptionalAction, default=True, help='Description ')
    parser.add_argument('--Sequence',default=True, action=argparse.BooleanOptionalAction,  help='Description ')
    

    args = vars(parser.parse_args())

    #Creating folders for data
    PrepareFolders()
    #Creating augmentated data
    Augmentation(args).Create()
    