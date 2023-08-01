import os
import shutil

#code source:  https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide/tree/master

DATA_ALL_DIR = os.path.join('.', 'data')

DATA_OUT_DIR = os.path.join('.', 'data_yolov8_format')

for set_ in ['train', 'validation']:
    for dir_ in [os.path.join(DATA_OUT_DIR, set_),
                 os.path.join(DATA_OUT_DIR, set_, 'images'),
                 os.path.join(DATA_OUT_DIR, set_, 'annotations')]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.mkdir(dir_)

helmet_id = '/m/0zvk5'
motorcycle_id = '/m/04_sv'  #general classes for box detection. id's from csv file  


train_bboxes_filename = os.path.join('.', 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('.', 'validation-annotations-bbox.csv')
#test_bboxes_filename = os.path.join('.', 'test-annotations-bbox.csv')


for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename]):
    set_ = ['train', 'validation'][j]
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if class_name in [helmet_id]:
                if not os.path.exists(os.path.join(DATA_OUT_DIR, set_, 'images', '{}.jpg'.format(id))):
                    shutil.copy(os.path.join(DATA_ALL_DIR, '{}.jpg'.format(id)),
                                os.path.join(DATA_OUT_DIR, set_, 'images', '{}.jpg'.format(id)))
                with open(os.path.join(DATA_OUT_DIR, set_, 'annotations', '{}.txt'.format(id)), 'a') as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1

                    f_ann.write('0 {} {} {} {}\n'.format(xc, yc, w, h)) #0 class helmet
                    f_ann.close()
            if class_name in [motorcycle_id]:
                if not os.path.exists(os.path.join(DATA_OUT_DIR, set_, 'images', '{}.jpg'.format(id))):
                    shutil.copy(os.path.join(DATA_ALL_DIR, '{}.jpg'.format(id)),
                                os.path.join(DATA_OUT_DIR, set_, 'images', '{}.jpg'.format(id)))
                with open(os.path.join(DATA_OUT_DIR, set_, 'annotations', '{}.txt'.format(id)), 'a') as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1

                    f_ann.write('1 {} {} {} {}\n'.format(xc, yc, w, h)) #1 class motorcycle
                    f_ann.close()

            line = f.readline()
