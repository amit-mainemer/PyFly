
from seeds.FlightSeeder import get_random_time_this_week


mock_user = {
    "full_name": "jhon devops",
    "real_id": 100001,
    "password": "password1"
}

second_mock_user = {
    "full_name": "jane devops",
    "real_id": 100002,
    "password": "password2"
}


failed_password_mock_user = {
    "full_name": "yossi devops",
    "real_id": 100003,
    "password": "pass"
}


mock_country = {
    "name": "narnia",
    "code": "x0x"
}

mock_country2 = {
    "name": "atlantis",
    "code": ".^."
}

flight_date = get_random_time_this_week()



mock_flight = {
    "remaining_seats": 1,
    "date": flight_date
}