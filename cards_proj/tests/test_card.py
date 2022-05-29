"""Test card data class"""
from cards import Card


def test_field_access():
    card = Card("something", "brian", "todo", 123)
    assert card.summary == "something"
    assert card.owner == "brian"
    assert card.state == "todo"
    assert card.id == 123


def test_defaults():
    card = Card()
    assert card.summary is None
    assert card.owner is None
    assert card.state == "todo"
    assert card.id is None


def test_equality():
    card1 = Card("something", "brian", "todo", 123)
    card2 = Card("something", "brian", "todo", 123)
    assert card1 == card2


def test_equality_with_different_ids():
    card1 = Card("something", "brian", "todo", 123)
    card2 = Card("something", "brian", "todo", 1234)
    assert card1 == card2


def test_from_dict():
    card_dict = dict(summary="something",
                     owner="brian",
                     state="todo",
                     id=123)
    card1 = Card("something", "brian", "todo", 123)
    card2 = Card.from_dict(card_dict)
    assert card1 == card2


def test_to_dict():
    card = Card("something", "brian", "todo", 123)
    expected_card_dict = dict(summary="something",
                              owner="brian",
                              state="todo",
                              id=123)
    actual_card_dict = card.to_dict()
    assert expected_card_dict == actual_card_dict
