#!/usr/bin/env python3


def chunk(list, size):
    """
    Split a list into a list of lists, each the length specified
    """
    return [list[i : i + size] for i in range(0, len(list), size)]


def remove_falsey(lst):
    """
    Removes falsey items from a list

    Falsey items include: False, '', 0, None
    """
    return list(filter(bool, lst))
