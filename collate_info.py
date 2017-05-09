import glob
import json
from copy import deepcopy

import numpy as np
from astropy.table import Table
from astropy.time import Time

from cos_monitoring import dark
from cos_monitoring.dark import solar

import pdb

solar.get_solar_data("./")

data = Table.read('solar_flux.txt', format='ascii')

all_info = []

for item in glob.glob("new/*_corrtag_c.fits") + glob.glob('out/*_corrtag_?.fits'):
    print(item)

    for item in dark.pull_orbital_info(item, step=700):

        try:
            darkrate = item['dark']
        except KeyError:
            continue

        t = Time(item['date'], format='decimalyear').mjd
        index = np.argmin(abs(data['col1'] - t))


        item['fsol'] = float(data['col2'][index])

        print(item)

        #if darkrate < 2e-6:
        #    continue

        all_info.append(deepcopy(item))

with open('./orbital_info.json', 'w') as out:
    json.dump(all_info, out, sort_keys=False, indent=4, separators=(',', ': '))

