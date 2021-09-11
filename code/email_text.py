import smtplib
import os
# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart

# 이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders

# 텍스트형식
from email.mime.text import MIMEText

# 위의 모든 객체를 생성할 수 있는 기본 객체
#MIMEBase(_maintype, _subtype)
# MIMEBase(<메인타입>,<서브타입>)
from email.mime.base import MIMEBase

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS보안연결
        server.starttls()
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        # 로그인된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string())
        # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.

        # 이메일을 성공적으로 보내면 결과는 {}, 자료형에 참거짓이 있다. 빈 딕셔너리는 False.
        if not response:
            print("이메일을 성공적으로 보냈습니다.")
        else:
            print(response)

smtp_info = dict({"smtp_server": "smtp.naver.com",  # SMTP서버주소
                  "smtp_user_id": "hahagarden1@naver.com",
                 "smtp_user_pw": "python-email",
                  "smtp_port": 587})  # SMTP서버포트

# 메일내용 작성
title = "한결이에게"
content = """한결아 안녕, 자료형에도 참/거짓이 있대.
빈 리스트,딕셔너리는 False를 의미한대.
빈 딕셔너리를 반환해야 정상실행된거라서 if not A 조건문을 사용했어.
니가 다시 보내랬지만 싫어. 이부분은 구글에서 자동으로 앞에 동일한 내용을 확인해주는지 확인하기위해 추가한 문장이야.
그리고 gmail로 보낼수 없어. 이건 네이버에서 SMTP 환경설정을 사용한거거든.
미안. 허위사실 유포했네. 내가 보내는 메일만 네이버로 하면 되나봐.
gmail로도 성공했어. 확인해줘서 고마워."""
sender = smtp_info['smtp_user_id']  # 송신자(sender) 이메일 계정
receiver = "kghnkl0103@gmail.com"

# 메일객체 생성: 메시지 내용에는 한글이 들어가기 때문에 한글을 지원하는 문자 체계인 UTF-8을 명시해주기
msg = MIMEText(_text=content, _charset="utf-8")  # 이메일 내용

msg['Subject'] = title  # 메일제목
msg['From'] = sender  # 송신자
msg['To'] = receiver  # 수신자

send_email(smtp_info, msg)
