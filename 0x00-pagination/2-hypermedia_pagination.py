#!/usr/bin/env python3
''''''

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
        '''get page that gets a given page from an offset page value.'''
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''implementing the gt hyper function.'''
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page != total_pages:
            next_page = page + 1
        else:
            next_page = None
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        result = {'page': page,
                  'page_size': page_size,
                  'data': data,
                  'next_page': next_page,
                  'prev_page': prev_page,
                  'total_pages': total_pages}

        return result

