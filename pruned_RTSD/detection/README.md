# Pruned Russian Traffic Sign Dataset

Takes only 100 frames and corresponding annotation files from original RTSD detection rtsd-d1-* directories. 
Moreover annotation files directory format was changed due to run this pruned dataset on YOLOv3 model. 
In more details original dataset has format (filename,x_from,y_from,width,height,sign_class) which contains annotations of all images in one place.
YOLOv3 format supposed to maintain two parallel directories for images and annotation files. I.e. files should have names like ./images/*.jpg and ./labels/*.txt .
Besides that internal annotation collumns' order was changed. 
Now it looks like (class_id, x_center, y_center, width, height) where x_center, y_center, width and height are normalized values with respect to real image's width and height, i.e. all this values belong to [0, 1].
