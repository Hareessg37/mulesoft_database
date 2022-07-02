import sqlite3 as sql

connection = sql.connect("dbaseMovies.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('Mankatha','Ajith Kumar','Trisha Krishnan','Venkat Prabhu',2011)")
pointer.execute("INSERT INTO MOVIES VALUES('The Dark Knight Rises','Christian Bale','Anne Hathaway','Christopher Nolan',2012)")
pointer.execute("INSERT INTO MOVIES VALUES('Interstellar','Matthew McConaughe','Anne Hathaway','Christopher Nolan',2014)")
pointer.execute("INSERT INTO MOVIES VALUES('Your Name','Taki Tachibana','Mitsuha Miyamizu','Makoto Shinkai',2016)")

allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))

actressQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTRESS = 'Anne Hathaway'").fetchall()
for i in actressQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
