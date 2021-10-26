import pytest
import os
import sys
from  ks_login import load_log
log = load_log.Log()


class TbpRunner(object):


    def run(self, path=None, run_args=None, case_mark=None):
        if path:
            work_runner = []
            path_list = path.split(",")
            work_runner.append("-s")
            if case_mark:
                work_runner.append("-m=%s" % case_mark)
            for i in path_list:
                work_runner.append(i)
            work_runner.append("--alluredir")
            work_runner.append("report")
            print(work_runner)
            pytest.main(work_runner)
        else:
            pytest.main(["-s",
                         "pytest_test/options",
                         "--alluredir", "report"])





if __name__ == "__main__":
    try:
        work_path = sys.argv[1]
    except Exception as e:
        log.error(e.args)
        work_path = None

    run = TbpRunner()
    run.run(path=work_path)


    # pytest.main(["--clean-alluredir", "-s", "pytest_test/options/test_file.py", "--alluredir", 'report'])

