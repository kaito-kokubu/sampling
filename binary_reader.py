from distutils import errors
import os
import datetime


def dfs(dir):
    if os.path.isfile(dir):
        print(dir)
        read_binary(dir)
        print('\n')
    else:
        dir_list = os.listdir(dir)
        next_dir_list = [os.path.join(dir, f) for f in dir_list]
        for next_dir in next_dir_list:
            dfs(next_dir)

        
def read_binary(file):
    with open(file, encoding='utf8', errors='ignore') as f:
        data = f.read()
        #print(data)
def main():
    init_dir = os.path.expanduser('~')
    os.chdir(init_dir)
    dir_list = os.listdir(path='.')
    next_dir_list = [os.path.join(init_dir, f) for f in dir_list]
    for dir in next_dir_list:
        dfs(dir)


if __name__ == '__main__':
    print(f"exec time: {datetime.datetime.now()}")
    main()
    print(f"exec time: {datetime.datetime.now()}")
