import xlrd                               # xlrd can read the .xls file

ipt = raw_input("Please input:")          # Input,and handle
ipt = ''.join(ipt.split())


book = (xlrd.open_workbook(ipt))          # Open the .xls file



sh = book.sheet_by_index(0)             # To the first sheet


day=''
lesson=''



for i in range(0,sh.nrows):                           # Find the start of week
    for j in range(0,sh.ncols):
        if(sh.cell_value(i,j)==u"星期一"):
            a,b=i,j
            print a
            print b
            print sh.cell_value(8,6)
            break
                                                            # Two functions to simplify the process
def Lessons (m):
    if (m == 3):
        lesson = u"第一二节"
    elif (m == 4):
        lesson = u"第三节"
    elif (m == 5):
        lesson = u"第四五节"                                #  Confirm the lesson
    elif (m == 6):
        lesson = u"第六七节[下午]"
    elif (m == 7):
        lesson = u"第八九节"
    elif (m == 8):
        lesson = u"第十，十一，十二节"
    return lesson

def Days (n):
    if (n == 2):
        day = u"星期一"                                    # Confirm the day
    elif (n == 3):
        day = u"星期二"
    elif (n == 4):
        day = u"星期三"
    elif (n == 5):
        day = u"星期四"
    elif (n == 6):
        day = u"星期五"
    return day


for n in range(2,7):                                    # Main function 
    for m in range(3, 9):
       if(sh.cell_value(m,n)==''):
            lesson = Lessons(m)
            day = Days(n)
            print day + lesson + u"有空"
