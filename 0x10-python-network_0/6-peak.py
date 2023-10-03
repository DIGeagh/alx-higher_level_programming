#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
    """Returns a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    size = len(list_of_integers)

    if size == 1:
        return list_of_integers[0]

    mid = size // 2  # Use integer division for mid-point calculation
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak

    if peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

    return find_peak(list_of_integers[mid + 1:])
