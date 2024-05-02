email_tmpl = """
   ...: Olá, %(nome)s
   ...:
   ...: Tens interesse em comprar %(produto)s?
   ...:
   ...: Este produto é ótimo para resolver seus problemas de %(texto)s
   ...:
   ...: Clique agora em %(link)s
   ...:
   ...: Apenas %(quantidade)d disponíveis!
   ...:
   ...: Preço promocional %(preco).2f
   ...: """

In [5]: clientes = ["Maria", "Joao", "Raphael"]

In [6]: for cliente in clientes:
   ...:     print(email_tmpl % {"nome": cliente, "produto":"caneta", "
   ...: texto": "Escrever muito bem", "link":"https://canetaslegais.co
   ...: m", "quantidade": 1, "preco": 50.5})
   ...:
