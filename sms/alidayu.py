import os
import logging
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


accesskeyid = os.environ['alidayu_accesskeyid']
accesssecret = os.environ['alidayu_accesssecret']
signname = os.environ['alidayu_signname']
templatecode = os.environ['alidayu_templatecode']


def send_by_alidayu(mobile, msg):
	client = AcsClient(accesskeyid, accesssecret, 'cn-hangzhou')
	request = CommonRequest()
	request.set_accept_format('json')
	request.set_domain('dysmsapi.aliyuncs.com')
	request.set_method('POST')
	request.set_protocol_type('https') # https | http
	request.set_version('2017-05-25')
	request.set_action_name('SendSms')

	request.add_query_param('RegionId', "cn-hangzhou")

	request.add_query_param('PhoneNumbers', mobile)
	request.add_query_param('SignName', signname)
	request.add_query_param('TemplateCode', templatecode)
	request.add_query_param('TemplateParam', '{"code":"%s"}' % msg)
	response = client.do_action_with_exception(request)
	response = json.loads(response)
	return response


if __name__ == '__main__':
	import sys
	mobile = sys.argv[1]
	msg = sys.argv[2]
	response = send_by_alidayu(mobile, msg)
	print(response)