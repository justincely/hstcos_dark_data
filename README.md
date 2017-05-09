# COS Dark Analysis

Scripts and data contained here are used to prepare the underlying data of the
[Darkrate Analysis](https://justincely.github.io/hstcos_darkrates/) site.

## HST data download and re-calibration.

The input FITS datasets must be retrieved through the
[MAST data portal](https://archive.stsci.edu/hst/search.php).  Download them to
the current directory.  

Software installation:
1. Setup an anaconda environment, and install the STScI provided software suite.  
  Instructions can be found [here](http://astroconda.readthedocs.io/en/latest/)

2. Install the `subsolar` branch of [CalCOS](https://github.com/justincely/calcos/tree/subsolar) .

```bash
# Calibrated the FUV data
bash recal_fuv.sh

# Calibrate the NUV data
bash recal_nuv.sh
```

## Data extraction, combination with solar data, and output to JSON

```bash
python collate_info.py
```

The prepared dataset `orbital_info.json` can be supplied to the site mentioned
above, either locally or by uploading to the github repository.
