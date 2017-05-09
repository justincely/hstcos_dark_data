for item in ls *_rawtag_a.fits
do
    calcos -o out $item
    rm -f out/*_flt_*.fits
    rm -f out/*_counts_*.fits
done
