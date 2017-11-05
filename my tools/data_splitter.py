import argparse


def split_to_test_and_learn(input_file_path, learn_output_file_path, test_output_file_path, learn_size):
  with open(input_file_path) as input, open(learn_output_file_path, 'w') as learn_output, open(test_output_file_path, 'w') as test_output:
    
    lines_read = 0
    
    for input_line in input:
      if lines_read < learn_size:
        learn_output.write(input_line)
      else:
        test_output.write(input_line)
        
      lines_read += 1


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Get file names')
  parser.add_argument("input", type=str, help="Path to input file.")
  parser.add_argument("learn_output", type=str, help="Path to output file for the learn sample.")
  parser.add_argument("test_output", type=str, help="Path to output file for the test sample.")
  parser.add_argument("size", type=int, help="Learn sample size. Values will be extracted from the beginning.")
  args = parser.parse_args()
  
  split_to_test_and_learn(args.input, args.learn_output, args.test_output, args.size)