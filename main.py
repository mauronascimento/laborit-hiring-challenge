from service.text_sql import TextSql
sql = TextSql(model = "gpt-3.5-turbo")
query = sql.query(
    [
        {
            "input": "What are the most popular products among corporate customers?",
            "query": "select products.product_name, order_details.quantity from orders inner join employees on orders.employee_id = employees.id inner join order_details on order_details.order_id = orders.id inner join products on products.id = order_details.product_id order by order_details.quantity desc;"
        },
        {
            "input": "What are the best-selling products in terms of quantity?",
            "query": "select products.product_name, order_details.quantity from orders inner join order_details on order_details.order_id = orders.id inner join products on products.id = order_details.product_id order by order_details.quantity desc;"
        },
    ]
)
print(query)