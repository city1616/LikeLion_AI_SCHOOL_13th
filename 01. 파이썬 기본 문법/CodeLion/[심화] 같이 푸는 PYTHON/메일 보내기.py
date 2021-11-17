# Step 1. 미리보기
# python으로 메일 보내는 프로그램

# Step 2. 사전 준비
# IMAP 사용 설정 -> IMAP 사용
# IMAP -> 다양한 기기에서 이메일에 엑세스하고 클라이언트, 서버에 이메일과 첨부파일을 저장하기 위함
# 메일 계정의 외부 접속에 대한 보안 설정 -> 보안 수준이 낮은 앱의 액세스 허용!

# Step 3. SMTP 1
# SMTP -> Simple Mail Transfer Protocol -> 간단하게 메일을 보내기 위한 약속
# Email Client(A) --- SMTP ---> Email Server(a@gmail.com) --- SMTP ---> Email Server(b@gmail.com) --- IMAP ---> Email Client(B)
# Email Client(A) <--- IMAP --- Email Server(a@gmail.com) <--- SMTP --- Email Server(b@gmail.com) <--- SMTP --- Email Client(B)
# SMTP 서버를 이용해서 우리가 원하는 곳으로 메일을 보낼 수 있다.

# Step 4. SMTP 2
# SMTP Server Address : smtp.gmail.com / Port : 465
# smtplib

# Step 5. SMTP 3
# 1. SMTP 메일 서버를 연결한다.		-> smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# 2. SMTP 메일 서버에 로그인한다.		-> smtp.login("gmail계정", "비밀번호")
# 3. SMTP 메일 서버로 메일을 보낸다.	-> smtp.send_message(), smtp.quit()
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 		# SMTP() -> SMTP_SSL()로 변경, gmail은 ssl 요구
print(smtp)												# <smtplib.SMTP_SSL object at 0x7f2b990d4040>

# Step 6. SMTP 4
# 2. SMTP 메일 서버에 로그인한다.		-> smtp.login("gmail계정", "비밀번호")
# 3. SMTP 메일 서버로 메일을 보낸다.	-> smtp.send_message(), smtp.quit()
import smtplib
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 	
# print(smtp.login("seungwoo132@gmail.com", "Seungsfla!24"))
smtp.login("seungwoo132@gmail.com", "Seungsfla!24")
smtp.send_message()
smtp.quit()

# Step 7. MIME
# MIME -> 전자 우편을 위한 인터넷 표준 포맷
# email.message 모듈 -> 파이썬 내장 모듈 -> .EmailMessage 기능
# 1. 이메일을 만든다			-> EmailMessage()
# 2. 이메일에 내용을 담는다		-> message.set_content("") -> 본문 작성
# 3. 발신자, 수신자를 설정한다.
import smtplib
from email.message import EmailMessage
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 	
# print(smtp.login("seungwoo132@gmail.com", "Seungsfla!24"))
smtp.login("seungwoo132@gmail.com", "Seungsfla!24")
smtp.send_message()
smtp.quit()

# Step 8. MIME - Header
# 3. 발신자, 수신자를 설정한다.
# Header -> Subject(제목), From(보내는 사람, 송신자), To(받는 사람, 수신자)
import smtplib
from email.message import EmailMessage
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")
message["Subject"] = "이것은 제목입니다."
message["From"] = "seungwoo132@gmail.com"
message["To"] = "seungwoo132@gmail.com"
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 	
# print(smtp.login("seungwoo132@gmail.com", "Seungsfla!24"))
smtp.login("seungwoo132@gmail.com", "Seungsfla!24")
smtp.send_message()
smtp.quit()

# Step 9. 메일 전송하기
# smtp.send_message(message) message -> MIME
import smtplib
from email.message import EmailMessage
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")
message["Subject"] = "이것은 제목입니다."
message["From"] = "seungwoo132@gmail.com"
message["To"] = "seungwoo132@gmail.com"
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 	 # SMTP Server에 연결
# print(smtp.login("seungwoo132@gmail.com", "Seungsfla!24"))
smtp.login("seungwoo132@gmail.com", "Seungsfla!24")  # 로그인
smtp.send_message(message)							 # 이메일 전송
smtp.quit()

# Step 10. 메일에 사진 첨부하기 1
# mode -> rb(read binary), wb(write binary), ab(append binary)
# open() - codelion.png / rb
image = open("codelion.png", "rb")
# 파일을 읽어서 출력해보세요. -> read()
print(image.read())

# Step 11. 메일에 사진 첨부하기 2
# add_attachment(...) -> multipart/mixed 타입의 메일
# 1. image -> 첨부할 파일의 내용
# 2. maintype -> 첨부한 내용의 유형(image, video)
# 3. subtype -> 확장자(png)
import smtplib
from email.message import EmailMessage
import imghdr
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")
message["Subject"] = "이것은 제목입니다."
message["From"] = "seungwoo132@gmail.com"
message["To"] = "seungwoo132@gmail.com"
with open("codelion.png", "rb") as image :
	image_file = image.read()
image_type = imghdr.what("codelion", image_file)
print(image_type) # png
message.add_attachment(image_file, maintype = "image", subtype = image_type)
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 	 # SMTP Server에 연결
# print(smtp.login("seungwoo132@gmail.com", "Seungsfla!24"))
smtp.login("seungwoo132@gmail.com", "Seungsfla!24")  # 로그인
smtp.send_message(message)							 # 이메일 전송
smtp.quit()

# Step 12. 유효성 검사하기 1
# 정규표현식 -> 문자열에서 나타나는 특정 패턴을 알아내 대응시키기 위해 사용되는 표현식, 이메일에만 나타나는 특정한 패턴 사용
# ^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$
# ^ 시작, $ 끝
# [a-zA-Z0-9.+_-]+ -> a부터 z까지, A부터 Z까지, 0부터 9까지, ., +, _, -
# + -> 1회 이상 반복된다.
# \. -> 그 뒤에 .이 붙는다.
# [a-zA-Z] -> a부터 z까지, A부터 Z까지
# {2, 3} -> 최소 2회, 최대 3번 반복된다.

# Step 13. 유효성 검사하기 2
import smtplib
from email.message import EmailMessage
import imghdr
import re # python 정규표현식
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")
message["Subject"] = "이것은 제목입니다."
message["From"] = "seungwoo132@gmail.com"
message["To"] = "seungwoo132@gmail.com"
with open("codelion.png", "rb") as image :
	image_file = image.read()
image_type = imghdr.what("codelion", image_file)
print(image_type) # png
message.add_attachment(image_file, maintype = "image", subtype = image_type)
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 	 # SMTP Server에 연결
# print(smtp.login("seungwoo132@gmail.com", "Seungsfla!24"))
smtp.login("seungwoo132@gmail.com", "Seungsfla!24")  # 로그인
reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"		# 이메일 유효성 검사
print(re.match(reg, "codelion.example@gmail.com"))			
smtp.send_message(message)							 # 이메일 전송
smtp.quit()

# Step 14. 유효성 검사하기 3
import smtplib
from email.message import EmailMessage
import imghdr
import re # python 정규표현식

def sendEmail(addr) :
	reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"		# 이메일 유효성 검사
	if bool(re.match(reg, addr)) :
		smtp.send_message(message)								# 이메일 전송
		print("정상적으로 메일이 발송되었습니다.")
	else :
		print("유효한 이메일 주소가 아닙니다.")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")
message["Subject"] = "이것은 제목입니다."
message["From"] = "seungwoo132@gmail.com"
message["To"] = "seungwoo132@gmail.com"

with open("codelion.png", "rb") as image :
	image_file = image.read()

image_type = imghdr.what("codelion", image_file)
print(image_type) # png

message.add_attachment(image_file, maintype = "image", subtype = image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) 	 # SMTP Server에 연결
# print(smtp.login("seungwoo132@gmail.com", "Seungsfla!24"))
smtp.login("seungwoo132@gmail.com", "Seungsfla!24")  # 로그인

# 메일을 보내는 sendEmail 함수를 호출해서 실행해보기		
sendEmail("seungwoo132@gmail.com")

smtp.quit()



















