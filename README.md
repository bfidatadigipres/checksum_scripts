# BFI checksum_scripts

Checksum comparison scripts that uses Python standard library zlib and hashlib to generate CRC32 and MD5 hashes respectively. They both use timeit to measure the speed that it takes to run each checksum pass. Timeit has been used to allow multiple timing assessments on smaller files. But as the BFI's are GBs the number is set to 1 timing attempt and the script is run one per file every four hours for 24 hours. You can change the number=1 setting to another figure for smaller files, such as number=100, and you will receive an average time across those 100. Default is 1,000,000 so best not remove the number=1/100.

There are two versions of the checksum_speed_test script that function fairly similarly detailed below, and both will run on Python2.7 or Python3: 


## checksum_speed_tests.py

To run the script:
`python checksum_speed_test.py /path_to_file/file.mkv`

This script allows a file to be input and tested against zlib and hashlib modules of Python to see which is quicker in generating CRC32 and MD5 checksums respectively. You can also drag/drop a file after the python script name to make sure the path is correct.

The script performs the following functions:
1. Checks the path is legitimate and present
2. If both are True it stores sys.argv[1] as variable 'filename'.
3. Makes timeit[lambda: ] calls to two functions as variables:
  - crc(input): Opens the file in bytes, and passes to zlib.crc32 in buffersizes of 65536 until the total file
    has been checksum evaluated. Prints the CRC32 checksum, formatted 08x
  - md5(input): Opens the input file in bytes, splits the file into chunks and iterates through these (size 4096)
    until the hash file is completed. Prints the MD5 checksum, formatted hexdigest.
4. Outputs the time taken for each function, along with the input file name.


## checksum_speed_tests_cron.py

Mostly identical to checksum_speed_tests.py, but with print statements removed so runs silently and appends to a log file at a specified path. To run this script you need to edit the paths variable (line 37/38) and specify a path for your log ouput (line 30). If you're testing in both Python2 and Python3 then you can also amend the version in line 87 and 88.

The script performs the following functions:
1. Iterates through path list, stored in paths variable, and checks path is legitimate.
2. For each path it iterates through the files within it (there is no check here for file type).
3. The script creates a filepath variable for each file, and runs a size check against it, in MB.
4. Passes the filepath to the crc() and md5() functions using timeit to record the duration taken.
  - crc(file): Opens the media file read only in bytes. Passes to zlib.crc32 in buffersizes of 65536 until the
    total file has been evaluated. Returns the CRC32 checksum, formatted 08x.
  - md5(file): Opens the input file in read only bytes. Splits the file into chunks, iterates through 4096
    bytes at a time. Returns the MD5 checksum, formatted hexdigest.
5. Outputs to log the following data, tab separated:
   Filepath     MD5/CRC32      Size in MB      Time taken in seconds       Python version


## test_checksum_speed_tests.py

Test script for the md5 and crc functions of checksum_speed_test scripts. This is a first attempt to work with PyTest asserts. No import of pytest is required to run this script. This test script should be kept in the same directory as the script it's testing so pytest can find it, and should have the same name as the script to be tested, name appended 'test_'.

You will need to install pytest. Thes easiest way is to use pip, or pip3:

`pip install pytest`

There are two ways to run a pytest. Change directory of your terminal console to the folder that holds both the scripts and run:
`py.test -v`
This will run any/all scripts prefixed "test_"

Alternatively, from any directory run:
`pytest -v /path_to_script/test_checksum_speed_tests.py`
The -v requests verbosity, useful when you have multiple test functions within the one script.

Python 3 compliant, not tested on Python2.
