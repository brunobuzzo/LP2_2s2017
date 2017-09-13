def conta_vogais(palavra):
    palavra = palavra.lower() 
    contagem = {}
    vogais = ['a','e','i','o','u']
    for i in vogais:
        if i in palavra:
            contagem[i] = palavra.count(i)
    return contagem

def test_vogais():
    print('vogais')
    assert conta_vogais('esse e o teste um') == {'e': 5, 'o': 1, 'u': 1}
    assert conta_vogais('agora esta testando o dois') == {'a': 4, 'e': 2, 'i': 1, 'o': 4}
    assert conta_vogais('este exercicio foi complicado') == {'a': 1, 'e': 4, 'i': 4, 'o': 4}
    assert conta_vogais('o programa esta testando este agora') == {'a': 6, 'e': 4, 'o': 4}
    assert conta_vogais('graças a Deus terminei o exercicio') == {'a': 3, 'e': 5, 'i': 4, 'o': 2, 'u': 1}
