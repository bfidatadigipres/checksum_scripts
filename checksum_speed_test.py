"""
Actions of the script:
1. Checks the path input is legitimate, then stores sys.argv[1] as variable 'filepath'.
2. The script creates a filepath variable for each file, and runs a size check against it, in MB.
3. Passes the filepath to the crc() and md5() functions using timeit to record the duration taken.
    crc(file) both chunk sizes 4096/65536:
    i. Opens the media file read only in bytes.
    ii. Passes to zlib.crc32 in buffersizes of 65536 until the total file has been evaluated.
    iii. Returns the CRC32 checksum, formatted 08x.
    md5(file) both chunk sizes 4096/65536:
    i. Opens the input file in read only bytes.
    ii. Splits the file into chunks, iterates through 4096 bytes at a time.
    iii. Returns the MD5 checksum, formatted hexdigest.
4. Outputs to log the following data, tab separated:
   Filepath     MD5/CRC32      Size in MB      Time taken in seconds       Python version
Joanna White 2020
Python 2.7+ and 3 compliant
"""

import hashlib
import logging
import os
import sys
import timeit
import zlib

# Setup logging
logger = logging.getLogger("checksum_speed_test")
hdlr = logging.FileHandler("checksum_speed_test.log")
formatter = logging.Formatter("%(asctime)s\t%(levelname)s\t%(message)s")
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


def crc_4096(file):
    """
    Zlib code
    """
    try:
        with open(file, "rb") as afile:
            buffersize = 4096
            buffr = afile.read(buffersize)
            crcvalue = 0
            while len(buffr) > 0:
                crcvalue = zlib.crc32(buffr, crcvalue)
                buffr = afile.read(buffersize)
        return format(crcvalue & 0xFFFFFFFF, "08x")

    except Exception:
        return None


def md5_4096(file):
    """
    Hashlib code
    """
    try:
        hash_md5 = hashlib.md5()
        with open(file, "rb") as fname:
            for chunk in iter(lambda: fname.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    except Exception:
        return None


def crc_65536(file):
    """
    Zlib code
    """
    try:
        with open(file, "rb") as afile:
            buffersize = 65536
            buffr = afile.read(buffersize)
            crcvalue = 0
            while len(buffr) > 0:
                crcvalue = zlib.crc32(buffr, crcvalue)
                buffr = afile.read(buffersize)
        return format(crcvalue & 0xFFFFFFFF, "08x")

    except Exception:
        return None


def md5_65536(file):
    """
    Hashlib code
    """
    try:
        hash_md5 = hashlib.md5()
        with open(file, "rb") as fname:
            for chunk in iter(lambda: fname.read(65536), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    except Exception:
        return None


def main():
    if len(sys.argv) < 2:
        print(
            "Please remember to supply a file name to run size checks against:\npython3 checksum.py /path_to_file/video.mkv"
        )
    else:
        filepath = sys.argv[1]
        if not (os.path.isfile(filepath)):
            print("ERROR: Path not valid. Please try again.")
        else:
            size = os.stat(filepath)
            size_mb = int(size.st_size / (1024 * 1024))
            print("File {} size is {} in MegaBytes".format(filepath, size_mb))
            print("Beginning the CRC32 4096 speed test checks for your file")
            # CRC32 Speed tests 4096 start here
            crc_time = timeit.timeit(lambda: crc_4096(filepath), number=1)
            print("It took {} seconds to retrieve the CRC32 4096 hash".format(crc_time))
            print("Beginning the MD5 4096 speed test checks for your file")
            # MD5 Speed tests 4096 start here
            md5_time = timeit.timeit(lambda: md5_4096(filepath), number=1)
            print("It took {} seconds to retrieve the MD5 4096 hash".format(md5_time))
            print("Beginning the CRC32 65536 speed test checks for your file")
            # CRC32 Speed tests 65536 start here
            crc2_time = timeit.timeit(lambda: crc_65536(filepath), number=1)
            print(
                "It took {} seconds to retrieve the CRC32 65536 hash".format(crc2_time)
            )
            print("Beginning the MD5 65536 speed test checks for your file")
            # MD5 Speed tests 65536 start here
            md52_time = timeit.timeit(lambda: md5_65536(filepath), number=1)
            print("It took {} seconds to retrieve the MD5 65536 hash".format(md52_time))
            print(
                "This data is being output to checksum_speed_test.log, in your working directory"
            )
            logger.info(
                "%s\t CRC32 4096\t %s\t %s\t Python <version>",
                filepath,
                size_mb,
                crc_time,
            )
            logger.info(
                "%s\t MD5 4096\t %s\t %s\t Python <version>",
                filepath,
                size_mb,
                md5_time,
            )
            logger.info(
                "%s\t CRC32 65536\t %s\t %s\t Python <version>",
                filepath,
                size_mb,
                crc2_time,
            )
            logger.info(
                "%s\t MD5 65536\t %s\t %s\t Python <version>",
                filepath,
                size_mb,
                md52_time,
            )


if __name__ == "__main__":
    main()
