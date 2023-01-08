import cv2
import os

def savefile(classes, filename, method, img, bboxes, dimensions):
    height = dimensions[0]
    width = dimensions[1]
    new_bboxes = []
    text = ''
    for box in bboxes:
        xc = (box[2] + box[0]) / (2 * width)
        yc = (box[3] + box[1]) / (2 * height)
        w = (box[2] - box[0]) / width
        h = (box[3] - box[1]) / height
        new_bboxes.append([xc, yc, w, h])
    
    for i in range(len(new_bboxes)):
        for j in range(4):
            if new_bboxes[i][j] > 1:
                new_bboxes[i][j] = 1
            elif new_bboxes[i][j] < 0:
                new_bboxes[i][j] = 0
    i = 0
    for box in new_bboxes:
        text += str(classes[i]) + ' '
        i += 1
        text += ' ' . join([str(x) for x in box]) + '\n'
    
    file = open('sample/generated_labels/' + filename + '_' + method + '.txt', 'w')
    file.write(text)
    file.close()

    cv2.imwrite('sample/generated_images/' + filename + '_' + method + '.jpg', img)


def PrepareFolders():
    try:
        os.mkdir('sample/generated_labels')
        os.mkdir('sample/generated_images')
    except:
        ans = input('Destination folder is already exist, do you want to continue  (yes/no)')
        if(ans[0].lower() == 'n'):
            exit(0)