def media_aluno(nome,n1,n2):
    aluno = {}
    media = (n1+n2)/2
    aluno[nome] = media
    return aluno

def test_aluno():
    print('aluno media')
    assert media_aluno('bruno', 4.0, 5.0) == {'bruno': 4.5}
    assert media_aluno('joao', 8.5, 9.7) == {'joao': 9.1}
