# 중복되는 연산을 줄이자! 
'''Dynamic programing : 동적 계획법 이라고도 한다. 
대표적으로 피보나치 수열이 있다. : 이전 두 항의 합을 현재의 항으로 설정하는 특징이 있는 수열이다. 
수학자들은 점화식을 사용해 수열의 항이 이어지는 형태를 간결하게 표현한다. 
점화식 : 인접한 항들 사이의 관계식 
수학적인 식은 책을 참고하는게 더 좋을 것 같다. 

'''
"""8-1.py 피보나치 함수 코드
# 피보나치 함수를 재귀함수로 구현 
def fibo(x):
    if x == 1 or x == 2:
        return 1 
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
"""

'''피보나치 수열의 정확한 시간복잡도는 세타 표기법을 사용하지만, 일반적으로는 빅오표기법을 이용하여 O(2^N)의 지수시간이 소요된다고 표현한다. 
이렇게 되면 N =30인 경우 약 10억 가량의 연산을 수행해야 하는 대참사가 일어날 수 있다. 
그림으로 나타냈을 경우 동일한 함수가 반복적으로 호출되는 것을 알 수 있는데, 이는 연산량이 극적으로 늘어나는 것에 일조하기도 한다.
이걸 왜 작성했냐면 이걸 해결해주는 방법이 동적계획법이기 때문이다.
이 두가지 조건을 만족할 경우 Dynamic 프로그래밍 기법을 사용할 수 있다.
1) 큰 문제를 작은 문제로 나눌 수 있을 때
2) 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일할 때
피보나치 수열은 이 두 조건을 만족하는 대표 문제이다. 이 문제를 메모제이션 기법을 사용해서 해결해보자.
메모제이션 : 다이나믹 프로그래밍의 구현 방법 중 한 종류로, 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 
            그대로 가져오는 기법, 메모제이션이 값을 저장하는 방법을 캐싱이라고도 한다.
            
'''

# 8_2.py 피보나치 수열 소스코즈(재귀적)
"""
# 한 번 계산된 결과를 메모제이션 하기 위한 리스트 초기화 
d = [0] * 100 

# 피보나치 ㄹ함수를 재귀함수로 구현 (탑 다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건 (1 혹은 2 일 때 1을 반환)
    if x == 1 or x == 2 :
        return 1 
    # 이미 계산한적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
"""

'''정리하자면 다이나믹 프로그래밍이란 큰 문제를 작게 나누고, 같은 문제라면 한번씩만 풀어 문제를 효율적으로 해결하는 알고리즘이다.
이는 퀵정렬과도 비슷한데, 퀵 정렬은 정렬을 수행할 때 리스트를 분할하며 전체적으로 정렬이 될 수 있도록 한다.'''
    
# 8-3.py 호출되는 함수 확인 
"""
d = [0] * 100 

def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]

pibo(6)

이렇게 큰 문제를 해결하기 위해 작은 문제를 호출하는 것을 탑다운 방식이라고 한다. 
반면 단순이 반복문을 이용하여 작성하는 경우 작은 문제부터 차근차근 답을 도출하는 것을 보텀업 방식이라고 한다. 

"""
# 8-4.py 피보나치 수열(반복적)
"""앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [0] * 100 

# 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 2
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])"""


