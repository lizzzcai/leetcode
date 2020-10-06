


class Array:
    """
    Achieve an Array by Python list
    """
    def __init__(self, size = 32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        """
        Get items
        :param index: get a value by index
        :return: value
        """
        return self._items[index]

    def __setitem__(self, index, value):
        """
        set item
        :param index: giving a index you want to teset
        :param value: the value you want to set
        :return:
        """
        self._items[index] = value

    def __len__(self):
        """
        :return: the length of array
        """
        return self._size

    def clear(self, value=None):
        """
        clear the Array
        :param value: set all value to None
        :return: None
        """
        for i in range(self._size):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item