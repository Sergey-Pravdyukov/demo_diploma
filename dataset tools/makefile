images_prefix=/content/demo_diploma/RTSD-d2/detection/rtsd-d2-frames/images
labels_prefix=/content/demo_diploma/RTSD-d2/detection/rtsd-d2-frames/labels
namefile_home=/content/demo_diploma/config

all: convert

convert:
	@echo "Execute convert_annotated_RTSD_data_to_YOLO_format.py"
	python3 convert_annotated_RTSD_data_to_YOLO_format.py
	rm -rf $(labels_prefix)/*/txt

# Run this target strictly before 'convert' target.
# Example: make imgfiles TYPES="test train val"
imgfiles:
	@echo "Create $${TYPES} imgfiles."
	for type in ${TYPES} ; do \
		ls ${labels_prefix}/$${type} > ${labels_prefix}/$${type}.txt ; \
		sed -i -e "s#^#${labels_prefix}/$${type}/#" ${labels_prefix}/$${type}.txt ; \
	done

# Run this target strictly before 'convert' target.
namefile:
	@echo "Create rtsd.name for dataset"
	python3 create_namefile.py

# Run this target strictly before 'convert' target.
datafile:
	@echo "Create rtsd.data for dataset"
	python3 create_datafile.py

clean:
	@echo "Cleaning up created annotations"
	rm -rf $(labels_prefix)/test/* $(labels_prefix)/train/* $(labels_prefix)/val/*
	@echo "Cleaning up created imgfiles"
	rm -f $(labels_prefix)/*.txt
	@echo "Cleaning up created namefile"
	rm -f $(namefile_home)/*.name
	@echo "Cleaning up created datafile"
	rm -f $(namefile_home)/*.data

