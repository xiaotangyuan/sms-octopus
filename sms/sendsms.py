from nameko.standalone.events import event_dispatcher


rabbitinfo = {
	'RABBIT_USER': 'guest',
	'RABBIT_PASSWORD': 'guest',
	'RABBIT_HOST': '192.168.5.105',
	'RABBIT_PORT': '5672',
}


AMQP_URI = 'pyamqp://{RABBIT_USER}:{RABBIT_PASSWORD}@{RABBIT_HOST}:{RABBIT_PORT}'.format(**rabbitinfo)
nameko_config = {
	'AMQP_URI': AMQP_URI
}

dispatcher = event_dispatcher(nameko_config)


if __name__ == '__main__':
	mobile = '137'
	msg = '123456'
	info = {
		'mobile': mobile,
		'msg': msg,
	}
	dispatcher('sms', 'checkcode', info)
