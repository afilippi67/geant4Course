#/bin/sh
echo $PWD
docker run -it --rm -p 6080:6080 -v $PWD:/jlab/work/myWork jeffersonlab/gemcinteractive:2.7
