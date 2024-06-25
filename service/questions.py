ALL_QUESTION = [
    {
        "input": "Quais são os produtos mais populares entre os clientes corporativos?",
        "query": """ SELECT products.product_name,
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
                ORDER  BY order_details.quantity DESC;  """
    },
    {
        "input": "Quais são os produtos mais vendidos em termos de quantidade?",
        "query": """SELECT products.product_name, 
                       order_details.quantity
                FROM   orders
                       INNER JOIN order_details
                               ON order_details.order_id = orders.id
                       INNER JOIN products
                               ON products.id = order_details.product_id
                GROUP  BY products.product_name,
                          order_details.quantity
                ORDER  BY order_details.quantity DESC;"""
    },
    {
        "input": "Qual é o volume de vendas por cidade?",
        "query": """
                 SELECT customers.city,
                       employees.city,
                       order_details.quantity
                FROM   orders
                       INNER JOIN employees
                               ON orders.employee_id = employees.id
                       INNER JOIN customers
                               ON orders.customer_id = customers.id
                       INNER JOIN order_details
                               ON order_details.order_id = orders.id
                       INNER JOIN products
                               ON products.id = order_details.product_id
                GROUP  BY customers.city,
                          employees.city,
                          order_details.quantity
                ORDER  BY order_details.quantity DESC;  
    """
    },
    {
        "input": "Quais são os clientes que mais compraram?",
        "query": """
             SELECT customers.first_name,
                   customers.city,
                   employees.first_name,
                   employees.city,
                   order_details.quantity
            FROM   orders
                   INNER JOIN employees
                           ON orders.employee_id = employees.id
                   INNER JOIN customers
                           ON orders.customer_id = customers.id
                   INNER JOIN order_details
                           ON order_details.order_id = orders.id
                   INNER JOIN products
                           ON products.id = order_details.product_id
            GROUP  BY customers.first_name,
                      customers.city,
                      employees.first_name,
                      employees.city,
                      order_details.quantity
            ORDER  BY order_details.quantity DESC;  
    """
    },
    {
        "input": "Quais são os produtos mais caros da loja?",
        "query": """
             SELECT products.product_name,
                   products.list_price
            FROM   products
            ORDER  BY list_price DESC;   
    """
    },
    {
        "question": "Quais são os fornecedores mais frequentes nos pedidos?",
        "query": """
                 SELECT suppliers.company,
                       suppliers.first_name,
                       purchase_order_details.quantity
                FROM   purchase_orders
                       INNER JOIN purchase_order_details
                               ON purchase_orders.id = purchase_order_details.purchase_order_id
                       INNER JOIN suppliers
                               ON suppliers.id = purchase_orders.supplier_id
                GROUP  BY suppliers.company,
                          suppliers.first_name,
                          purchase_order_details.quantity
                ORDER  BY purchase_order_details.quantity DESC;  
    """
    },
    {
        "input": "Quais os melhores vendedores?",
        "query": """
 
    """
    },
    {
        "input": "Qual é o valor total de todas as vendas realizadas por ano?",
        "query": """

    """
    },
    {
        "input": "Qual é o valor total de vendas por categoria de produto?",
        "query": """

    """
    },
    {
        "input": "Qual o ticket médio por compra?",
        "query": """

"""
    },
]