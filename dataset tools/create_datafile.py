import click 
import os
from convert_annotated_RTSD_data_to_YOLO_format import get_annotation_lines, get_all_labels

@click.command()
@click.option('--dataset_path', default='/content/demo_diploma/RTSD-d2/detection/rtsd-d2-frames', help='Relative path to convertible dataset home dir.')
@click.option('--dataset_annotations_path', default='/content/demo_diploma/RTSD-d2/detection/rtsd-d2-gt/rtsd-d2-gt_full.csv', help='Relative path to full datase toannotation files.')
@click.option('--namefile_path', default='/content/demo_diploma/config/rtsd.names', help='Path to dataset namefile.')
@click.option('--target_dir', default='/content/demo_diploma/config', help='Path to created *.data')
def create_datafile(dataset_path, dataset_annotations_path, namefile_path, target_dir):
	datafile_args = {}

	datafile_args['classes'] = len(get_all_labels(get_annotation_lines(dataset_annotations_path)))
	datafile_args['train'] = os.path.join(dataset_path, 'images', 'train.txt')
	datafile_args['valid'] = os.path.join(dataset_path, 'images', 'val.txt')
	datafile_args['names'] = namefile_path

	file = open(os.path.join(target_dir, 'rtsd.data'), 'w')	
	for key, value in datafile_args.items():
		file.write("%s=%s\n" %(key, value))
	file.close()

if __name__=='__main__':
	create_datafile()