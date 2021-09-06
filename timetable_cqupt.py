from hashlib import md5
from datetime import datetime, timedelta

classTime = [None, (8, 15), (9, 10), (10, 15), (11, 10), (13, 15), (14, 10),
	(15, 5), (16, 0)] #TODO: 添加第9, 第10节课的具体上课时间.
weeks = [None]
starterDay = datetime(2021, 9, 6)
for i in range(1, 30):
	singleWeek = [None]
	for d in range(0, 7):
		singleWeek.append(starterDay)
		starterDay += timedelta(days = 1)
	weeks.append(singleWeek)

oeWeek = lambda startWeek, endWeek, mode: [i for i in range(startWeek, endWeek + 1) if (i + mode) % 2 == 0]
rgWeek = lambda startWeek, endWeek: [i for i in range(startWeek, endWeek + 1)]
uid_generate = lambda key1, key2: md5(f"{key1}{key2}".encode("utf-8")).hexdigest()

classes = [
	["WEB前端技术", "张燕宁", "电信320第十机房", "191332200030", oeWeek(2, 6, 0) + rgWeek(7, 10) + rgWeek(12, 14) + [17] , 1, rgWeek(1, 4)],
	["软件工程与UML", "张景峰", "电信318第八机房", "191332200020", rgWeek(1, 2) + oeWeek(4, 6, 0) + rgWeek(12, 14) + rgWeek(17, 18), 2, rgWeek(1, 4)],
	["面向对象程序设计", "朱孔涛", "电信307第五机房", "191332100040", rgWeek(1, 4) + rgWeek(6, 10) + rgWeek(12, 14) + rgWeek(17, 18), 3, rgWeek(1, 4)],
	["形势与政策2", "李晓", "电信110阶梯教室", "191001100032", rgWeek(7, 8), 3, rgWeek(7, 8)],
	["数据库设计", "常荧", "电信313移动APP应用开发实训室", "191332100060", rgWeek(1, 4) + rgWeek(6, 10) + rgWeek(12, 14) + rgWeek(17, 18), 4, rgWeek(1, 4)],
	["瑜伽", "杨青", "体育馆形体房", "9030290", rgWeek(2, 4) + rgWeek(6, 18), 4, rgWeek(9, 10)],
	["UI界面设计", "苏晨", "电信310RFID技术应用实训室", "191332200010", rgWeek(1, 3) + rgWeek(5, 10) + rgWeek(12, 14) + rgWeek(17, 18), 5, rgWeek(1, 2)],
	["WEB前端技术", "张燕宁", "电信320第十机房", "191332200030", [2], 6, rgWeek(1, 4)],
	["WEB前端技术", "常荧", "电信313移动APP应用开发实训室", "191332100060", [5], 6, rgWeek(1,4)],
	["瑜伽", "杨青", "体育馆形体房", "9030290", [5], 4, rgWeek(9, 10)],
	["软件工程与UML", "张景峰", "电信318第八机房", "191332200020", [3], 7, rgWeek(1, 4)],
]

iCal = """BEGIN:VCALENDAR
METHOD:PUBLISH
VERSION:2.0
X-WR-CALNAME:课表
X-WR-TIMEZONE:Asia/Shanghai
CALSCALE:GREGORIAN
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
END:VTIMEZONE
"""

def get_location(loc):
	from re import search
	try:
		room = search("[0-9]{4}", loc).group()
	except AttributeError:
		room = "6666"
	if "电信" in loc:
		customGEO = """LOCATION:电信工程学院\\n
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=电信工程学院
 \\\\n:geo:39.771097,116.512190"""
	else: #Fallback
		customGEO = """LOCATION:电信工程学院\\n
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=电信工程学院
 \\\\n:geo:39.771097,116.512190"""
	customGEO = f'\n{customGEO}\nGEO:{customGEO.split("geo:")[1].replace(",", ";")}'
	return customGEO

runtime = datetime.now().strftime('%Y%m%dT%H%M%SZ')

for Class in classes:
	[Name, Teacher, Location, classID, classWeek, classWeekday, classOrder] = Class[:]
	Title = Name + " - " + Location
	
	customGEO = get_location(Location) # 通过 geo_location 匹配，也可替换为其他文本

	for timeWeek in classWeek:
		classDate = weeks[timeWeek][classWeekday]
		startTime = classTime[classOrder[0]]; endTime = classTime[classOrder[-1]]
		classStartTime = classDate + timedelta(minutes = startTime[0] * 60 + startTime[1])
		classEndTime = classDate + timedelta(minutes = endTime[0] * 60 + endTime[1] + 45)
		Description = classID + " 任课教师: " + Teacher + "。"

		StartTime = classStartTime.strftime('%Y%m%dT%H%M%S')
		EndTime = classEndTime.strftime('%Y%m%dT%H%M%S')
		singleEvent = f"""BEGIN:VEVENT
DTEND;TZID=Asia/Shanghai:{EndTime}
DESCRIPTION:{Description}
UID:CQUPT-{uid_generate(Name, StartTime)}
DTSTAMP:{runtime}
URL;VALUE=URI:{customGEO}
SUMMARY:{Title}
DTSTART;TZID=Asia/Shanghai:{StartTime}
END:VEVENT
"""
		iCal += singleEvent

iCal += "END:VCALENDAR"

with open("cqupt.ics", "w", encoding = "utf-8") as w:
	w.write(iCal)