## Laborit 💼💻 - Hiring Challenge
### Usando OpenAI, Langchain

<hr />

<img src="https://github.com/weet-ai/text2sql-workshop/blob/main/img/nosql.png?raw=true"/>

### Overview

* This repo demonstrates the power of **Large Language Models** and **Generative AI** for simplifying access to data: instead of querying a database using **SQL**, why not doing so using **Natural Language**?
* **text2sql** is a basic Python package which ships with [Langchain](https://www.langchain.com/). It contains simple logic for connecting to a local [Postgresql](https://www.postgresql.org/) instance, and by leveraging Langchain's `create_sql_query_chain`, it obtains metadata from our local DB instances and creates multiple prompts which are executed against an LLM (in our case, [OpenAI](https://openai.com/) ChatGPT).
* As a result, we are able to convert questions from Natural Language to SQL Queries that are compliant with Postgresql's dialect.

### Usage

* Crie um ambiente virtual com a ferramenta de sua preferência e instale o pacote **text2sql** Python

#### Example

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

## Prereqs

* Certifique-se de definir corretamente seu `OPENAI_API_KEY`

## Authors

* [Rafael Pierre](https://github.com/mauronascimento/)