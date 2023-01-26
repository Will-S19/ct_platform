# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

from external.protocol.python.authority_list_request import AuthorityListRequest
from external.protocol.python.authority_list_response import AuthorityListResponse
from external.protocol.python.menu_create_request import MenuCreateRequest
from external.protocol.python.menu_create_response import MenuCreateResponse
from external.protocol.python.menu_list_request import MenuListRequest
from external.protocol.python.menu_list_response import MenuListResponse
from external.protocol.python.role_create_request import RoleCreateRequest
from external.protocol.python.role_create_response import RoleCreateResponse

class RBACService(object):
	"""
	权限服务
	"""
	@classmethod
	def role_create(cls, request: RoleCreateRequest, response: RoleCreateResponse):
		"""
		角色创建
		"""
		pass


	@classmethod
	def authority_list(cls, request: AuthorityListRequest, response: AuthorityListResponse):
		"""
		权限列表
		"""
		pass


	@classmethod
	def menu_list(cls, request: MenuListRequest, response: MenuListResponse):
		"""
		菜单列表
		"""
		pass


	@classmethod
	def menu_create(cls, request: MenuCreateRequest, response: MenuCreateResponse):
		"""
		菜单创建
		"""
		pass


