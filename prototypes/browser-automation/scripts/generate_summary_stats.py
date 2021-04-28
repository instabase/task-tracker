import argparse
import pandas


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', required=True, help='path to results file')
  args = parser.parse_args()
  df = pandas.read_csv(args.path, header=0, names=['index', 'latency', 'success'])
  print(f'Success rate: {df.success.mean()}')
  print(f'Latency for passing runs: {df.loc[df.success].latency.mean()}')
  print(f'Latency for failing runs: {df.loc[~df.success].latency.mean()}')  
