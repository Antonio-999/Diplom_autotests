#АНТОН ТИМОШИН, 37 когорта - Финальный проект. Инженер по тестированиваю плюс

import sender_stand_request
import data

def test_create_order():
    create_response = sender_stand_request.create_order(data.order_data)
    assert create_response.status_code == 201  
    track = create_response.json()["track"]  

