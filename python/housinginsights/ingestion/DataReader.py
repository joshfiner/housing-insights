from collections import Counter
from csv import DictReader
from argparse import ArgumentParser

class DataReader(object):

    def __init__(self, path):
        self.path = path
        self ._length = None
        self. _counter = None

    def __iter__(self):
        self._length = 0
        self._counter = Counter()
        with open(self.path, 'rU') as data:
            reader = DictReader(data)
            for row in reader:
                self._length += 1
                # Nlihc_id is for the parcel.csv
                self._counter[row['Nlihc_id']] += 1
                yield row

    def __len__(self):
        if self._length is None:
            for row in self: continue ## Read data for length and counter
        return self._length

    @property
    def counter(self):
        if self._counter is None:
            for row in self: continue
        return self._counter

    @property
    def items(self):
        return self.counter.keys()

    def reset(self):
        """
        In case it breaks in the middle of reading the file
        :return:
        """
        self._length = None
        self._counter = None

if __name__ == "__main__":
    parser = ArgumentParser(description='Process some data')
    parser.add_argument('source', help='The location of the source file')
    arguments = parser.parse_args()
    if arguments.source:
        reader = DataReader(arguments.source)
        items = reader.items
        print("Items: {}".format(len(items)))