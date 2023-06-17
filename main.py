import requests
from googleapiclient.discovery import build
from google.oauth2 import service_account
"""
перед использование прочесть инструкцию!!!!
"""


login = "Введите логин сайта edu"
password = "Введите пароль сайта edu"
calendar = "Введите идентификатор календаря google пример: " \
           "b90c8ea61e34c0fe706f9d1fdaeda2615043883f4eeaee0cdd6257b79a7ac374@group.calendar.google.com"


def hex_to_number(hex_color):
    hex_color = hex_color.lstrip('#')
    decimal_color = int(hex_color, 16)
    number = decimal_color % 11 + 1
    return number


def get_token():
    token1 = requests.post("https://edu.donstu.ru/api/tokenauth",
                           json={"userName": f"{login}", "password": f"{password}", "isParent": "false"})
    t = token1.json()
    token = t["data"]["data"]["accessToken"]
    return token


def get_schedule():
    params = {"educationSpaceID": "4", "equals": "true", "description": "", "enabled": "true"}
    token = f"Bearer {get_token()}"
    headers = {"Authorization": token}
    sh1 = requests.get("https://edu.donstu.ru/api/RaspManager", params=params, headers=headers)
    sh = sh1.json()
    add_schedule_to_google_calendar(sh)


def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = 'schedule-390011-d440850030d8.json'
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)
    return service


def create_event(service, start_time, end_time, summary, location, theme, teacher, color_id, calendar_id):
    event = {
        'summary': summary,
        'location': location,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Europe/Moscow',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Europe/Moscow',
        },
        'colorId': color_id,
        'description': f"Teacher: {teacher}\nTheme: {theme}",
    }
    event = service.events().insert(calendarId=calendar_id, body=event).execute()


def delete_events(service, calendar_id):
    events = service.events().list(calendarId=calendar_id).execute()
    for event in events['items']:
        service.events().delete(calendarId=calendar_id, eventId=event['id']).execute()


def add_schedule_to_google_calendar(sh):
    service = authenticate()
    calendar_id = calendar

    delete_events(service, calendar_id)

    for item in sh['data']['raspList']:
        name = item['name']
        start = item['start']
        end = item['end']
        aud = item['info']['aud']
        teacher = item['info']['teachersNames']
        theme = item['info']['theme']
        color = item["color"]
        color_id = hex_to_number(color)
        print(color_id)

        create_event(service, start, end, name, aud, theme, teacher, color_id, calendar_id)


get_schedule()
