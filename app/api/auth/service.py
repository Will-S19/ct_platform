# -*- coding: utf-8 -*-
from app.model.tbl_user import TblUser
from common.mydb import mydb
from common.exception import CtException
from common.result_code import ERR_USER_NOT_FOUND,ERR_PASSWORD,ERR_USER_EXISTS
from common.token import hash_password, encode_jwt

from external.protocol.python.login_request import LoginRequest
from external.protocol.python.login_response import LoginResponse
from external.protocol.python.register_request import RegisterRequest
from external.protocol.python.register_response import RegisterResponse

from app.model.tbl_user import TblUser


class AuthService(object):
    """
    示例服务
    """

    @classmethod
    def login(cls, request: LoginRequest, response: LoginResponse):
        """
        登录
        """
        # 校验用户是否已经存在
        tbl_user = mydb.query(TblUser).filter(TblUser.username == request.username).first()
        if not tbl_user:
            raise CtException(ERR_USER_NOT_FOUND)

        # 哈希密码
        password = hash_password(request.password)

        # 校验密码是否正确
        if password != tbl_user.password:
            raise CtException(ERR_PASSWORD)

        # 签发token
        jwt = encode_jwt({
            "user_account": tbl_user.user_account
        }, user_account=tbl_user.user_account)
        response.set_jwt(jwt)

    @classmethod
    def register(cls, request: RegisterRequest, response: RegisterResponse):
        """
        注册
        """
        # 校验用户是否已经存在
        user = mydb.query(TblUser).filter(TblUser.username == request.username).first()
        if user:
            raise CtException(ERR_USER_EXISTS)

        # 将请求赋值给model对象
        tbl_user = TblUser()

        # 哈希密码
        password = hash_password(request.password)

        # 插入数据库
        tbl_user.password = password
        tbl_user.username = request.username
        mydb.add(tbl_user)
        mydb.commit()
