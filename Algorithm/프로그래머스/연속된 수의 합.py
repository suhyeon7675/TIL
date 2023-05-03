def solution(num, total):
    answer = []
    start = total // num - num // 2 + (num % 2 == 0) * 1
    answer = [i for i in range(start, start + num)]
    return answer
