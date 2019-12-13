# Conversor de NFA para DFA
Conversor de um Autômato Finito Não-Determinístico para um Autômato Finito Determinístico  
Projeto final da disciplina **Linguagens Formais e Autômatos**

## Tecnologias Usadas:
🔵 Python

## Como Usar:

Para converter um autômato NFA para um DFA basta digitar o seguinte comando no terminal:
```
python3 main.py 'automato.txt'
```
O arquivo .txt deve representar um NFA e ter a seguinte estrutura:

```
NOME_DO_AUTOMATO=({q0,q1,q2,q3},{a,b},q0,{q1,q3})
Prog
(q0,a)=q1
(q0,b)=q2
(q1,b)=q2
(q2,a)=q3
(q2,a)=q2
(q3,a)=q3
(q3,b)=q2
```
