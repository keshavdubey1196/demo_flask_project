"""
# cur.execute("create table books (id serial primary key, title varchar (150) NOT NULL, author varchar (50) NOT NULL,pages integer NOT NULL)")
# cur.execute(CREATE TABLE IF NOT EXISTS fyndnine (emp_id serial primary key,
#                                                     name varchar(100),
#                                                     salary integer,
#                                                     address varchar(200));)
# print("Table created")
# con.commit()

# cur.execute(insert into fyndnine (name, salary, address)
#                 values ('Harshita', 22000, 'Sector 59 Noida');)
# con.commit()

# print("Values inserted")
cur.execute("select * from fyndnine")
print(cur.fetchall())
"""

# import zeep

# i_am_client = zeep.Client(
#     wsdl="https://ecs.syr.edu/faculty/fawcett/Handouts/cse775/code/calcWebService/Calc.asmx?WSDL")


# if __name__ == "__main__":
# print(i_am_client.service.Add(2, 3))
# print(i_am_client.service.Subtract(2, 9))


# db_dict = {"db_user": db_user,
#            "db_passwd": db_passwd,
#            "db_host": db_host,
#            "db_port": db_port,
#            "db_name": db_name}
