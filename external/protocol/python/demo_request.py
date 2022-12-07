# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class DemoRequest:
	"""
	this a demo
	"""
	def __init__(self) -> None:
		self._name = ""  # 姓名
		self._name_u = 0  # 姓名设置标识
		pass

	def set_name(self, name):
		"""
		set 姓名
		"""
		self._name = name
		self._name_u = 1

	@property
	def is_set_name(self):
		"""
		is set 姓名
		"""
		return self._name_u != 0

	@property
	def name(self):
		"""
		get 姓名
		"""
		return self._name

	def to_dict(self) -> dict:
		"""
		Convert object to dict and return
		"""
		data_dict = {}
		data_dict["name"] = self._name  # 姓名

		return data_dict

	def to_obj(self, data_dict: dict):
		"""
		Convert dict to object
		"""

		# check params
		if len( data_dict.get("name") ) < 1:
			raise Exception("param:name error, out of range min:1!")
		if len( data_dict.get("name") ) > 32:
			raise Exception("param:name error, out of range max:32!")

		# parse params
		self.set_name( data_dict.get("name") )  # 姓名

	def to_json(self):
		"""
		Convert object to object
		"""
		return json.dumps( self.to_dict() )
