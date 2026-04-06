"""
회원정보 C/R/U/D 처리 클래스
"""
from modules.UserVO    import UserVO
from modules.DBManager import DBManager

class UserDAO :
    def Login(self, id, pw) :
        
        with DBManager() as db :
            vo = None
            
            sql  = "select * from user "
            sql += f"where id = '{id}' and pw = md5('{pw}')"
            
            total = db.Select(sql)
            if total >= 0 :
                vo = UserVO()
                vo.id = db.GetValue(0,"id")
                vo.name   = db.GetValue(0,"name")
            return vo