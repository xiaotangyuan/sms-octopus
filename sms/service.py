import logging

from nameko.events import event_handler
from nameko.rpc import rpc


logger = logging.getLogger(__name__)


class SmsService:

    name = 'sms'

    @rpc
    def get(self):
        return 'got it!'
