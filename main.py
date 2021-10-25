import pytest


if __name__ == "__main__":
    pytest.main(["-s", "pytest_test/options/test_file.py", "--alluredir", 'report'])
