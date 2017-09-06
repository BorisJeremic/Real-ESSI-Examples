for d in */; do
    echo "$d"
    cd $d
    bash clean.sh
    cd ..
done




for d in */; do
    echo "$d"
    cd $d
    bash run.sh
    cd ..
done