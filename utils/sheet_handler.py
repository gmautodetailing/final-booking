import datetime

bookings = {}

def is_slot_available(date, time, zone):
    key = f"{zone}_{date}_{time}"
    return key not in bookings

def save_booking(name, phone, postcode, service, date, time, zone):
    key = f"{zone}_{date}_{time}"
    bookings[key] = {
        "name": name,
        "phone": phone,
        "postcode": postcode,
        "service": service,
        "date": date,
        "time": time,
        "zone": zone
    }
