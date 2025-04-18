import mysql.connector
import matplotlib.pyplot as plt

con=mysql.connector.connect(
     user = 'root',
     host='localhost',
     database='expense_tracker',
     passwd='Mos2020june!')

cur=con.cursor()

cur.execute("DELETE FROM expenses WHERE category IS NULL OR amount IS NULL;")
con.commit()

cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category;")

results = cur.fetchall()

cur.close()
con.close()

category = []
amount = []

for row in results:
    category.append(row[0])
    amount.append(row[1])

plt.figure(figsize=(8,5))
plt.bar(category, amount, color='skyblue')
plt.ylim(0, max(amount)+ 50)
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.title("Total Expenses per Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

