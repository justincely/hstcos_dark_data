for item in ls *_rawtag.fits
do
    calcos -o new $item
    rm -f out/*_flt_*.fits
    rm -f out/*_counts_*.fits
done
