import argparse
import csv
import datetime
import logging
import subprocess
import time

RESULTS_FILENAME = f"benchmark-{datetime.datetime.now()}.csv"
RUN_CMD = ["make", "run-docker"]


def run_benchmarks(n: int):
    csvfile = open(RESULTS_FILENAME, "w")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["run_number", "latency (seconds)", "succeeded?"])
    for i in range(n):
        logging.info(f"Starting run {i}")
        starting = time.time()
        try:
            subprocess.run(RUN_CMD, check=True)
            success = True
        except subprocess.CalledProcessError:
            # indicates failure (likely with timeout exception)
            success = False
        ending = time.time()
        csvwriter.writerow([i, ending - starting, success])

    # docker_run_cmd =


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", required=True, type=int)
    parser.add_argument("--log-level", dest="log_level", default="info")
    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format="[%(levelname)s] (%(module)s.%(funcName)s) %(message)s",
    )
    run_benchmarks(args.n)
