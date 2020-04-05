labels_prefix=../pruned_RTSD/detection/rtsd-d1-frames/labels

all: convert

convert:
	@echo "Execute convert_annotated_RTSD_data_to_YOLO_format.py"
	python3 convert_annotated_RTSD_data_to_YOLO_format.py
	rm -rf $(labels_prefix)/*/txt

create_imgfiles:  
	for type in ${TYPES} ; do \
		ls ${labels_prefix}/$${type} > ${labels_prefix}/$${type}.txt ; \
		sed -i -e "s#^#${labels_prefix}/$${type}/#" ${labels_prefix}/$${type}.txt ; \
	done

clean:
	@echo "Cleaning up created annotations"
	rm -rf $(labels_prefix)/test/* $(labels_prefix)/train/* $(labels_prefix)/val/*
	@echo "Cleaning up created imgfiles"
	rm -f $(labels_prefix)/*.txt
