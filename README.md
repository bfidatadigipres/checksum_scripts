# BFI checksum_scripts

Checksum comparison scripts that uses Python standard library zlib and hashlib to generate CRC32 and MD5 hashes, and uses timeit to measure the speed that it takes to run each checksum pass. There are two versions that function fairly similarly and both will run on Python2.7 or Python3.

## checksum_speed_tests.py

To run the script:
`python checksum_speed_test.py /path_to_file/file.mkv`

This script allows a file to be input and tested against zlib and hashlib modules of Python to see which is quicker in generating CRC32 and MD5 checksums respectively. You can also drag/drop a file after the python script name to make sure the path is correct.

The script performs the following functions:
1. Checks the path is legitimate and present
2. If both are True it stores sys.argv[1] as variable 'filename'.
3. Makes timeit[lambda: ] calls to two functions as variables:
  crc(input):
  - Opens the file in bytes, and passes to zlib.crc32 in buffersizes of 65536 until the total file
    has been checksum evaluated. Prints the CRC32 checksum, formatted 08x
  md5(input):
  - Opens the input file in bytes, splits the file into chunks and iterates through these (size 4096)
    until the hash file is completed. Prints the MD5 checksum, formatted hexdigest.
4. Outputs the time taken for each function, along with the input file name.

Python 2.7 and 3 compliant.

## checksum_speed_tests_cron.py

Mostly identical to checksum_speed_tests.py, but with print statements removed so runs silently and appends to a log file at a specified path. To run this script you need to edit the paths variable (line 37/38) and specify a path for your log ouput (line 30). If you're testing in both Python2 and Python3 then you can also amend the version in line 87 and 88.

The script performs the following functions:
1. Iterates through path list, stored in paths variable, and checks path is legitimate.
2. For each path it iterates through the files within it (there is no check here for file type).
3. The script creates a filepath variable for each file, and runs a size check against it, in MB.
4. Passes the filepath to the crc() and md5() functions using timeit to record the duration taken.
  crc(file):
  - Opens the media file read only in bytes. Passes to zlib.crc32 in buffersizes of 65536 until the
    total file has been evaluated. Returns the CRC32 checksum, formatted 08x.
  md5(file):
  - Opens the input file in read only bytes. Splits the file into chunks, iterates through 4096
    bytes at a time. Returns the MD5 checksum, formatted hexdigest.
5. Outputs to log the following data, tab separated:
   Filepath     MD5/CRC32      Size in MB      Time taken in seconds       Python version

## test_checksum_speed_tests.py

Test script for the md5 and crc functions of checksum_speed_tests.py (written to work with cron edition which returns checksum values). This is a first attempt to work with PyTest asserts, and as such no import of pytest is required. The test script should be kept alongside the script it's testing, and you can run it (after pip installing pytest) by two methods:

cd into the folder that holds both the scripts and run:
`py.test -v`
This will run any/all scripts prefixed "test_"

Alternatively, from any directory run:
`pytest -v /path_to_script/test_checksum_speed_tests.py`
The -v requests verbosity, useful when you have multiple test functions within the one script.

Python 3 compliant.
