## Python 大学生课表 (.ics) 生成

**如果你是重庆邮电大学学生，请访问 [CQUPT-ics](https://github.com/qwqVictor/CQUPT-ics) 项目，可自动生成学生课表。**

![效果图](render_2021.jpg)

\* **2021 年 9 月更新**：此代码于 2021 年 3 月增加了日历项 UID 生成，在此之前生成的 ics 文件可以正常导入 Apple 日历，但在 iOS「已订阅的日历」设置中订阅 ics 可能存在问题；此代码于 2021 年 9 月修改了 UID 生成方式，解决了在订阅日历中由于随机 UID 出现日历项不断重置的问题。敬请使用更新后的代码。

## 简介

iCalendar 是广泛使用的日历数据交换标准，在诸如 Apple 日历、Google Calendar 的日历 app 中创建日历项，不仅可清晰的了解日程安排，更可体验 iOS、Android 系统为日历提供的各种功能：计划出行时间、日程提醒、如 Siri 与 Google Assistant 等智能语音助理自动化服务等。

不过，并非所有学校都为学生提供 ics 日历，因此本代码旨在用 Python 3 协助你创建一个自己的 ics 日历课表。

## 功能

* 经测试，兼容 Apple 日历、Google Calendar、Outlook Calendar 等日历应用，**支持上述应用的日历订阅**（如果以本代码生成的文件创建日历订阅）
* 支持录入各种信息，示例代码中包含：教室、课程名称、教师、必修/选修状态等
* 支持多种课程时间安排：**单独的周数，范围的周数，奇偶周数**，如 "**第2周，5 至 11 周中的单数周，13 至 17 周**"
* 支持添加教学楼信息，其中 **Apple 日历还支持教学楼 GPS 定位** ，在日历项中添加教学楼，就可利用 iOS 的 Siri 分析功能在多个 app 中获得附加功能
* 导入到系统日历后，支持诸多由操作系统提供的日历功能：例如，在 iOS 设备中添加日历项后，你可以直接向 Siri 询问：「我下周五有什么日程？」获得下周五的课表；或是在 Apple Watch 表盘上显示下一个课程的时间；或是使用 Shortcut 捷径进行更多操作。

## 使用

请调整代码中的以下内容以适配自己的课表：

```python
classes = [
	["信号与系统", "张三", "5203", "", rgWeek(1, 12), 1, [3, 4]],
	# 信号与系统，张三老师，5203 教室，1 - 12 周，周一，3、4 节上课
 
	["面向对象程序设计", "李四", "计算机教室（六）(综合实验楼B405/B406)", "", oeWeek(3, 17, 1), 3, [3, 4]],
	# 面向对象程序设计，李四老师，综合实验楼，3 - 17 周单周，周三，3、4 节上课
 
	["大学体育", "王五", "风华运动场", "", oeWeek(2, 16, 0), 3, [3, 4]],
	# 大学体育，王五老师，风华运动场，2 - 16 周双周，周三，3、4 节上课
 
	["马克思主义基本原理概论", "赵六", "3105", "", rgWeek(1, 8) + rgWeek(10, 16), 3, [5, 6, 7]],
	# 马克思主义基本原理概论，赵六老师，1 - 8 周及 10 - 16 周，周三，5、6、7 节上课
]
```

1. 在代码前端的 `for i in range(1, 30):` 中，30 表示将会预生成的日历周数，如果很不幸你这学期有超过 30 周的课，应该修改 30 为最大周数 + 1（此数字可以设置的更大）。

2. **classTime** 为每节课的**开始上课**时间，以元组形保存。预留第 [0] 项为 None 是为了让后续读取第 1 节课时可以按照常规思路取第 [1] 项，而非第 [0] 项。请依次填写每节课的 24 小时制上课时间：例如 8:00 上课，则录入 `(8, 0)`；下午 7:50 上课，则录入 `(19, 50)`。

3. 修改 **starterDay** 为本学期第一周星期一的日期。

4. 修改 **classes** 中的课程信息，由于不同学校课表可能含有不同信息，请参考源代码中的课表填写，并直接在后续定义中作出相应修改：

   在 `for Class in classes:` 后，定义了不同的变量，均可进行自定义。最终，「**Title**」变量为日历项的标题，「**Description**」变量为日历项的备注，均可根据自己喜好修改。

   代码中给出的「**Title**」是类似「高等数学 - 5200」的样式，「**Description**」则包括该课程的一些其他信息，如教学班号、教师姓名、学分、必修/选修等。

   **如何设置课程在哪一周？**
   单独周：请改为数组形式，例如 [2]；
   范围周：你可以使用 `rgWeek` 函数，例如 `rgWeek(3, 7)` 代表第三周到第七周；
   奇数周：你可以使用 `oeWeek` 函数，例如 `oeWeek(2, 9, 1)` 代表第二周到第九周的单数周，将 1 改为 0 即为偶数周。

   **如何设置课程在哪一节？**
   一节课：请改为数组形式，例如 [2]；
   范围课，你可以使用 `rgWeek` 函数，例如 `rgWeek(3, 7)` 代表第三节一直上到第七节；

   当然，在任意时候你都可以直接用数组列举出所有的值，例如 `[2, 3, 5, 7, 10, 12, 16]`。

   如果周数、节数是由多项组成，请使用加法。例如，第2周，5-11单数周，13-17 周，则为：

```python
[2] + oeWeek(5, 11, 1) + rgWeek(13, 17)
```

5. 在 `classEndTime` 赋值行末尾将 `+ 45` 修改为加每节课的时长，一节课 40 分钟则为 `+ 40`。

## 生成后使用

* 要了解什么是日历订阅，如何进行日历订阅，请了解[文档](https://github.com/qwqVictor/CQUPT-ics/blob/main/docs/ImportOrSubscribe.md)；
* 要了解生成日历文件后如何导入或添加日历订阅到 Apple 设备，请了解[文档](https://github.com/qwqVictor/CQUPT-ics/blob/main/docs/ImportOrSubscribe.md)。

## 为代码添加定位信息

* 如果你只是想在日历项的地理位置中增加一个教学楼的名称

  你可以直接使用下述内容代替代码中 110 行附近的的 customGEO。

  ```python
  customGEO = "LOCATION:<你想要的作为教学楼显示名的任何文本>"
  ```

  请留意转义符号的使用，例如要表示 \n 需要使用 \\\\n。

* 如果你使用 Apple Maps，并希望添加教学楼的 **GPS 坐标**定位信息：

  Apple 日历使用了「X-APPLE-STRUCTURED-LOCATION」和「X-APPLE-MAPKIT-HANDLE」来记录 Apple Maps 位置信息，这一项包含位置文字和坐标。一个样例内容如下:

  ```C++
  LOCATION:重庆邮电大学综合实验大楼\n南山路新力村
  X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKIT-HANDLE=;X-APPLE-RADIUS=500;X-TITLE=重庆邮电大学综合实验大楼\\n南山路新力村:geo:29.524289,106.605595
  ```

  其中，`LOCATION `和 `X-TITLE` 中的地址必须**一字不差**的和 Apple Maps 结果对应，不得修改！

  为了保证可用性，这一段文本只能手动创建日历项并导出提取，以下是导出方法。

  * 打开 macOS 日历 app，任意创建一个日历项，添加你想要用在代码中的地理位置。

  * 请确定刚刚创建的日历项在哪一个日历里，然后点击 macOS 工具栏中的 文件 -> 导出 -> 导出，保存 ics 文件。

  * 用文本编辑器打开 ics 文件，找到一个由 `BEGIN:VEVENT` 开头的你刚刚建立的包含位置的 VEVENT 项目。

  * 你将可找到类似以下两个文段：

  ```C++
  LOCATION:重庆大学虎溪校区\n大学城南路55号    
  X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-APPLE-MAPKITHANDLE=1234567890ABCDEFGHIJ;X-APPLE-RADIUS=925.4324489259043;X-TITLE=重庆大学虎溪校区\\n大学城南路5号:geo:29.592566,106.299150
  ```

  这里「X-APPLE-MAPKITHANLE」中的「1234567890ABCDEFGHIJ」是一串随机文字，可以全部去掉（注意不要删除后面的分号），「RADIUS」没有必要修改但可以稍改，而「TITLE」中的文字务必不要修改！

  代码中，定义了名为 `get_location` 的函数，提供了重庆邮电大学部分教学楼和场所的匹配方式，供参考。请仍留意转义符号的使用，例如要表示 \n 需要使用 \\\\n。

## 联系作者

* 直接提交 Issue
* 微博 [@赛艇的同学](http://weibo.com/u/3566216663 "@赛艇的同学")

