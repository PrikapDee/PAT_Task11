from Action_chain import Action
import pytest

url = "https://jqueryui.com/droppable/"

action_obj1 = Action(url)


# test method to test open url case
def test_open_url():
    assert action_obj1.open_url() == True
    print("success : test Url pass")


# test method to check drag and drop case
def test_drag_drop():
    assert action_obj1.drag_drop() == True
    print("success : test Url pass")
