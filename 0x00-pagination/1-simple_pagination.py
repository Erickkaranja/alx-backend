#!/usr/bin/env python3
'''pagination implementation.'''

import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''simple pagination implemention function.'''
    start_index: int = page_size * page - page_size
    end_index: int = page_size * page
    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''creating a get page function.'''
        data = []
        data_index = index_range(page, page_size)
        try:
            if (isinstance(page, int) and isinstance(page_size, int)):
                dataset = self.dataset()
                for i in range(data_index[0], data_index[1]):
                    element = dataset[i]
                    data.append(element)
            return data
        except IndexError:
            return []
