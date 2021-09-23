import pytest
from inspiration.api.payloads import MessageToSkill, AnswerToUser, RequestData, ResponseData

MESSAGE_TO_SKILL = {
    "type": "MESSAGE_TO_SKILL",
    "payload": {
        "original_text": "Какая погода в Омске?"
    },
    "UUID": "4221",
    "status": 200
}

REQUEST_DATA = {
    "type": "REQUEST_DATA",
    "payload": {
        "type": "get_weather",
        "city": "Omsk",
        "country": "Russia"},
    "UUID": "4221",
    "status": 200
}

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
    "status": 200
}

ANSWER_TO_USER = {
    "type": "ANSWER_TO_USER",
    "UUID": "4221",
    "payload": {
        "items": [
            {"text": "В Омске -23, ппц холодно"},
            {"text": "Чел, сиди лучше дома..."}
        ]
    },
    "status": 200
}


class TestMessageToSkill:
    @staticmethod
    def response():
        return MessageToSkill(**MESSAGE_TO_SKILL)

    def test_get_uuid(self):
        assert "4221" == self.response().UUID

    def test_get_original_text(self):
        assert "Какая погода в Омске?" == self.response().payload["original_text"]

    def test_get_type_message(self):
        assert "MESSAGE_TO_SKILL" == self.response().type

    def test_get_status(self):
        assert 200 == self.response().status


class TestAnswerToUser:
    @staticmethod
    def response():
        return AnswerToUser(**ANSWER_TO_USER)

    def test_get_uuid(self):
        assert "4221" == self.response().UUID

    def test_get_status(self):
        assert 200 == self.response().status

    def test_get_item_0(self):
        assert "В Омске -23, ппц холодно" == self.response().payload['items'][0]['text']

    def test_get_item_1(self):
        assert "Чел, сиди лучше дома..." == self.response().payload['items'][1]['text']

    def test_get_type_message(self):
        assert "ANSWER_TO_USER" == self.response().type


class TestRequestData:
    @staticmethod
    def response():
        return RequestData(**REQUEST_DATA)

    def test_get_uuid(self):
        assert "4221" == self.response().UUID

    def test_get_status(self):
        assert 200 == self.response().status

    def test_get_type_message(self):
        assert "REQUEST_DATA" == self.response().type

    def test_get_service_type(self):
        assert "get_weather" == self.response().payload['type']

    def test_get_service_city(self):
        assert "Omsk" == self.response().payload['city']


class TestResponseData:
    @staticmethod
    def response():
        return ResponseData(**RESPONSE_DATA)

    def test_get_uuid(self):
        assert "4221" == self.response().UUID

    def test_get_status(self):
        assert 200 == self.response().status

    def test_get_type_message(self):
        assert "RESPONSE_DATA" == self.response().type

    def test_get_service_type(self):
        assert "get_weather" == self.response().payload['type']

    def get_temperature(self):
        assert "-23" == self.response().payload['temperature']
