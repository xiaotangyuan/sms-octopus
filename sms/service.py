import logging

from nameko.events import EventDispatcher, event_handler
from nameko.events import SINGLETON
from nameko.rpc import rpc


logger = logging.getLogger(__name__)


class SmsService:

    name = 'sms'
    dispatch = EventDispatcher()

    @rpc
    def get(self):
        logging.debug('will return msg')
        return 'got it!'

    @rpc
    def request_sms(self, content):
        self.dispatch("checkcode", content)

    """
    此sendsms被装饰成一个event_handler，用于接收发送短信的请求
    """
    @event_handler('sms', 'checkcode', handler_type=SINGLETON)
    def sendsms(self, content):
        logging.debug(content)
        




