import matplotlib.pyplot as plt
#following are for calling a SQL database; not sure if they work
'''import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="john",         # your username
                     passwd="megajonhy",  # your password
                     db="jonhydb")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
#for row in cur.fetchall():
#    print row[0]'''

plt.figure()

#plots w example data
x_series = []
y_series = []

#labels
plt.xlabel("Hours")
plt.ylabel("Temperature")
plt.title("Temperature Over 24H. Period")

#limits
#the graph would only show up to the current hour when the user requests it
plt.xlim(0,max(x_series))
plt.ylim(25,45)

#would need to pull from the database; this is where the graph would reset
if ("""hour in database == 00:00 or 0.00"""):
    bbt = min(y_series)
    plt.plot(x_series, y_series)
    #save as png
    plt.savefig("graph_example.png")
    #new graph
    plt.figure()
    return 0
else:
    #would only graph at a whole hour eg. 8:00; need database
    while ("""whole hour or no float"""):
          x_series = x_series.append("""add hour to list""")
          y_series = y_series.append("""temperature""")
          plt.plot(x_series, y_series)
          #save as png
          plt.savefig("temp_day_graph.png")    
          break
    

#part of SQL calling
#db.close()