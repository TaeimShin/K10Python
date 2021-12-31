'''
문제 3
아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요. 
*
**
***
****
*****
'''
for j in range(5):
    for i in range(j+1):
        print('*', end='')
    print("")