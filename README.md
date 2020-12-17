# BFI checksum_scripts

##checksum_speed_tests.py

New script, needs refactoring. Allows a file to be input and tested against zlib and hashlib modules of Python to see which is quicker in generating CRC32 and MD5 checksums respectively.

To use the script: python3 checksum_speed_tests.py /path_to_folder/file.mkv You can also drag/drop a file after the python script name.

main():

    It checks the path is legitimate and present
    If both are True it stores sys.argv[1] as variable 'input'.
    Makes timeit[lambda: ] calls to two functions as variables: crc(input):
        Opens the file in bytes, and passes to zlib.crc32 in buffersizes of 65536 until the total file has been checksum evaluated. Prints the CRC32 checksum, formatted 08x md5(input):
        Opens the input file in bytes, splits the file into chunks and iterates through these (size 4096) until the hash file is completed. Prints the MD5 checksum, formatted hexdigest.
    Outputs the time taken for each function, along with the input file name.

TO DO: The script functions for checksum generation need comparing to those currently used in BFI scripts. It's possible these examples may present very differently. Research into alternative checksum generation, then organise files and timings for the scripts. How might the lambda: call be slower than presenting commands as string form. Configure log file outputs, just set for print statements at the moment.

Python 2.7 and 3 compliant.
checksum_speed_tests_cron.py

Mostly identical to checksum_speed_tests.py, but with print statements removed and logging included. This script has been refactored to run from cron, so sys.argv[1] as input no longer needed. Paths list added for iteration benefits, and inputs sourced this way.
test_checksum_speed_tests.py

Test script for the md5 and crc functions of checksum_speed_tests.py (written to work with cron edition which returns checksum values). This is a first attempt to work with PyTest asserts, and as such no import of pytest is required. The test script should be kept alongside the script it's testing, and you can run it (after pip installing pytest) by two methods:

    cd into the folder that holds both the scripts and run: py.test -v This will run any/all scripts prefixed "test_"

    From anywhere run: pytest -v /path_to_script/test_checksum_speed_tests.py The -v requests verbosity, useful when you have multiple test functions within the one script.

Python 3 compliant.
