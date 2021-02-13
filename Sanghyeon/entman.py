'''
개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를
몰래 공격하려고 합니다. 메뚜기 마을에는 여러개의 식량창고가
있는데 식량 창고는 일직선으로 이어져 있습니다.
각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는
식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정입니다. 이때
메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로
인접한 식량창고가 공격받으면 바로 알아낼 수 있습니다.
따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기
위해서는 최소한 한 칸 이상의 떨어진 식량 창고를 약탈해야 합니다.

입력조건 첫째 줄에 식량 창고의 개수는 N이 주어집니다.(3 <= N <= 100)
         둘째 줄에 공백을 기준으로 각 식량창고에 저장된 식량의 개수 K 가 주어집니다. (0 <= K <= 1,000)
출력조건 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하세요
입력예시 4 
         1 3 1 5
출력예시 8

'''

# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 데이터를 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programing) 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n-1])