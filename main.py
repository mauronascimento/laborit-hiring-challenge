from service.text_sql import TextSql
from service.text_sql_invoke import TextSqlInvoke
from service.questions import ALL_QUESTION

sql = TextSqlInvoke(model = "gpt-3.5-turbo")
# Insira a questão abaixo
#Exemplo
#send_openai = "How much do we have in total produtos?"
send_openai = "Quais são os produtos mais populares entre os clientes corporativos?"

#
for i, question in enumerate(ALL_QUESTION):
    if ALL_QUESTION[i].get("input") == send_openai:
        send_openai = []
        sql = TextSql(model="gpt-3.5-turbo")
        send_openai.append(ALL_QUESTION[i])


query = sql.query(send_openai)
print(query)
