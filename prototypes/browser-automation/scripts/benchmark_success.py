import argparse
import csv
import datetime
import logging
import subprocess
import time

RESULTS_FILENAME = f"benchmark-{datetime.datetime.now()}.csv"
USE_DOCKER_PREFIX = ["docker", "run", "backend-browtomation"]
RUN_SELENIUM_CMD = [
    "python",
    "scripts/update_dob_selenium.py",
    "--new-dob",
    "01/01/1995",
]
RUN_PLAYWRIGHT_CMD = [
    "python",
    "scripts/update_dob_playwright.py",
    "--new-dob",
    "01/01/1995",
]


def generate_cmd(use_docker: bool, use_chrome: bool, use_playwright: bool):
    RUN_CMD = RUN_PLAYWRIGHT_CMD if use_playwright else RUN_SELENIUM_CMD
    if use_docker:
        RUN_CMD = USE_DOCKER_PREFIX + RUN_CMD
    if use_chrome:
        RUN_CMD += ["--browser", "chrome"]
    else:
        RUN_CMD += ["--browser", "firefox"]
    return RUN_CMD


def run_benchmarks(n: int, run_cmd: list, results_filename: str):
    csvfile = open(results_filename, "w")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["run_number", "latency (seconds)", "succeeded?"])
    logging.info(f"Using run_cmd: {run_cmd}")
    for i in range(n):
        starting = time.time()
        try:
            subprocess.run(run_cmd, check=True)
            logging.info(f"Run {i} succeeded")
            success = True
        except subprocess.CalledProcessError:
            # indicates failure
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
    parser.add_argument("--use-playwright", dest="use_playwright", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format="[%(levelname)s] (%(module)s.%(funcName)s) %(message)s",
    )
    run_cmd = generate_cmd(args.use_docker, args.use_chrome, args.use_playwright)
    output_filename = f"benchmark-n-{args.n}-docker-{args.use_docker}-playwright-{args.use_playwright}-chrome-{args.use_chrome}.csv"
    run_benchmarks(args.n, run_cmd, output_filename)
