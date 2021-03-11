import pytest
from reddit_module.reddit import User

def test_user_create():
    user_id = 99
    num_posts = 54
    reputation = 13
    mod_status = True
    can_post = False

    test_user = User(user_id, num_posts, reputation, mod_status, can_post)

    assert(type(test_user))