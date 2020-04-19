import csv
import os
import cv2
import numpy as np
import click
import logging

def find_labels(img_list, dataset_part, dataset_path, dataset_annotations_path):
	# print("img_list:", img_list)

	# print("dataset part:", dataset_part)
	# print("dataset psth:", dataset_path)
	# print("dataset_annotations_path:", dataset_annotations_path)
	annotation_lines = get_annotation_lines(dataset_annotations_path)
	labels_dict = get_all_labels(annotation_lines)
	# print("annotation_lines:", annotation_lines)
	img_annotations = []
	for img_name in img_list:
		found = False
		for line in annotation_lines:
			if line[0] == img_name.split('/')[-1]:
				found = True
				img_annotations.append(line)
		if not found:
			file = open(os.path.join(dataset_path, 'labels', dataset_part, (img_name.split('/')[-1])[:-3] + 'txt'), 'a')
			file.write('')
			file.close()
	# print("img_annotations:",img_annotations)
	for annotation in img_annotations:
		img_name = annotation[0]
		img = cv2.imread(os.path.join(dataset_path, 'images', dataset_part, img_name))
		converted_annotation = convert_label(annotation[-1], labels_dict) + ' ' + convert_points_to_YOLO_format(' '.join(annotation[1:-1]), img.shape[:-1])
		# print("Writing file:", os.path.join(dataset_path, 'labels', dataset_part, img_name[:-3] + 'txt'))
		file = open(os.path.join(dataset_path, 'labels', dataset_part, img_name[:-3] + 'txt'), 'a')
		file.write(converted_annotation + '\n')
		file.close()

def get_annotation_lines(dataset_annotations_path):
	annotation_lines = []
	with open(dataset_annotations_path) as annotations:
		annotations_reader = csv.reader(annotations)

		next(annotations_reader)
		next(annotations_reader)
		next(annotations_reader)
		next(annotations_reader)

		for line in annotations_reader:
			annotation_lines.append(line)
	return annotation_lines

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
	x, y, w, h = map(lambda x: int(x), annotation.split(' '))

	center_x = float(int((2 * x + w) / 2)) / total_w
	center_y = float(int((2 * y + h) / 2)) / total_h
	w = float(w) / total_w
	h = float(h) / total_h

	center_x, center_y, w, h = map(lambda x: str(x), (center_x, center_y, w, h))
	return(" ".join([center_x, center_y, w, h]))

@click.command()
@click.option('--dataset_path', default='/content/demo_diploma/pruned_RTSD/detection/rtsd-d3-frames', help='Relative path to convertible dataset home dir.')
@click.option('--dataset_annotations_path', default='/content/demo_diploma/pruned_RTSD/detection/rtsd-d3-gt/rtsd-d3-gt_full.csv', help='Relative path to full datase toannotation files.')
def convert_annotated_RTSD_data_to_YOLO_format(dataset_path, dataset_annotations_path):
	dataset_parts = ['train', 'val']
	for dataset_part in dataset_parts:
		logging.info("Finding labels for %s dataset part." % dataset_part)
		file = open(os.path.join(dataset_path, 'images', (dataset_part + '.txt')), 'r')
		img_list = file.read()
		img_list = img_list.split('\n')	
		find_labels(img_list, dataset_part, dataset_path, dataset_annotations_path) 			

if __name__ == '__main__':
	convert_annotated_RTSD_data_to_YOLO_format()
	