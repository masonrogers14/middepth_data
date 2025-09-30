for k in {0..2}
do

for l in {0..3}
do

for g in {0..2}
do

rsync -aruv --exclude='*.data' --exclude='*.meta' --exclude='STD*' --exclude='std*' --exclude='core*' ../2pt_wall/k1t2l0/ k${k}l${l}g${g}/

done
done
done
