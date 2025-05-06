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


def test_md5_med2():
    md5_check = checksum_speed_test.md5_65536(".....")
    assert md5_check is None


def test_md5_med3():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med4():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med5():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med6():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med7():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med9():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med19():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med21():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med20():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med72():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med24():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med60():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med62():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med628hh9():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med8888():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None


def test_md5_med8899():
    md5_check = checksum_speed_test.md5_65536("")
    assert md5_check is None
