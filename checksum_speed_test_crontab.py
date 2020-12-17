'''
Actions of the script:
1. Iterates through path list, stored in paths variable, and checks path is legitimate.
2. For each path it iterates through the files within it (there is no check here for media type).
3. The script creates a filepath variable for each file, and runs a size check against it, in MB.
4. Passes the filepath to the crc() and md5() functions using timeit to record the duration taken.
    crc(file):
    i. Opens the media file read only in bytes.
    ii. Passes to zlib.crc32 in buffersizes of 65536 until the total file has been evaluated.
    iii. Returns the CRC32 checksum, formatted 08x.
    md5(file):
    i. Opens the input file in read only bytes.
    ii. Splits the file into chunks, iterates through 4096 bytes at a time.
    iii. Returns the MD5 checksum, formatted hexdigest.
5. Outputs to log the following data, tab separated:
   Filepath     MD5/CRC32      Size in MB      Time taken in seconds       Python version

Joanna White 2020
Python 2.7+ and 3 compliant
'''

import os
import zlib
import hashlib
import timeit
import logging

# Setup logging
logger = logging.getLogger('checksum_speed_tests_crontab')
hdlr = logging.FileHandler('/add_your_path_here/checksum_speed_tests_crontab.log')
formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

paths = [
         '/mnt/add_your_path_here_1/checksum_test/',
         '/mnt/add_your_path_here_1/checksum_test/'
        ]


def crc(file):
    '''
    Zlib code
    '''
    try:
        with open(file, 'rb') as afile:
            buffersize = 65536
            buffr = afile.read(buffersize)
            crcvalue = 0
            while len(buffr) > 0:
                crcvalue = zlib.crc32(buffr, crcvalue)
                buffr = afile.read(buffersize)
        return format(crcvalue & 0xFFFFFFFF, '08x')

    except Exception:
        return None


def md5(file):
    '''
    Hashlib code
    '''
    try:
        hash_md5 = hashlib.md5()
        with open(file, "rb") as fname:
            for chunk in iter(lambda: fname.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    except Exception:
        return None


def main():
    for path in paths:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    filepath = os.path.join(root, file)
                    size = os.stat(filepath)
                    size_mb = int(size.st_size / (1024*1024))
                    # CRC32 Speed tests start here
                    crc_time = timeit.timeit(lambda: crc(filepath), number=1)
                    # MD5 Speed tests start here
                    md5_time = timeit.timeit(lambda: md5(filepath), number=1)
                    logger.info("%s\t CRC32\t %s\t %s\t Python version", filepath, size_mb, crc_time)
                    logger.info("%s\t MD5\t %s\t %s\t Python version", filepath, size_mb, md5_time)


if __name__ == '__main__':
    main()
