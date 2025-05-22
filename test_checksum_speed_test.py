"""help"""

#!/usr/bin/env python3

import checksum_speed_test


def test_crc_easy():
    crc_check = checksum_speed_test.crc_4096("sample_file.mkv")
    assert crc_check == "6ed2a568"


def test_crc_med():
    crc_check = checksum_speed_test.crc_65536("/dummy_directory/no_file/")
    assert crc_check is None


def test_crc_med2():
    crc_check = checksum_speed_test.crc_4096("")
    assert crc_check is None


def test_md5_easy():
    md5_check = checksum_speed_test.md5_65536("sample_file.mkv")
    assert md5_check == "6f56b883a687dfb69266d3ed5299e937"


def test_md5_med():
    md5_check = checksum_speed_test.md5_4096("/dummy_directory/no_/")
    assert md5_check is None


def test_md5_med_btoken():
    md5_check = checksum_speed_test.md5_4096(".....")
    assert md5_check is None


def test_md5_med_btoken__():
    md5_check = checksum_speed_test.md5_4096(".!!!!..")
    assert md5_check is None


def test_md5_med_btoken__1():
    md5_check = checksum_speed_test.md5_4096(".!!!!..")
    assert md5_check is None


def test_md5_med_more_of_the_same():
    md5_check = checksum_speed_test.md5_4096("...!@!..")
    assert md5_check is None
