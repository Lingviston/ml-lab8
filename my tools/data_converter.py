import csv
import argparse


def convert_data_to_libsvm_format(input_file_path, output_file_path):
  with open(input_file_path) as input, open(output_file_path, 'w', newline="\n", encoding="utf-8") as output:
    reader = csv.reader(input, delimiter=',')
    writer = csv.writer(output, delimiter=' ')
    
    for input_row in reader:
      output_row = list()
      output_row.append(input_row[57]) # moving class value to the beginning
      for idx, attribute in enumerate(input_row[:-1]):
        if float(attribute) != 0:
          output_row.append(str(idx + 1) + ":" + attribute)
      writer.writerow(output_row)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Get file names')
  parser.add_argument("input", type=str, help="An input filename")
  parser.add_argument("output", type=str, help="An output filename")
  args = parser.parse_args()
  
  convert_data_to_libsvm_format(args.input, args.output)