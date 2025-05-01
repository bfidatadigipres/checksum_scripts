#!/usr/bin/env python3

"""
Tests using sample
and dummy files
"""

import checksum_speed_test


def test_crc_easy():
    """Sample file CRC 4096"""
    crc_check = checksum_speed_test.crc_4096("sample_file.mkv")
    assert crc_check == "6ed2a568"


def test_crc_med():
    """Dummy CRC 65536"""
    crc_check = checksum_speed_test.crc_65536("/dummy_directory/no_file/")
    assert crc_check is None


def test_crc_med2():
    """Empty string CRC 4096"""
    crc_check = checksum_speed_test.crc_4096("")
    assert crc_check is None


def test_md5_easy():
    """Sample file MD5 65536"""
    md5_check = checksum_speed_test.md5_65536("sample_file.mkv")
    assert md5_check == "6f56b883a687dfb69266d3ed5299e937"


def test_md5_med():
    """Dummy MD5 4096"""
    md5_check = checksum_speed_test.md5_4096("/dummy_directory/no_file/")
    assert md5_check is None


def test_md5_med2():
    """Empty str MD5 65536"""
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None
