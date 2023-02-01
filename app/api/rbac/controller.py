# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""

from app.api.base.controller import BaseView
from app.api.rbac.service import RBACService
from middleware.decorator import *

from external.protocol.python.alter_role_request import AlterRoleRequest
from external.protocol.python.alter_role_response import AlterRoleResponse
from external.protocol.python.menu_create_request import MenuCreateRequest
from external.protocol.python.menu_create_response import MenuCreateResponse
from external.protocol.python.menu_list_request import MenuListRequest
from external.protocol.python.menu_list_response import MenuListResponse

class AlterRoleView(BaseView):
    """
    修改用户角色
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = AlterRoleRequest
    response_protocol = AlterRoleResponse
    view_func = {
        "post": RBACService.alter_role
    }

class MenuListView(BaseView):
    """
    菜单列表
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = MenuListRequest
    response_protocol = MenuListResponse
    view_func = {
        "post": RBACService.menu_list
    }

class MenuCreateView(BaseView):
    """
    菜单创建
    """
    methods = ["POST"]  # 允许的请求方式
    request_protocol  = MenuCreateRequest
    response_protocol = MenuCreateResponse
    view_func = {
        "post": RBACService.menu_create
    }

