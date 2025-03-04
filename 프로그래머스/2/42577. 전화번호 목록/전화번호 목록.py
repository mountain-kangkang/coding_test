'''
def solution(phone_book):
    
    for phone in phone_book:
        for sec_ph in phone_book:
            if phone == sec_ph:
                continue;
            ph_len = len(phone)
            if phone == sec_ph[0:ph_len]:
                return False
    
    return True
# 채점 결과
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0

# 시간 복잡도: 현재 코드는 O(n^2) 시간 복잡도를 가집니다. 이는 큰 입력값에 대해 매우 비효율적입니다.
# 불필요한 비교: 같은 전화번호를 비교하는 경우를 건너뛰는 것은 좋지만, 모든 가능한 쌍을 비교하는 것은 여전히 비효율적입니다.
# 접두어 검사 방법: 현재 방식은 모든 가능한 접두어를 확인합니다. 이는 불필요한 연산을 초래합니다.
'''

def solution(phone_book):
    phone_book.sort()  # 전화번호를 정렬
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True
'''
# 정렬 활용: 전화번호를 정렬함으로써, 인접한 번호만 비교하면 됩니다. 이는 시간 복잡도를 O(n log n)으로 줄입니다.
# 효율적인 접두어 검사: startswith() 메소드를 사용하여 접두어를 효율적으로 확인합니다.
# 불필요한 비교 제거: 정렬 후에는 인접한 번호만 비교하므로, 불필요한 비교를 대폭 줄일 수 있습니다.
'''