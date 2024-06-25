## Laborit 💼💻 - Hiring Challenge
### Usando OpenAI, Langchain

* Olá, desenvolvedores! Me chamo Mauro Nascimento e estou participando do processo seletivo para Laborit. Onde utilza OpenAI e Langchain para gerar consultas no banco de dados mysql.

### Uso

* Crie um ambiente virtual com a ferramenta de sua preferência e instale o pacote **text2sql** Python

#### Exemplo

```python
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
```

```bash
> SELECT products.product_name,
                       order_details.quantity
                FROM   orders
                       INNER JOIN employees
                               ON orders.employee_id = employees.id
                       INNER JOIN order_details
                               ON order_details.order_id = orders.id
                       INNER JOIN products
                               ON products.id = order_details.product_id
                GROUP  BY products.product_name,
                          order_details.quantity
                ORDER  BY order_details.quantity DESC;
```

## Pré-requisito

* Certifique-se de definir corretamente seu `OPENAI_API_KEY`

## Autor

* [Mauro Nascimento](https://github.com/mauronascimento/)