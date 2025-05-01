"""
Testing checksums
"""

#!/usr/bin/env python3

import checksum_speed_test


def test_crc_easy():
    """Testing code"""
    crc_check = checksum_speed_test.crc_4096("sample_file.mkv")
    assert crc_check == "6ed2a568"


def test_crc_med():
    """Testing code"""
    crc_check = checksum_speed_test.crc_65536("/dummy_directory/no_file/")
    assert crc_check is None


def test_crc_med2():
    """Testing code"""
    crc_check = checksum_speed_test.crc_4096("")
    assert crc_check is None


def test_md5_easy():
    """Testing code"""
    md5_check = checksum_speed_test.md5_65536("sample_file.mkv")
    assert md5_check == "6f56b883a687dfb69266d3ed5299e937"


def test_md5_med():
    """Testing code"""
    md5_check = checksum_speed_test.md5_4096("/dummy_directory/no_/")
    assert md5_check is None


def test_md5_med2():
    """Testing code"""
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None
