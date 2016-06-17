import sqlite3

db = sqlite3.connect('ptt.db')

keyword = input('Keyword:')
articles = db.execute('select * from articles where `LABELED` = 0 and `CONTENT` like \'%'+keyword+'%\'').fetchall()
for i in articles:
    print('================================================================')
    print(i[1]) #title
    cmd = input('>')
    if(cmd == 'y'):
        print('YES')
        print(i[0])
        db.execute('UPDATE articles SET `POLITICAL`=1, `LABELED`=1 WHERE id='+str(i[0]))
        db.commit()
        flag = True
    elif(cmd == 'n'):
        print('NO')
        print(i[0])
        db.execute('UPDATE articles SET `POLITICAL`=0, `LABELED`=1 WHERE id='+str(i[0]))
        db.commit()
        flag = True
    else:
        cont = i[5].split('\n') #content splitted
        flag = False
        l = 0
        while not flag:
            if(l < len(cont)):
                while(cont[l] == '' and l < len(cont) - 1):
                    l += 1
                print(cont[l])
            cmd = input('>')
            if(cmd == 'y'):
                print('YES')
                db.execute('UPDATE articles SET `POLITICAL`=1, `LABELED`=1 WHERE id='+str(i[0]))
                db.commit()
                flag = True
            elif(cmd == 'n'):
                print('NO')
                db.execute('UPDATE articles SET `POLITICAL`=0, `LABELED`=1 WHERE id='+str(i[0]))
                db.commit()
                flag = True
            elif(l < len(cont) - 1):
                l += 1
