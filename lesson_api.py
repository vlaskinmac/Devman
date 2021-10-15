import requests
import logging


def show_weather(locations, payload, headers):
    url = 'https://wttr.in/'
    for location in locations:
        response = requests.get(
            '{}{}'.format(url, location),
            params=payload, headers=headers
        )
        response.raise_for_status()
        logging.debug(f"{response.status_code}")
        print(response.text)


def main():
    logging.basicConfig(
        level=logging.ERROR,
        filename='logs.log',
        filemode='w',
        format='%(asctime)s - [%(levelnames] - %(message)s'
    )
    HEADERS = {
        'Accept-Language': 'ru-RU,ru;'
    }
    locations = ['Лондон', 'Шереметьево', 'Череповец']
    payload = {'nTq': '', 'M': '', 'm': ''}
    try:
        show_weather(locations=locations, payload=payload, headers=HEADERS)
    except requests.exceptions.ConnectionError as exc:
        logging.error(exc)
        print(exc)


if __name__ == '__main__':
    main()