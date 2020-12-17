#!/usr/bin/env python3

import checksum_speed_tests


def test_crc_easy():
    crc_check = checksum_speed_tests_cron.crc('sample_file.mkv')
    assert crc_check == '6ed2a568'


def test_crc_med():
    crc_check = checksum_speed_tests_cron.crc('/dummy_directory/no_file/')
    assert crc_check is None


def test_crc_med2():
    crc_check = checksum_speed_tests_cron.crc('')
    assert crc_check is None


def test_md5_easy():
    md5_check = checksum_speed_tests_cron.md5('sample_file.mkv')
    assert md5_check == '6f56b883a687dfb69266d3ed5299e937'


def test_md5_med():
    md5_check = checksum_speed_tests_cron.md5('/dummy_directory/no_file/')
    assert md5_check is None


def test_md5_med2():
    md5_check = checksum_speed_tests_cron.md5('')
    assert md5_check is None
