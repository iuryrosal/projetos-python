from database import DatabaseClient

database_1 = DatabaseClient(1234)
database_2 = DatabaseClient(4567)

print(database_1.get_connection())

print(database_2.get_connection())

if database_1 == database_2:
  print("São iguais!")
else:
  print("São distintas!")

database_1.set_classmates(["Iury"])
print(database_1.get_classmates())

database_2.set_classmates(["Laura"])
print(database_2.get_classmates())
print(database_1.get_classmates())