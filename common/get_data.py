from common.do_initdata import DoInitData
class GetData:
    COOKIE=None
    '''未注册初始号码'''
    noreg_tel=DoInitData.read_initdata(1,1)
    '''登录通用号码'''
    login_tel=DoInitData.read_initdata(2,1)
    '''借钱人ID'''
    loan_member_id = DoInitData.read_initdata(4,1)
    '''管理人账号'''
    admin_tel = DoInitData.read_initdata(3,1)
    '''用户id'''
    memberID=DoInitData.read_initdata(5,1)
    '''标id'''
    loanid=None
    pwd='123456'
if __name__ == '__main__':
    print(getattr(GetData,'memberID'))