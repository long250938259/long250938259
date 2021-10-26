import pytest


if __name__ == "__main__":
    pytest.main(["--clean-alluredir", "-s", "pytest_test/options/test_file.py", "--alluredir", 'report'])
