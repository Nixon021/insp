from typing import Dict
from pydantic import BaseModel


class Default(BaseModel):
    """Контракт по умолчанию"""
    type: str
    UUID: str
    payload: Dict
    status: int


"""
Блок контракта ANSWER_TO_USER - ответ пользователю
"""


class AnswerPayload(BaseModel):
    """Тело контракта answer to user"""
    items: list


class AnswerToUser(Default):
    """Тип контракта ANSWER_TO_USER"""
    payload = AnswerPayload


"""
Блок контракта MESSAGE_TO_SKILL - запрос в маршрутизатор
"""


class MessageToSkillPayload(BaseModel):
    """Тело контракта MESSAGE_TO_SKILL"""
    original_text: str


class MessageToSkill(Default):
    """Тип контракта MESSAGE_TO_SKILL"""
    payload = MessageToSkillPayload


"""
Блок контракта REQUEST_DATA - запрос в вспомогательный сервис
"""


class RequestDataPayload(BaseModel):
    """Тело контракта REQUEST_DATA"""
    type: str


class RequestData(Default):
    """Тип контракта REQUEST_DATA"""
    payload = RequestDataPayload


"""
Блок контракта RESPONSE_DATA - ответ от вспомогательного сервиса
"""


class ResponseDataPayload(BaseModel):
    """Тело контракта RESPONSE_DATA"""
    type: str


class ResponseData(Default):
    """Тип контракта RESPONSE_DATA"""
    payload = ResponseDataPayload

