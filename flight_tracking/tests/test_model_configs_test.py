from datetime import datetime, timedelta

datetime_now = datetime.now()

airport_data_records = [
    {"code": "AMH", "name": "Adnan Menderes Airport"},
    {"code": "IST", "name": "Istanbul Airport"},
    {"code": "TZX", "name": "Trabzon Airport"},
]


flight_data_records = [
    {"flight_number": "TK3534", "take_off": datetime_now, "landing": datetime_now + timedelta(hours=2)},
    {"flight_number": "TK6134", "take_off": datetime_now, "landing": datetime_now + timedelta(hours=3)},
    {"flight_number": "TK3534", "take_off": datetime_now, "landing": datetime_now + timedelta(days=1, hours=3)},
    {"flight_number": "TK3534", "take_off": datetime_now, "landing": datetime_now + timedelta(days=1, hours=3)},
    {"flight_number": "TK3561", "take_off": datetime_now, "landing": datetime_now + timedelta(hours=4)},
    {"flight_number": "TK3561", "take_off": datetime_now, "landing": datetime_now + timedelta(days=1, hours=4)},
]
