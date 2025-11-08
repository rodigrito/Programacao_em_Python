ecommerce = {
     
        'celulares':{
             'SAMSUNG':1500.66,
             'IPHONE':3000.0
        },


        'roupas':{
            'camiseta':150.0,
            'calça':250.0


        },
        'acesorios':{
            'relogio':500.0,
            'anel':90.0
        }



}




carrinho = []
valores  =  [] # criar a lista valores


deseja = input('deseja comprar - sim / não ?')
while deseja == 'sim':
    secao = input('Secao - celulares roupas ou acesorios')
    p1 = input(f'Produto: {ecommerce[secao]}')
    carrinho.append(p1) # adionamos o produto
    valores.append(ecommerce[secao][p1])
    print(carrinho)
    total = sum(valores)
    print('R$', total)
    deseja = input('Deseja continuar   - sim / não?')
else:
    print('Obrigada volte sempre!')