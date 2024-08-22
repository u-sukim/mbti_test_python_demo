print("힙합 MBTI 테스트")


ei = [0, 0, 0, 0, "X"] #최종합, 1번, 2번, 3번, 최종글자 순서임.
ns = [0, 0, 0, 0, "X"]
ft = [0, 0, 0, 0, "X"]
pj = [0, 0, 0, 0, "X"]


def inp(what, n): #인풋받아서 숫자로 __[1], __[2], __[3]에 저장.(1, -1 순서 지문)
    choice = input("a/b 입력: ")
    if(choice == "a"):
        what[n] = 1
    elif(choice == "b"):
        what[n] = -1
    else:
        print("wrong input!")
        inp(what, n)


def inp_rvs(what, n): #인풋받아서 숫자로 __[1], __[2], __[3]에 저장.(-1, 1 순서 지문)
    choice = input("a/b 입력: ")
    if(choice == "a"):
        what[n] = -1
    elif(choice == "b"):
        what[n] = 1
    else:
        print("wrong input!")
        inp(what, n)

def plusAll(what):
    for i in range(1, 4):
        what[0] += what[i]


def convert(what):
    if what == ei:
        what[4] = "E" if what[0] > 0 else "I"
    elif what == ns:
        what[4] = "S" if what[0] > 0 else "N"
    elif what == ft:
        what[4] = "F" if what[0] > 0 else "T"
    elif what == pj:
        what[4] = "P" if what[0] > 0 else "J"
    else:
        print("wrong input!")
        convert(what)

def result_mbti():
    mbti = ei[4] + ns[4] + ft[4] + pj[4]
    print(f"{mbti}")
    
    mbti_descriptions = {
        "ISTJ": "세상의 소금형",
        "ISTP": "백과사전형",
        "ESTP": "수완좋은 활동가형",
        "ESTJ": "사업가형",
        "ISFJ": "임금 뒷편의 권력형",
        "ISFP": "성인군자형",
        "ESFP": "사교적인 유형",
        "ESFJ": "친선도모형",
        "INFJ": "예언자형",
        "INFP": "잔다르크형",
        "ENFP": "스파크형",
        "ENFJ": "언변능숙형",
        "INTJ": "과학자형",
        "INTP": "아이디어형",
        "ENTP": "발명가형",
        "ENTJ": "지도자형"
    }
    
    if mbti in mbti_descriptions:
        print(mbti_descriptions[mbti])
    else:
        print("오류가 발생했습니다.")
        result_mbti()


print("1. 힙합 콘서트에 가게 됐다.")  # E/I 결정
print("a) 친구들과 함께 소리 지르며 에너지를 발산한다.")  # E(+1)
print("b) 사람들과의 소통보다는 음악에 집중하며 감상한다.")  # I(-1)
inp(ei, 1)

print("2. 힙합 커뮤니티에 논란이 되는 주제가 올라왔다.")  # E/I 결정
print("a) 즉각 댓글을 달아 논쟁에 참여하며 자신의 의견을 강하게 주장한다.")  # E(+1)
print("b) 상황을 지켜보며 필요할 때만 의견을 남긴다.")  # I(-1)
inp(ei, 2)

print("3. 리스닝 파티에 참석할 기회가 생겼다.")  # E/I 결정
print("a) 다양한 사람들과 적극적으로 네트워킹을 시도하며 인맥을 쌓는다.")  # E(+1)
print("b) 필요한 경우에만 사람들과 교류하고 대부분은 관찰자 역할을 한다.")  # I(-1)
inp(ei, 3)



print("4. 얼마 전 커리어 하이를 달성한 래퍼가 신보를 냈는데 내 기대에 못 미쳤다.")  # N/S 결정
print("a) 그동안의 커리어를 무시하거나 부정하며 아쉬워한다.")  # S(+1)
print("b) 그럼에도 불구하고 다음 앨범을 기대하며 기다린다.")  # N(-1)
inp(ns, 1)

print("5. 음악을 들을 때,")  # N/S 결정
print("a) 남들이 잘 모르는 숨겨진 곡들을 디깅해 듣는 편이다.")  # N(+1)
print("b) 현재 유행하고 있고, 상대적으로 대중적인 곡들을 즐겨 듣는 편이다.")  # S(-1)
inp(ns, 2)

print("6. 평소 좋아하던 아티스트의 LP 한정반이 재발매됐다. 하지만 해당 LP의 가격이 만만치 않다.")  # N/S 결정
print("a) 그 LP의 예술적 가치와 희소성을 중요하게 여긴다.")  # N(+1)
print("b) 가격이 너무 비싸다고 판단하고 포기한다.")  # S(-1)
inp(ns, 3)



print("7. 내가 평소 애정하던 래퍼의 신곡 뮤직비디오에 출연할 기회가 생겼다.")  # T/F 결정
print("a) 별로 이득될 게 없기 때문에 정중히 거절한다.")  # T(-1)
print("b) 이득이 되지는 않지만, 래퍼의 뮤직비디오 제작에 참여한다.")  # F(+1)
inp_rvs(ft, 1)

print("8. 나의 최애 앨범에 대해 부정적으로 말하는 친구에게, 당신의 반응은?")  # T/F 결정
print("a) 그 친구의 의견도 존중하며 대화를 이어간다.")  # F(+1)
print("b) 그 앨범이 명반인 이유를 논리적으로 설명하며 설득한다.")  # T(-1)
inp(ft, 2)

print("9. 평소 팬이었던 래퍼의 안 좋은 기사가 올라왔을 때, 당신은 어떻게 반응하나요?")  # T/F 결정
print("a) 사건의 사실 여부와 논리적인 근거를 확인하며 이성적으로 판단한다.")  # T(-1)
print("b) 아티스트의 입장을 이해하고 감정적으로 공감하며 받아들인다.")  # F(+1)
inp_rvs(ft, 3)



print("10. 평소 좋아하던 아티스트의 새 앨범이 나왔을 때, 어떻게 감상하나요?")  # P/J 결정
print("a) 앨범을 처음부터 끝까지 순서대로 듣고 전체적인 흐름을 분석한다.")  # J(-1)
print("b) 기분에 따라 무작위로 트랙을 골라 듣는다.")  # P(+1)
inp_rvs(pj, 1)

print("11. 여행을 갈 때 음악을 선곡해야 한다면, 어떻게 고르시나요?")  # P/J 결정
print("a) 미리 플레이리스트를 준비해 체계적으로 선곡한다.")  # J(-1)
print("b) 여행 중 그때그때 분위기에 맞춰 즉흥적으로 고른다.")  # P(+1)
inp_rvs(pj, 2)

print("12. 아티스트의 새 앨범 발매 소식을 들었을 때, 어떻게 행동하나요?")  # P/J 결정
print("a) 발매일을 미리 체크하고 사전 예약을 통해 확실히 준비한다.")  # J(-1)
print("b) 발매 당일에 상황을 보고 그때 구매를 결정한다.")  # P(+1)
inp_rvs(pj, 3)


plusAll(ei) #__[1] + __[2] + __[3] 값을 모두 더해 __[0]에 숫자로 저장.
convert(ei) #__[0]이 양수냐 음수냐에 따라 각 알파벳 결정.
plusAll(ns)
convert(ns)
plusAll(ft)
convert(ft)
plusAll(pj)
convert(pj)

result_mbti() #예시 : ENFP, ENTP, INTP, ...
