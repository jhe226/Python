# p.g 270
# 01.
class Book():
    def set_info(self, title, name):
        self.title = title
        self.name = name
    def print_info(self):
        print('책 제목: {}'.format(self.title))
        print('책 저자: {}'.format(self.name))

book1 = Book()
book2 = Book()

book1.set_info('파이썬', '민경태')
book2.set_info('어린왕자', '생텍쥐페리')

book_list = [book1, book2]
for book in book_list:
    book.print_info()

print()
print()

# 02.
class Watch:
    def set_time(self):
        now = input('시간을 입력하세요 >>> ')
        hms = now.split(':')
        self.hour = int(hms[0])
        self.minute = int(hms[1])
        self.second = int(hms[2])
        
    def add_hour(self, hour):
        if hour <= 0:
            return
        self.hour += hour
        self.hour %= 24
        
    def add_minute(self, minute):
        if minute <= 0:
            return
        self.minute += minute
        self.add_hour(self.minute // 60)
        self.minute %= 60
    def add_second(self, second):
        if second <= 0:
            return
        self.second += second
        self.add_second(self.second // 60)
        self.second %= 60

    def print_hms(self):
        print('계산된 시간은 {}시 {}분 {}초입니다.'.format(self.hour, self.minute, self.second))

watch = Watch()
watch.set_time()
watch.add_hour(int(input('계산할 시간을 입력하세요 >>> ')))
watch.add_minute(int(input('계산할 분을 입력하세요 >>> ')))
watch.add_second(int(input('계산할 초를 입력하세요 >>> ')))
watch.print_hms()
print()
print()

# p.g 271
# 03.
class Singer :
    def set_song(self, song, genre):
        self.song = song
        self.genre = genre
    def set_singer(self, singer):
        self.singer = singer
    def hit_song(self, hit):
        self.hit = hit
    def print_singer(self, singer, hit):
        print('가수이름 : {}\n노래제목 : {}({})'.format(self.singer, self.song, self.genre))

s = Song()
s.set_song('취중진담','발라드')
s.set_singer('김동률')
s.set_hit(song)
singer.print_singer()

        
