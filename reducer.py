#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
current_date = None
current_tempature = 0
max_tempature = -9999
  
# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    date, temperature, quality = line.split('\t', 2)
    # convert count (currently a string) to int
    try:
        quality = int(quality)
        temperature = int(temperature)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    # filter
    if quality not in [0, 1, 4, 5, 9]:
        continue
    if temperature == 9999:
        continue
    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: date) before it is passed to the reducer
    if current_date == date:
        max_tempature = max(max_tempature, temperature)
    else:
        if current_date:
            print ('%s\t%s' % (current_date, max_tempature))
        current_date = date
        max_tempature = temperature

  
# do not forget to output the last word if needed!
if current_date == date:
    print('%s\t%s' % (current_date, max_tempature))