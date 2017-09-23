for d in */; do
    echo "$d"
    cd $d
    bash clean.sh
    cd ..
done
