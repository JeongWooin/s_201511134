use myDB
show dbs
show tables
db.myCol.insert({"Persons":[{"id":"201511134","이름":"정우인"},{"id":"201511127","이름":"임예지"}]})
db.myCol.find({"Persons.이름":"정우인"})