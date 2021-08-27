class Diary:
    def __init__(self, date):
        # 날짜
        self.date = ''
        # 이모지
        self.emoji = ''
        # 일기 작성
        self.write = ''
        pass

    def set_date(self):
        time = input("날짜를 입력하세요 ex)2021.06.04 : ")
        self.time = 0 if time == '' else time
        # 예시를 보여줌(2021.06.04)

    def set_emoji(self):
        link = input('>> 자신의 기분을 숫자로 입력해 나타내주세요. : ')
        if link == '1':
            print('기쁨')
        elif link == '2':
            print('슬픔')
        elif link == '3':
            print('화남')
        else:
            input('>>자신의 기분을 직접 작성하세요. : ')

        # 이모티콘을 숫자로 선택하게 함

    def set_write(self):
        while True:
            info = input("일기를 작성하세요 (일기를 종료하려면 1을 눌러주세요.)")
            if info == '':
                break

            if info == 1:
                print("작성 종료!")
                break

        # if로 일기가 끝났는지 물어본 후 이모지에 따라 응원문구 출력

    def set_diary(self):
        self.set_date()
        self.set_emoji()
        self.set_write()

    def __str__(self):
        return

