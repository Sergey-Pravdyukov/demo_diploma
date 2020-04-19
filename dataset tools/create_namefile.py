import os
import click
from convert_annotated_RTSD_data_to_YOLO_format import get_annotation_lines, get_all_labels

@click.command()
@click.option('--dataset_annotations_path', default='/content/demo_diploma/pruned_RTSD/detection/rtsd-d3-gt/rtsd-d3-gt_full.csv', help='Relative path to full datase toannotation files.')
@click.option('--target_dir', default='/content/demo_diploma/config', help='Path to created *.name')
def create_namefile(dataset_annotations_path, target_dir):
	annotation_lines = get_annotation_lines(dataset_annotations_path)
	labels_dict = get_all_labels(annotation_lines)
	file = open(os.path.join(target_dir, 'rtsd.names'), 'w')
	file.write('\n'.join(labels_dict.keys()))
	file.close()

if __name__=='__main__':
	create_namefile()