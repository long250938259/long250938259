import pytest

def pytest_configure(config):
    marker_list = ["transfer", "critical", "P2"]
    for markers in marker_list:
        config.addinivalue_line("markers", markers)