import csv
import os
import cv2
import numpy as np
import click

def find_labels(img_list, annotation_lines, dataset_part, labels_dict, dataset_path):
	img_annotations = []
	for img_name in img_list:
		found = False
		for line in annotation_lines:
			if line[0] == img_name:
				# img_annotations_line = ' '.join(line)
				found = True
				img_annotations.append(line)
		if not found:
			file = open(os.path.join(dataset_path, 'labels', dataset_part, img_name[:-3] + 'txt'), 'a')
			file.write('')
			file.close()
	for annotation in img_annotations:
		img_name = annotation[0]
		img = cv2.imread(os.path.join(dataset_path, 'images', dataset_part, img_name))
		# print("img shape:", img.shape)
		cur_annotation = convert_label(annotation[-1], labels_dict) + ' ' + convert_points_to_YOLO_format(' '.join(annotation[1:-1]), img.shape[:-1])
		# print(os.path.join(dataset_path, 'labels', dataset_part, img_name[:-3] + 'txt'))
		file = open(os.path.join(dataset_path, 'labels', dataset_part, img_name[:-3] + 'txt'), 'a')
		file.write(cur_annotation + '\n')
		file.close()
	
def get_all_labels(annotation_lines):
	labels = {}
	counter = 0
	for line in annotation_lines:
		if line[-1] not in labels:
			labels[line[-1]] = counter
			counter += 1
	return labels

def convert_label(strange_label, labels_dict):
	return str(labels_dict[strange_label])

def convert_points_to_YOLO_format(annotation, img_size):
	total_h, total_w = img_size
	x, y, w, h = annotation.split(' ')
	x, y, w, h = int(x), int(y), int(w), int(h)

	w, h = x + w, y + h
	# print("most points:", x, y, w, h)
	
	center_x = int((x + w) / 2)
	center_y = int((y + h) / 2) 
	w = abs(x - w)
	h = abs(y - h)

	# print("img size:", total_w, total_h)
	# print("like ints:", center_x, center_y, w, h)

	center_x = float(center_x) / total_w
	center_y = float(center_y) / total_h
	w = float(w) / total_w
	h = float(h) / total_h

	center_x, center_y, w, h = str(center_x), str(center_y), str(w), str(h)
	# print("floats:", center_x, center_y, w, h, '\n')
	return(center_x + ' ' + center_y + ' ' + w + ' ' + h)

@click.command()
@click.option('--dataset_path', default='../pruned_RTSD/detection/rtsd-d1-frames', help='Relative path to convertible dataset home dir.')
@click.option('--dataset_annotations_path', default='../pruned_RTSD/detection/rtsd-d1-gt/rtsd-d1-gt_full.csv', help='Relative path to full datase toannotation files.')
def convert_annotated_RTSD_data_to_YOLO_format(dataset_path, dataset_annotations_path):
	dataset_parts = ['train', 'val', 'test']
	labels_dict = {}
	annotation_lines = []

	with open(dataset_annotations_path) as annotations:
		annotations_reader = csv.reader(annotations)

		next(annotations_reader)
		next(annotations_reader)
		next(annotations_reader)
		next(annotations_reader)

		for line in annotations_reader:
			annotation_lines.append(line)
		labels_dict = get_all_labels(annotation_lines)

	for dataset_part in dataset_parts:
		file = open(os.path.join(dataset_path, 'images', dataset_part, (dataset_part + '_images.txt')), 'r')
		img_list = file.read()
		img_list = img_list.split('\n')	
		find_labels(img_list, annotation_lines, dataset_part, labels_dict, dataset_path) 			
	# # for k, v in labels_dict.items():
	# # 	print(k)

if __name__ == '__main__':
	convert_annotated_RTSD_data_to_YOLO_format()
	# convert_annotated_RTSD_data_to_YOLO_format()
	