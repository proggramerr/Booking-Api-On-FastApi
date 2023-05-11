import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('email,password,status_code', [('kit@pes.com', 'kotopes', 200), ('kit@pes.com', 'koto2pes', 409), ('asdsa', 'kotopes', 422)])
async def test_register_user(email, password, status_code, async_client: AsyncClient):
    response = await async_client.post('/api/v1/auth/register', json={
        'email': email,
        'password': password
    })
    assert response.status_code == status_code

@pytest.mark.parametrize('email,password,status_code', [('test@test.com', 'test', 200), ('artem@example.com', 'artem', 200), ('asdsa', 'kotopes', 422)])
async def test_login_user(email, password, status_code, async_client: AsyncClient):
    responce = await async_client.post('/api/v1/auth/login', json={
        'email':email,
        'password':password
    })
    assert responce.status_code == status_code
