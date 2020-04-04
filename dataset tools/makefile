labels_prefix=../pruned_RTSD/detection/rtsd-d1-frames/labels

all: execute

execute:
	@echo "Execute convert_annotated_RTSD_data_to_YOLO_format.py"
	python3 convert_annotated_RTSD_data_to_YOLO_format.py
	rm -rf $(labels_prefix)/*/txt

clean:
	@echo "Cleaning up created annotations"
	rm -rf $(labels_prefix)/test/* $(labels_prefix)/train/* $(labels_prefix)/val/*
