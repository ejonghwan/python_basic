


# 타입: 숫자, 문자열, 불, 
# 자료구조: 변수, 리스트, 튜플 , 딕셔너리 , 집합



# 1. 숫자
# a = 3
# b = 4

# print(type(1)) # 정수 int
# print(type(3.5)) # 소수 float
# print(a//b)  # / 나누기   // 몫   % 나머지
# print(a**b)  # 제곱 3의 4승


# 2. 문자
# \n띄어쓰기   \t탭간격  \\슬러쉬  \'작따옴  \"큰따 
a = 'abcdefg'
print(type(a))


# 3. 인덱싱 
# print(a[1])

# 4. 슬리이싱 
# print(a[이상:미만:간격])
# print(a[2:6:2])


# 5. 포메팅   %d 정수    %f 실수    %s 문자열
# a = "호호하하 3 호호하하"
# print(a)

# num = 5
# day = "one"
# b = "나는 %d개의 사과를 먹었다 %s " %(num, day)
# print(b)

# 소수점 남길땐
# c = "%0.4f" % 3.145234324234235235235 
# print(c)


a = "hobby"
print(a.count('b')) #갯수
print(a.find('b'))  #인덱스
print(",".join("abcd")) #앞을 기준으로 나눠줌 split 이랑비슷
print(a.lower()) #대문자 소문자로
print(a.upper()) #소문자ㅣ 대문자로
print(a.strip()) #공백지우기
#replace 바꾸기
#split :기준으로 짤라서 배열로 


# 6. 리스트
# a.sort() 정렬
# a.append() 추가
# a.reverse() 위ㅏ치바꾸기
# a.index(5) 번호찾기
# a.insert() 특정인덱스에 삽입
# a.remove() 지우기
# a.pop() 마지막껄 빼내기
# a.count("a") 세어줌
# a.extend([2,3]) 추가
