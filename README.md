Общение inspiration на post запросах Основные типы сообщений:
MESSAGE_TO_SKILL ANSWER_TO_USER REQUEST_DATA RESPONSE_DATA Статусы контрактов:
0 - успех 1 - данные вернулись от сервиса, но что-то пошло не так 2 - сервис не овтечает, в качестве тела - контракт в
случае ошибки

Успешное взаимодейтсвие:

- запихать UUID в редис и ограничить время жизни (5 минут например) от последнего обновления сессии в редисе
- если сессия протухает, сессию из редиса удаляем
- принятие запросов от клиента, где тело:
  MESSAGE_TO_SKILL = {
  "type": "MESSAGE_TO_SKILL",
  "payload": {
  "original_text": "Какая погода в Омске?"
  },
  "UUID": "4221",
  "status": 0 }
- Валидацию и обработку этого сообщения
- Принятие решения, в какой апп послать это сообщение
- в сторону сценария по адресу летит контракт MESSAGE_TO_SKILL.


- сценарий на той стороне принимает решение сходить за предиктивными данными о клиенте 4221 и посылает запрос в сторону
  inspiration:
  REQUEST_DATA = {
  "type": "REQUEST_DATA",
  "payload": {
  "type": "get_weather",
  "city": "Omsk",
  "country": "Russia"},
  "UUID": "4221",
  "status": 0 }

- модуль маршрутизации проводит валидацию и обработку, принимает решение сходить за даными о погоде, посылая сообщение в
  сторону сервиса weather:
  REQUEST_DATA = {
  "type": "REQUEST_DATA",
  "payload": {
  "type": "get_weather",
  "city": "Omsk",
  "country": "Russia"},
  "UUID": "4221",
  "status": 0 }

- сервис weather возвращает ответ в виде:
RESPONSE_DATA = {
    "type": "RESPONSE_DATA",
    "payload": {
        "type": "get_weather",
        "city": "Omsk",
        "country": "Russia",
        "temperature": "-23",
        "degree": "C"
    },
    "UUID": "4221",
    "status": 0
}

- inspiration, получив позитивный ответ, посылает в сторону сценария сообщение с телом:
  {
  "type": "RESPONSE_DATA",
  "payload": {
  "type": "get_weather",
  "city": "Omsk",
  "country": "Russia",
  "temperature": "-23",
  "degree": "C"
  },
  "UUID": "4221",
  "status": 0 }

- сценарий на той стороне принимает решение вернуть маршрутизатору ответ с телом:
  ANSWER_TO_USER = {
  "type": "ANSWER_TO_USER",
  "UUID": "4221",
  "payload": {
  "items": [
  {"text": "В Омске -23, ппц холодно"}, {"text": "Чел, сиди лучше дома..."}
  ]
  },
  "status": 0 }
  
- маршрутизатор принимает решение вернуть ответ клиенту:
  ANSWER_TO_USER = {
  "type": "ANSWER_TO_USER",
  "UUID": "4221",
  "payload": {
  "items": [
  {"text": "В Омске -23, ппц холодно"}, {"text": "Чел, сиди лучше дома..."}
  ]
  },
  "status": 0 }

# Установить пакет с обычными и extra-зависимостями "dev"

pip install -e '.[dev]'

# Установить пакет только с обычными зависимостями

pip install -e .

# start test from tests/

pytest -l  *.py