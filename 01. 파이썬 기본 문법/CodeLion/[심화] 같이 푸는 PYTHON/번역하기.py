# Step 1. 미리보기
# 번역기 프로그램

# Step 2. Googletrans 알아보기
# googletrans -> 언어 감지 / 번역
# 언어 감지 -> 안녕하세요 : 한국어 / Hello : 영어
# 번역 	  -> 안녕하세요 : Hello / 사자 : Lion / 한국 : South Korea
from googletrans import Translator
print(Translator) 				# <class 'googletrans.client.Translator'>

# Step 3. 언어 감지하기
# 1. 번역기를 만든다. -> Translator()
# 2. 언어 감지를 원하는 문장을 설정한다. 
# 3. 언어를 감지한다. -> detect(text)
from googletrans import Translator

translator = Translator()
# sentence = "안녕하세요 코드라이언입니다."
sentence = input("언어를 감지할 문장을 입력해주세요 : ")
detected = translator.detect(sentence)

print(detected) 			# Detected(lang=ko, confidence=1.0) / confidence -> 신뢰성
print(detected.lang)		# ko

# Step 4. 번역하기 1
# 1. 번역기를 만든다. 				-> Translator()
# 2. 번역을 원하는 문장을 설정한다.
# 3. 번역을 원하는 언어를 설정한다.		-> translate(text, dest, src) / text : 번역을 원하는 문장, dest : 번역하고자 하는 언어, src : 생략가능, source, 번역된 언어
# 4. 번역한다.
from googletrans import Translator
translator = Translator()
sentence = "안녕하세요 코드라이언입니다."
result = translator.translate(sentence, "en")
print(result)

# Step 5. 번역하기 2
from googletrans import Translator

translator = Translator()

# sentence = "안녕하세요 코드라이언입니다."
sentence = input("번역을 원하는 문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요? ")

result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

print("===========출 력 결 과===========")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("=================================")