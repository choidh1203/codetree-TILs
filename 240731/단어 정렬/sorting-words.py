#단어의 개수 n 입력
n = int(input())

#list comprehension을 이용하여 단어 리스트 구성
words = [input() for i in range(n)]

#리스트 내 단어들을 사전순으로 오름차순 정렬
words.sort()

#정렬된 단어 출력
for word in words:
    print(word)