dir=${1}
datatype=${2}

ls ${dir}/${datatype} > ${dir}/${datatype}.txt
sed -i -e "s#^#${dir}/${datatype}/#" ${dir}/${datatype}.txt
