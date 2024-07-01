import platform


def test_operating_system():
    expected_os = 'Linux'
    current_os = platform.system()
    assert current_os == expected_os, f"Tests were not run on {expected_os}. Current OS: {current_os}"

def test_python_version():
    expected_version = "3.10.12"
    current_version = platform.python_version()
    assert current_version == expected_version, f"Tests were not run on Python {expected_version}. Current Python version: {current_version}"