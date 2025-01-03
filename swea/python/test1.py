# 초기값 문제
def find_initial_balls(N, final_counts, D, X):
    moved_balls = 0
    current_box = D - 1

    while True:
        moved_balls += 1
        current_box = (current_box + 1) % N
        if current_box == X - 1:
            break

    return final_counts[D - 1] + moved_balls

# 입력 받기
N = int(input("박스의 총 개수를 입력하세요: "))
final_counts = list(map(int, input(f"{N}개의 박스의 최종 공 개수를 공백으로 구분하여 입력하세요: ").split()))
D = int(input("공을 꺼낸 박스 번호를 입력하세요: "))
X = int(input("공을 넣은 마지막 박스 번호를 입력하세요: "))

result = find_initial_balls(N, final_counts, D, X)
print(f"D번째 박스의 초기 공 개수: {result}")