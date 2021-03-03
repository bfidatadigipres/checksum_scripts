# BFI checksum_scripts

The Data and Digital Preservation team in the BFI National Archive has been running checksum speed comparisons, with an aim to reducing bottlenecks caused by an increasing volume of digital media files. One such bottleneck is caused by our use of hashlib in Python2 scripts to generate MD5 checksums for every media file before being written to LTO tape storage. We have decided to run some comparisons between CRC32 and MD5, as we currently only have support for these within our tape library system. (Ruling out the supported SHA options as we have no need for the cryptographic functionality and prefer the speed gain over that functionality).

The scripts in this repository use Python standard library zlib and hashlib to generate CRC32 and MD5 hashes respectively. They both use timeit to measure the speed that it takes to run each checksum pass. As the media files are generally many GBs in size the test repeat number is set to 1 in timeit, so the script is only run once per file, every four hours from crontab. Timeit however, was developed to create averages across multiple speed tests on short snippets of code. If you are checksum testing smaller files in a collection you can change the `number=1` setting to another figure, such as number=100 and run the test to receive an average time across those 100. Timeit's default is 1,000,000 (when no number is specified) so do ensure you set a number for checksum tests that is achievable.

There are two versions of the checksum_speed_test script that allow for single use checksum testing or automated testing of directories, and both will run on Python2.7 or Python3.

Result from the tests, run on 8 thread Ubuntu VM with 12GB RAM and 10Gbps network connection - testing with files on two different network shares: CRC32 chunk size 65536 using Python 3 (3.6 installed) implementation is fastest, with MD5 chunk size 4096 Python 2 (2.7 installed) implementation slowest.

#### Methodology | MB per Second

Tests averaged across one week of repeat testing:
 - MD5 4096 Python2 | 224.778250340242.
 - MD5 65536 Python2 | 357.535889127455.
 - MD5 4096 Python3 | 326.132731717776.
 - MD5 65536 Python3 | 398.015125290373.
 - CRC32 4096 Python2 | 265.358376013364.
 - CRC32 65536 Python2 | 546.4826626438.
 - CRC32 4096 Python3 | 348.466331006633.
 - CRC32 65536 Python3 | 609.691086005532.


## checksum_speed_test.py

This script allows for a single file to be input and tested against zlib CRC32 and hashlib MD5 modules of Python to see which is quicker. You can drag/drop a file after the python script name to make sure the path is correct.

To run the script:
`python checksum_speed_test.py /path_to_file/file.mkv`

The script performs the following functions:
1. Checks the path supplied is legitimate and present.
2. If both are True it stores sys.argv[1] (the path you supplied) as variable 'filename'.
3. Makes timeit[lambda: ] calls to the following functions supplying the filename:
  - crc_4096(filename): Opens the file in bytes, and passes to zlib.crc32 in buffersizes of 4096, until the whole of the file
    has been checksum evaluated. Prints the CRC32 checksum to the terminal output, formatted 08x.
  - crc_65536(filename): Opens the file in bytes, and passes to zlib.crc32 in buffersizes of 65536, until the whole of the file
    has been checksum evaluated. Prints the CRC32 checksum to the terminal output, formatted 08x.
  - md5_4096(filename): Opens the input file in bytes, splits the file into chunks and iterates through these (size 4096)
    until the hash file is completed. Prints the MD5 checksum, formatted hexdigest.
  - md5_65536(filename): Opens the input file in bytes, splits the file into chunks and iterates through these (size 65536)
    until the hash file is completed. Prints the MD5 checksum, formatted hexdigest.
4. Outputs the time taken for each function to terminal console. Also outputs to (or appends to if you have multiple attempts) a log
   in the current terminal directory. Tab separated: Filepath - MD5/CRC32 chunk size - Size in MB - Time taken in seconds - Python version.


## checksum_speed_test_crontab.py

Mostly identical to checksum_speed_tests.py, but with print statements removed so runs silently and appends to a log file at a specified path. To run this script you need to edit the paths variable (line 37/38) and specify a path for your log ouput (line 30). If you're testing in both Python2 and Python3 then you can also amend the version in line 87 and 88.

The script performs the following functions:
1. Iterates through path list, stored in paths variable, and checks each path is legitimate.
2. For each path it iterates through the files within it (there is no check here for file type).
3. The script creates a filepath variable for each file, and runs a size check against it, in MB.
4. Passes the filepath to the following functions using timeit to record the duration taken.
  - crc_4096(filename): Opens the file in bytes, and passes to zlib.crc32 in buffersizes of 4096, until the whole of the file
    has been checksum evaluated. Prints the CRC32 checksum to the terminal output, formatted 08x.
  - crc_65536(filename): Opens the file in bytes, and passes to zlib.crc32 in buffersizes of 65536, until the whole of the file
    has been checksum evaluated. Prints the CRC32 checksum to the terminal output, formatted 08x.
  - md5_4096(filename): Opens the input file in bytes, splits the file into chunks and iterates through these (size 4096)
    until the hash file is completed. Prints the MD5 checksum, formatted hexdigest.
  - md5_65536(filename): Opens the input file in bytes, splits the file into chunks and iterates through these (size 65536)
    until the hash file is completed. Prints the MD5 checksum, formatted hexdigest.
5. Outputs to log the following data, tab separated:
   Filepath     MD5/CRC32 chunk size      Size in MB      Time taken in seconds       Python version


## test_checksum_speed_test.py

Test script for the md5 and crc functions of checksum_speed_test scripts. This is a first attempt to work with PyTest asserts. No `import pytest` is required in this script to run the test. This test script should be kept in the same directory as the script it's testing so pytest can find it, and should have the same name as the script to be tested, name appended 'test_'.

You will need to install pytest. The easiest way is to use pip/pip3 globally or in a Virtual Environment.
(Guidance here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

`pip install pytest`

There are two ways to run a pytest. Change directory of your terminal console to the folder that holds both the scripts and run:
`py.test -v`
This will run any/all scripts prefixed "test_".

Alternatively, from any directory run:
`pytest -v /path_to_script/test_checksum_speed_test.py`
The -v requests verbosity, useful when you have multiple test functions within the one script.

Python 3 compliant, not tested on Python2.
