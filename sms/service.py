import json
import logging

from nameko.events import EventDispatcher, event_handler
from nameko.events import SINGLETON
from nameko.rpc import rpc
from nameko.extensions import DependencyProvider

from .alidayu import send_by_alidayu


logger = logging.getLogger(__name__)


class ErrorHandler(DependencyProvider):
    def worker_result(self, worker_ctx, res, exc_info):
        if exc_info is None:
            return  # nothing to do
        exc_type, exc, tb = exc_info
        # do whatever you need with the exception here
        print(exc)


class SmsService:

    name = 'sms'
    dispatch = EventDispatcher()

    # handler = ErrorHandler()

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
        """
        这里http请求在python3.7版本有：
        wrap_socket() got an unexpected keyword argument '_context'
        报错，是eventlet和python的版本冲突，downgrade到python3.6即可。
        """
        if type(content) is not dict:
            content = json.loads(content)
        logging.debug('%s,%s'% (content['mobile'], content['msg']))
        try:
            response = send_by_alidayu(content['mobile'], content['msg'])
            response = json.dumps(response)
            logging.debug(response)
        except Exception as e:
            logging.error(e)
