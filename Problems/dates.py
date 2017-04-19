import calendar

n = int(input())
date = []
for i in range(n):
    a = input()
    for ii in range(len(a)):
        try:
            int(a[ii])
            int(a[ii+1])
            int(a[ii+2])
            int(a[ii+3])
            year = int(a[ii:ii+4])
            if a[ii+4] == '-':
                if int(a[ii+5:ii+6]) < 13:
                    if a[ii+7] == '-':
                        month = int(a[ii+5:ii+7])
                        day = int(a[ii+8:ii+10])
                        if month == 1:
                            if day == 31:
                                date.append(a[ii:ii+10])
                        elif month == 2:
                            if calendar.isleap(year):
                                if day <= 29:
                                    date.append(a[ii:ii+10])
                            elif day <= 28:
                                date.append(a[ii:ii+10])
                        elif month == 3:
                            if day <= 31:
                                date.append(a[ii:ii+10])
                        elif month == 4:
                            if day <= 30:
                                date.append(a[ii:ii+10])
                        elif month == 5:
                            if day <= 31:
                                date.append(a[ii:ii+10])
                        elif month == 6:
                            if day <= 30:
                                date.append(a[ii:ii+10])
                        elif month == 7:
                            if day <= 31:
                                date.append(a[ii:ii+10])
                        elif month == 8:
                            if day <= 31:
                                date.append(a[ii:ii+10])
                        elif month == 9:
                            if day <= 30:
                                date.append(a[ii:ii+10])
                        elif month == 10:
                            if day <= 31:
                                date.append(a[ii:ii+10])
                        elif month == 11:
                            if day <= 30:
                                date.append(a[ii:ii+10])
                        elif month == 12:
                            if day <= 31:
                                date.append(a[ii:ii+10])
        except:
            pass
for i in range(len(date)):
    print(date[i])

