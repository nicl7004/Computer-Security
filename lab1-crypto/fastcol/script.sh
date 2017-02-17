#!/bin/bash

./fastcoll -p prefix  -o col1 col2
cat col1 suffix > newfile1.py; cat col2 suffix > newfile2.py
python newfile1.py
python newfile2.py 
