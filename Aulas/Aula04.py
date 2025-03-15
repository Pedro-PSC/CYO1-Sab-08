#region Operadores de Comparação e Lógicos
'''
Operados de Comparação:

== → Se os valores comparados forem iguais;
!= → Se os valores comparados são diferentes;
>  → Se um dos valores comparados é maior que o outro;
<  → Se um dos valores comparados é menos que o outro;
>= → Se um dos valores comparados é maior ou igual ao outro;
<= → Se um dos calores comparados é menor ou igual ao outro.

Operadores Lógicos:
and (e → &&) → Verifica se ambas os dados são verdadeira para o resultado final ser verdadeiro
Ex.: True and True = True | True and False = False

or (ou → ||) → Verifica se apenas um dos dados é verdadeiro para o resultado ser verdadeiro
Ex.: True or True = True | True or False = True | False or False = False

not (não → !) → Verifica se o valor do dado é o oposto do valor atual
Ex.: !True = False | !False = True

'''
#endregion

#region Estrutura Condicional

'''
Uma estrutura condicional é usada para que possamos executar deternimados comandos
em momentos específicos com base em um condição verdadeira

Estrutura básica da condicional em python

if condição:
    o que vai executar

Estrutura de Múltiplas condições

if condição:
    código
elif condição:
    código
elif condição:
    codigo
else:
    código

Notas sobre a estrutura acima:
→ o "if" sempre inicia a estrutura de condição a mesca estrutura não pode possuir dois "if";
→ o "elif" pode ter a quantidade que for nescessária ele também precisa de condição assim como o "if";
→ O "else" não é obrigatória e não precisa de condição ele é usado para quando nenhuma das condições acima dele forem verdadeira (Executadas) e ainda você quer executar algo casa nada seja verdadeiro.
'''

#endregion

nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print("Aluno Aprovado!")
elif nota > 4 and nota < 6:
    print("Aluno de Recuperação!")
else:
    print("Aluno Reprovado!")