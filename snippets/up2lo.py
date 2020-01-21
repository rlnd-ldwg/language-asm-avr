#!/usr/bin/python
''' converts AVR assembler instruction to lower case
    copyright (c) January 2020 Roland Ludwig

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''

import sys
import re
import string

Keywords = ["ADC", "ADD", "ADIW", "AND", "ANDI", "ASR", "BCLR", "BLD", "BRBC", "BRBS", "BRCC", "BRCS", "BREAK", "BREQ", "BRGE", "BRHC", "BRHS", "BRID", "BRIE", "BRLO", "BRLT", "BRMI", "BRNE", "BRPL", "BRSH", "BRTC", "BRTS", "BRVC", "BRVS", "BSET", "BST", "CALL", "CBI", "CBR", "CLC", "JMP"]

print '\nConverting to lower case v.0.1.0 January \'20\n'

if len(sys.argv) < 3:
    print 'Missing parameters\nusage : ' + sys.argv[0] + ' <source> <target>\n'
    quit()
print 'converting ' + sys.argv[1] + ' to ' + sys.argv[2] + '...\n'
infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'w')
count = 0
keyword = ""
for dummy in infile:
    line = dummy.rstrip()
    if line.find("prefix") == 4:
        count += 1
        start = line.find('"')
        end = line.rfind('"')
        keyword = line[start+1:end]
        if keyword.upper() not in Keywords:
            keyword = ""
# change the following line to convert back to upper case
#    line = line.replace(keyword, keyword.upper())
    line = line.replace(keyword, keyword.lower())
    outfile.write('%s\r\n' % line)
    if line.find("'''") == 4:
        keyword=""
print ("%d Keywords changed." % count)
infile.close()
outfile.close()
