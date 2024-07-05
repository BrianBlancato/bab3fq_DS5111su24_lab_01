import platform


# Test type of oeprating system
def test_operating_system():
    # Given the current operating system and expected os
    # When the current os is compared to the expected os
    # Then the current os should be equal to the expected os of Linux
    expected_os = 'Linux'
    current_os = platform.system()
    assert current_os == expected_os, f"Tests were not run on {expected_os}. Current OS: {current_os}"


# Test the python version
def test_python_version():
    # Given the expected python version
    # When the current python version is pulled
    # Then the current python version should be equal to the expected python version of 3.10.12
    expected_version = "3.10.12"
    current_version = platform.python_version()
    assert current_version == expected_version, f"Tests were not run on Python {expected_version}. Current Python version: {current_version}"