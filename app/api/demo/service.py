# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

from external.protocol.python.add_demo_request import AddDemoRequest
from external.protocol.python.add_demo_response import AddDemoResponse
from external.protocol.python.alter_demo_request import AlterDemoRequest
from external.protocol.python.alter_demo_response import AlterDemoResponse
from external.protocol.python.delete_demo_request import DeleteDemoRequest
from external.protocol.python.delete_demo_response import DeleteDemoResponse
from external.protocol.python.query_demo_request import QueryDemoRequest
from external.protocol.python.query_demo_response import QueryDemoResponse
from external.protocol.python.query_demos_request import QueryDemosRequest
from external.protocol.python.query_demos_response import QueryDemosResponse

class DemoService(object):
	"""
	示例服务
	"""
	@classmethod
	def add_demo(cls, request: AddDemoRequest, response: AddDemoResponse):
		"""
		添加demo
		"""
		response.set_name(request.name)
		response.set_age(request.age)


	@classmethod
	def query_demo(cls, request: QueryDemoRequest, response: QueryDemoResponse):
		"""
		查询demo
		"""
		response.set_name(request.name)
		response.set_age(request.age)


	@classmethod
	def query_demos(cls, request: QueryDemosRequest, response: QueryDemosResponse):
		"""
		查询demo列表
		"""
		response.set_name(request.name)
		response.set_age(request.age)


	@classmethod
	def alter_demo(cls, request: AlterDemoRequest, response: AlterDemoResponse):
		"""
		修改demo
		"""
		response.set_name(request.name)
		response.set_age(request.age)


	@classmethod
	def delete_demo(cls, request: DeleteDemoRequest, response: DeleteDemoResponse):
		"""
		删除demo
		"""
		response.set_name(request.name)
		response.set_age(request.age)


