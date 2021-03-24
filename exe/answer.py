def fun01():
    a_list = []
    b_list = []
    for i in range(50, 101):
        if i % 2 == 0 and i % 3 == 0:
            a_list.append(i)
        if i % 3 == 0 and i % 5 == 0:
            b_list.append(i)
    print(a_list)
    print(b_list)


def fun02():
    files = ['zy1.docx', 'zy2.xlsx', 'zy3.txt', 'zy4.docx', 'zy5.doc']
    docxfile = []
    for i in files:
        r1 = i.find('.docx')
        r2 = i.find('.doc')
        if r1 != -1 or r2 != -1:
            docxfile.append(i)
    print(docxfile)


def fun03():
    a = {'one':[], 'two':[]}
    for i in range(50, 101):
        if i % 2 == 0 and i % 3 == 0:
            a['one'].append(i)
        if i % 3 == 0 and i % 5 == 0:
            a['two'].append(i)
    print(a)


if __name__ == '__main__':
    # fun01()
    # fun02()
    fun03()
