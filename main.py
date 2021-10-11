import pytest


if __name__ == "__main__":
    pytest.main(["-s", "pytest_test/options/test_in_theaters.py", "--alluredir", 'report'])
