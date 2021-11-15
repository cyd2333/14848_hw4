#!/usr/bin/env python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys
  
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()

    # fetch date, temperature and quality
    date = line[15:23]
    temperature = line[87:92]
    quality = line[92]
    
    print('%s\t%s\t%s' % (date, temperature, quality))
        
        
