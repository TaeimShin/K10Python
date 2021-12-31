'''
open()
    : 파일을 다룰떄 사용되는 내장함수로 첫번째만 필수
    
    mode : 파일 열기 모드
        r : 읽기모드
        
'''
print("="*30)
print("새파일01.txt")
print("="*30)


#새로운 파일을 생성하고 반복문으로 입력
f_open = open("새파일01.txt",mode='wt', encoding='utf-8')
for i in range(1,21):
    data = "%d번째 줄입니다.\n"%i
    f_open.write(data)
f_open.close()



f_read = open("새파일01.txt",mode= 'rt', encoding='utf-8')
while True:
    line = f_read.readline() # 파일 내용 한줄을 읽는다
    if not line: break #읽을내용이없다면 탈출
    print(line) # 출력
f_read.close()

#기존 파일에 내용 추가하기
f_add = open("새파일01.txt", mode='at', encoding='utf-8')
# 한줄을 추가한다. 개행문자가 없어 줄바꿈 처리가 되지않는다.
f_add.write("추가하는내용입니다.")
#리스트를 통해 여러줄의 내용을 입력한다.
f_add.writelines(["줄바꿈은되나요?\n", "안되면 개행문자를 넣어주세요."])
f_add.write("마지막라인입니다.")
f_add.close()

print("="*30)
print("새파일02.txt")
print("="*30)
#자동으로 파일 객체 닫기 및 여러줄 쓰기/ 읽기
#파일 쓰기
with open("새파일02.txt",mode='wt', encoding='utf-8') as myfile:
    for i in range(1,21):
        data = "%d라인 입력합니다.\n"%i
        myfile.write(data)
# 파일 읽기
with open("새파일02.txt",mode='rt', encoding='utf-8') as myfile:
    line = None
    while line != '':
        line = myfile.readline()
        print(line.strip('\n'))
        
        '''
        피클링
            : 파이썬 객체를 파일에 저장하는 과정을 의미한다.
            복원하는것으르 언피클링 이라고 한다.
            
        '''
import pickle #모듈임포트

name ='kosmo'
age = 99
address = '서울시 금천구 가산동'
times = {'JAVA': 20, 'HTML': 2, 'Oracle':10, 'Python':3} #딕셔너리


#kosmo.p 라는 파일을 2진파일 모드로 오픈 쓰기모드
with open('kosmo.p', 'wb') as file:
    pickle.dump(name, file) # dump()를 통해 저장
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(times,file)
    
#2진파일 읽기모드로 파일을 오픈한 후 load()를 통해 복원한다.
with open('kosmo.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    times = pickle.load(file)
    print("이름", name)
    print("나이", age)
    print("주소", address)
    print("배당시간", times)