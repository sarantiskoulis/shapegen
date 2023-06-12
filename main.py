from cli import Run
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new file at the specified path')
    parser.add_argument('--shape', type=str)
    parser.add_argument('--path', type=str, help='Path of the new file to create')
    parser.add_argument('--draw', action='store_true' ,help='Draw object into file')
    parser.add_argument('--delete', type=str, help='Delete file')
    args = parser.parse_args()
    print(args)
    Run(args)