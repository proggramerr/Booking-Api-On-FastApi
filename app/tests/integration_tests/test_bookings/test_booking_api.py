import json

import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('room_id,date_to,date_from,status_code',[
    *[('4', '2030-05-01', '2030-05-15', 200)]*100],
)
async def test_add_and_get_booking(room_id ,date_to, date_from, status_code, authenticated_ac: AsyncClient):
    response = await authenticated_ac.post('/api/v1/bookings', params={
        "room_id":room_id,
        'date_from': date_from,
        'date_to': date_to,
    })
    assert response.status_code == status_code

async def test_get_and_delete_booking(authenticated_ac: AsyncClient):
    response = await authenticated_ac.get("/api/v1/bookings")
    print(response.text)
    existing_bookings = [booking["id"] for booking in json.loads(response.text)]
    for booking_id in existing_bookings:
        response = await authenticated_ac.delete(
            f"/api/v1/bookings/{booking_id}",
        )

    response = await authenticated_ac.get("/api/v1/bookings")
    assert len(response.json()) == 0