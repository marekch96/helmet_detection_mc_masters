import os

#code source:  https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide/tree/master

helmet_id = '/m/0zvk5' 
motorcycle_id = '/m/04_sv'  #general classes for box detection. id's from csv file  

#official csv files from open images v7 website separated to train, validation and test. source:   https://storage.googleapis.com/openimages/web/download_v7.html


train_bboxes_filename = os.path.join('.', 'oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('.', 'validation-annotations-bbox.csv')
#test_bboxes_filename = os.path.join('.', 'test-annotations-bbox.csv')  different dataset to be used for testing 



image_list_file_path = os.path.join('.', 'image_list_file')
#creates list of images in txt format prior using downloaded.py from google api 

#split/image_id see source for more info:  https://storage.googleapis.com/openimages/web/download_v7.html

image_list_file_list = []
for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename]): 
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            if (class_name in [helmet_id] or class_name in [motorcycle_id]) and id not in image_list_file_list:
                image_list_file_list.append(id)
                with open(image_list_file_path, 'a') as fw:
                    fw.write('{}/{}\n'.format(['train', 'validation'][j], id))
            line = f.readline()

        f.close()

#update