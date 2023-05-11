import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize('user_id, email, exists',[
    (1, 'test@test.com', True),
    (2, 'artem@example.com', True),
    (3, 'asdsadasdsa', False)
])
async def test_find_user_by_id(user_id, email, exists):
    user = await UsersDAO.find_by_in_id(user_id)

    if exists:
        assert user.id == user_id
        assert user.email == email

