import pdb

import sys   #reload()之前必须要引入模块
# reload(sys)
# sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    lines = []
    with open('resources/datasets/turkcorpus/turkcorpus.test.complex', 'r', encoding='utf-8') as f:
    # with open('resources/datasets/wikicorp/wikicorp.train.complex.txt', 'r', encoding='utf-8') as f:
         for line in f.readlines():
            print(line)
    # pdb.set_trace()
    a = 1