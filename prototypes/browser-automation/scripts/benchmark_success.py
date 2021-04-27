import argparse
import csv
import datetime
import logging
import subprocess
import time

RESULTS_FILENAME = f"benchmark-{datetime.datetime.now()}.csv"
RUN_CMD_IN_DOCKER = [
    "docker",
    "run",
    "backend-selenium",
    "python",
    "scripts/update_dob_selenium.py",
    "--new-dob",
    "11/15/1992",
]
RUN_CMD_NATIVE = ["python", "scripts/update_dob_selenium.py", "--new-dob", "01/01/1995"]


def run_benchmarks(n: int, use_docker: bool, use_chrome: bool):
    csvfile = open(RESULTS_FILENAME, "w")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["run_number", "latency (seconds)", "succeeded?"])
    RUN_CMD = RUN_CMD_IN_DOCKER if use_docker else RUN_CMD_NATIVE
    if use_chrome:
        logging.info(f"Using Chrome")
        RUN_CMD += ["--browser", "chrome"]
    else:
        logging.info(f"Using Firefox")
        RUN_CMD += ["--browser", "firefox"]
    logging.info(f"Using RUN_CMD: {RUN_CMD}")
    for i in range(n):
        starting = time.time()
        try:
            subprocess.run(RUN_CMD, check=True)
            logging.info(f"Run {i} succeeded")
            success = True
        except subprocess.CalledProcessError:
            # indicates failure (likely with timeout exception)
            logging.warning(f"Run {i} failed")
            success = False
        ending = time.time()
        csvwriter.writerow([i, ending - starting, success])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", required=True, type=int)
    parser.add_argument("--log-level", dest="log_level", default="info")
    parser.add_argument("--use-docker", dest="use_docker", action="store_true")
    parser.add_argument("--use-chrome", dest="use_chrome", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format="[%(levelname)s] (%(module)s.%(funcName)s) %(message)s",
    )
    run_benchmarks(args.n, args.use_docker, args.use_chrome)
