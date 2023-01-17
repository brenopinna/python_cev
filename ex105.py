def notas(* valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-' * 30)
    resp = {'total': len(valores), 'maior': max(valores),
            'menor': min(valores), 'média': round((sum(valores) / len(valores)), 3)}
    if sit:
        if resp['média'] >= 7:
            resp['situação'] = 'BOA'
        elif 5 <= resp['média'] < 7:
            resp['situação'] = 'RAZOÁVEL'
        else:
            resp['situação'] = 'RUIM'
    return resp


print(notas(5.5, 9.5, 10, 6.5, sit=True))
help(notas)
