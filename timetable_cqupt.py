from hashlib import md5
from datetime import datetime, timedelta

classTime = [None, (8, 15), (9, 10), (10, 15), (11, 10), (13, 15), (14, 10),
	(15, 5), (16, 0)]
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
	["WEB前端技术", "张燕宁", "电信320第十机房", "abc", oeWeek(2, 6, 0) + rgWeek(7, 10) + rgWeek(12, 14) + [17] , 1, rgWeek(1, 4)],
	["软件工程与UML", "张景峰", "电信318第八机房", "abc", rgWeek(1, 2) + oeWeek(4, 6, 0) + rgWeek(12, 14) + rgWeek(17, 18), 2, rgWeek(1, 4)],
	["面向对象程序设计", "朱孔涛", "电信307第五机房", "abc", rgWeek(1, 4) + rgWeek(6, 10) + rgWeek(12, 14) + rgWeek(17, 18), 3, rgWeek(1, 4)],
	["形势与政策2", "李晓", "电信110阶梯教室", "abc", rgWeek(7, 8), 3, rgWeek(7, 8)],
	["数据库设计", "常荧", "电信313移动APP应用开发实训室", "abc", rgWeek(1, 4) + rgWeek(6, 10) + rgWeek(12, 14) + rgWeek(17, 18), 4, rgWeek(1, 4)],
	["UI界面设计", "苏晨", "电信310RFID技术应用实训室", "abc", rgWeek(1, 3) + rgWeek(5, 10) + rgWeek(12, 14) + rgWeek(17, 18), 5, rgWeek(1, 2)],
	["WEB前端技术", "张燕宁", "电信320第十机房", "abc", [2], 6, rgWeek(1, 4)],
	["WEB前端技术", "常荧", "电信313移动APP应用开发实训室", "abc", [5], 6, rgWeek(1,4)],
	["软件工程与UML", "张景峰", "电信318第八机房", "abc", [3], 7, rgWeek(1, 4)],
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
	if "YF" in loc: 
		customGEO = """LOCATION:重庆邮电大学-逸夫科技楼\\n崇文路2号重庆邮电大学
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 -逸夫科技楼\\\\n崇文路2号重庆邮电大学:geo:29.535617,106.607390"""
	elif "SL" in loc: 
		customGEO = """LOCATION:重庆邮电大学数理学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 数理学院\\\\n崇文路2号重庆邮电大学内:geo:29.530599,106.605454"""
	elif "综合实验" in loc or "实验实训室" in loc: 
		customGEO = """LOCATION:重庆邮电大学综合实验大楼\\n南山路新力村
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 综合实验大楼\\\\n南山路新力村:geo:29.524289,106.605595"""
	elif "风华" in loc or loc == "运动场1": 
		customGEO = """LOCATION:风华运动场\\n南山街道重庆邮电大学5栋
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=
 风华运动场\\\\n南山街道重庆邮电大学5栋:geo:29.532757,106.607510"""
	elif "太极" in loc:
		customGEO = """LOCATION:重庆邮电大学-太极体育场\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 -太极体育场\\\\n崇文路2号重庆邮电大学内:geo:29.532940,106.609072"""
	elif "乒乓球" in loc:
		customGEO = """LOCATION:风雨操场(乒乓球馆)\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=风雨操场(乒乓球馆)\\\\n
 崇文路2号重庆邮电大学内:geo:29.534230,106.608516"""
	elif "篮球" in loc or "排球" in loc:
		customGEO = """LOCATION:重庆邮电学院篮球排球馆\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电学院篮球排球馆\\\\n
 崇文路2号重庆邮电大学内:geo:29.534025,106.609148"""
	elif room[0] == "1":
		customGEO = """LOCATION:重庆邮电大学-光电工程学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 -光电工程学院\\\\n崇文路2号重庆邮电大学内:geo:29.531478,106.605921"""
	elif room[0] == "2": 
		customGEO = """LOCATION:重庆邮电大学二教学楼\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 二教学楼\\\\n崇文路2号重庆邮电大学内:geo:29.532703,106.606747"""
	elif room[0] == "3": 
		customGEO = """LOCATION:重庆邮电大学第三教学楼\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 第三教学楼\\\\n崇文路2号:geo:29.535119,106.609114"""
	elif room[0] == "4": 
		customGEO = """LOCATION:重庆邮电大学第四教学楼\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 第四教学楼\\\\n崇文路2号:geo:29.536107,106.608759"""
	elif room[0] == "5": 
		customGEO = """LOCATION:重庆邮电大学-国际学院\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 -国际学院\\\\n崇文路2号重庆邮电大学内:geo:29.536131,106.610090"""
	elif room[0] == "8": 
		customGEO = """LOCATION:重庆邮电大学八教学楼A栋\\n崇文路2号重庆邮电大学内
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=重庆邮电大学
 八教学楼A栋\\\\n崇文路2号重庆邮电大学内:geo:29.535322,106.611020"""
	else: #Fallback
		customGEO = """LOCATION:重庆邮电大学\\n崇文路2号
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-TITLE=
 重庆邮电大学\\\\n崇文路2号:geo:29.530807,106.607617"""
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