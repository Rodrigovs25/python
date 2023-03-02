
>>> dic = {}
>>> dic['ze'] = 300
>>> dic['mauricio'] = 100
>>> dic['heloisa'] = 150
>>> dic['ze']
300
>>> dic
{'mauricio': 100, 'ze': 300, 'heloisa': 150}
>>> dic['ze'] = 200
>>> dic
{'mauricio': 100, 'ze': 200, 'heloisa': 150}
>>> dic.keys() # o método keys() retorna a lista de chaves do dicionário. Um método nada mais é que uma função associada
# a um objeto, que deve ser invocada usando a sintaxe objeto.metodo(). Em nosso exemplo temos dic.keys().
['mauricio', 'ze', 'heloisa']
>>> dic['paulo']
Traceback (innermost last):
    File '', line 1, in ?
     dic['paulo']
KeyError: paulo
>>> dic.has_key('heloisa') # para verificar se uma determinada chave existe, usamos o método has_key() (tem_chave).
# Os exemplos mostram que has_key() retorna 1 quando a chave existe, e zero quando ela não existe.
True
>>> dic.has_key('paulo')
False