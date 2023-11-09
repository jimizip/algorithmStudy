# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력: 첫째 줄에 A+B를 출력한다.
A,B = map(int, input().split())
print(A+B)

# split()는 공백을 기준으로 문자열을 잘라줌.
# input().split에 int()를 할 수 없기 때문에 map을 사용하여 코드 길이를 줄임.