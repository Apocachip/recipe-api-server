from http import HTTPStatus
from flask import request
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector
from email_validator import validate_email, EmailNotValidError

class UserRegisterResource(Resource) :
    def post(self) :
        
        # {
        #     "username" : "홍길동",
        #     "email" : "abc@naver.com",
        #     "password" : "1234"
        # }

        # 클라이언트가 body 에 보내준 json 을 받아온다.
        data = request.get_json()

        

        # 2. 이메일 주소형식이 제대로 된 주소형식인지
        # 확인하는 코드 작성.

        
        # DB에 저장하지마시고, 테스트코드만 작성해서 테스트해보세요.
        try :
            # 데이터 업데이트
            # 1. DB에 연결
            connection = get_connection()

            # 2. 쿼리문 만들기
            query = '''update user;'''

            record = (recipe_id, )
            
            # 3. 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서를 이용해서 실행한다.
            cursor.execute(query, record)

            # 5. 커넥션을 커밋해줘야 한다 => DB에 영구적으로 반영하라는 뜻
            connection.commit()

            # 6. 자원 해제
            cursor.close()
            connection.close()

        except mysql.connector.Error as e :
            print(e)
            cursor.close()
            connection.close()
            return {'error' : str(e)}, 503

        return {"result" : "success"}, 200