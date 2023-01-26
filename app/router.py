# -*- coding: utf-8 -*-
"""
The file auto generated by tool genapi, Do not modify.
"""
from flask import Flask
from flask.blueprints import Blueprint

from app.api.demo.controller import AddDemoView
from app.api.demo.controller import QueryDemoView
from app.api.demo.controller import QueryDemosView
from app.api.demo.controller import AlterDemoView
from app.api.demo.controller import DeleteDemoView
from app.api.rbac.controller import LoginView
from app.api.rbac.controller import RegisterView
from app.api.auth.controller import LoginView
from app.api.auth.controller import RegisterView

router = Blueprint('api', __name__)

def route_register(app: Flask):
	# service: 示例服务 owner: andy.mei@momenta.ai
	router.add_url_rule('/api/v1/demo/add_demo', view_func = AddDemoView.as_view('add_demo')) # 1.添加demo
	router.add_url_rule('/api/v1/demo/query_demo', view_func = QueryDemoView.as_view('query_demo')) # 2.查询demo
	router.add_url_rule('/api/v1/demo/query_demos', view_func = QueryDemosView.as_view('query_demos')) # 3.查询demo列表
	router.add_url_rule('/api/v1/demo/alter_demo', view_func = AlterDemoView.as_view('alter_demo')) # 4.修改demo
	router.add_url_rule('/api/v1/demo/delete_demo', view_func = DeleteDemoView.as_view('delete_demo')) # 5.删除demo

	# service: 权限服务 owner: 施意波
	router.add_url_rule('/api/v1/auth/login', view_func = LoginView.as_view('login')) # 1.角色创建
	router.add_url_rule('/api/v1/auth/register', view_func = RegisterView.as_view('register')) # 2.权限创建

	# service: 认证服务 owner: andy.mei@momenta.ai
	router.add_url_rule('/api/v1/login', view_func = LoginView.as_view('login')) # 1.登录
	router.add_url_rule('/api/v1/register', view_func = RegisterView.as_view('register')) # 2.注册

	app.register_blueprint(router)