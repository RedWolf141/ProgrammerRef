# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.

#동아리 부원
define chris = Character("레프", color = "#c95760")
define vec = Character("벡터", color = "#000000")
define black = Character("블랙", color = "#495057")
define han = Character("하나", color = "#dbde21" )

#조연들
define class = Character("담임선생님", color = "000000")

define narrator = Character(None, kind = nvl)
define nul = Character(None)


#배경 사진들 
image bg_white = "Bg/white.jpg" 
image teachers_office = "Bg/teachers_office.jpg"

#캐릭터 
image chris:
    im.FactorScale("character/ref_chris.png", 1.5)
    

define center = Position(xalign = 0.5)
define left = Position(xalign = 0.2)
define right = Position(xalign = 0.8)
# 여기에서부터 게임이 시작합니다.
label start:
    scene bg_white
    " 들어가기에 앞서 알려드릴것이 있습니다."
    " 본 소설의 내용은 --입니다. 동명의 실제 인명, 단체, 사건, 장소와는 무관함을 알립니다. "
    " 또한 본 작품의 캐릭터의 대부분이 퍼리가 나오니, 좋아하지 않는 분들은 유의 해주시길 바랍니다."
    jump chapter1


label chapter1:
    
    nvl clear
    scene teachers_office
    " 고등학교 입학이 얼마 안남았을때, 담임 선생님께서 교무실로 부르셔서, 교무실로 가는 길이었다."
    " 평소에 성적이 좋아서 여러 선생님들이 눈독을 들이셨는데, 이렇게 입학 직전에 부르는 경우는 드물었기에 조금은 의아한 생각이 들었다."
    " 그렇게 교무실에 도착해서 담임 선생님이 있는곳으로 향하였다. "
    nvl clear
    class " 어 그래, 왔니?"
    show chris at right
    chris " 네, 혹시 무슨 일로 부른건가요?"
    class " 이번에 장래 희망 조사서 적은거 때문에 말이지."
    class " 너가 적은걸 보니까 게임 개발자?가 되고 싶다고 적었는걸."
    chris " 예 맞아요. 꼭 컴퓨터 공학과나 아니면 게임 개발 관련 학과로 가서 개발자가 되고 싶어요."
    class " 차라리 의대나 신소재쪽으로 가는건 어떠니?"
    class " 그런 게임 만드는 회사 가는거 보다 차라리 의대로 가서 의사가 되면 돈도 많이 벌텐데"
    class " 특히 과학 선생님이 화학이랑 생명 과학에 재능이 있다고 엄청 칭찬하던데"

    narrator " 평소에도 담임 선생님이 개발자들을 무시하는 경향을 보이긴 했지만 이정도 일줄이야.. "
    narrator " 다른 선생님도 한번씩 권유는 했지만, 담임 선생님 마저 이럴줄은 몰랐는걸."


    return
