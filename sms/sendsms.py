import os
import json
from nameko.standalone.events import event_dispatcher


rabbitinfo = {
	'RABBIT_USER': os.environ['RABBIT_USER'],
	'RABBIT_PASSWORD': os.environ['RABBIT_PASSWORD'],
	'RABBIT_HOST': os.environ['RABBIT_HOST'],
	'RABBIT_PORT': os.environ['RABBIT_PORT'],
}


AMQP_URI = 'pyamqp://{RABBIT_USER}:{RABBIT_PASSWORD}@{RABBIT_HOST}:{RABBIT_PORT}'.format(**rabbitinfo)
nameko_config = {
	'AMQP_URI': AMQP_URI
}

dispatcher = event_dispatcher(nameko_config)


if __name__ == '__main__':
	import sys
	mobile = sys.argv[1]
	msg = sys.argv[2]
	info = {
		'mobile': mobile,
		'msg': msg,
	}
	info = json.dumps(info)
	dispatcher('sms', 'checkcode', info)
