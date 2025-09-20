from main.highest_rate import (get_highest_rated)
import pytest




def test_highest_rate_rest():
    # Arrange/Act
    restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]

    highest_rate = get_highest_rated(restaurants)

    # Assert
    assert highest_rate == {"name": "Crow's Nest", "rating": 5}

def test_highest_rate_only_one():
    # Arrange/Act
    restaurants = [{"name": "Crow's Nest", "rating": 1}]

    highest_rate = get_highest_rated(restaurants)

    # Assert
    assert highest_rate == {"name": "Crow's Nest", "rating": 1}


def test_highest_rate_empty_input():
    restaurants = []

    highest_rate = get_highest_rated(restaurants)

    assert highest_rate == None