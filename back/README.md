# Gerência de configuração de mudanças
Criação do banco UFRN

# Integrantes:
* Victor Morais
* Joyce Beatriz
* Keystone Barreto

# Rodando o projeto

basta executar os seguintes comandos:
```
pip install -r requirements.txt

flask --app main run
```

# Especificação dos requisitos

- [x] Cadastrar Conta -  Solicita um número e cria uma conta com este número e saldo igual a zero
- [x] Consulta Saldo - Solicita um número de conta e exibe o saldo da conta
- [x] Crédito - Solicita um número e valor e atualiza a conta informada acrescentando o valor informado ao saldo
- [x] Débito - Solicita um número e valor. Atualiza a conta informada subtraindo o valor informado ao saldo
- [ ] Transferência - Solicita o número de conta de origem, número de conta de destino e valor a ser transferido. Realiza o débito da conta de origem e o crédito na conta destino

# Requisitos adicionais
- [x] As contas podem ter saldo negativo
- [x] Não existe limite de número de contas que podem ser criadas
- [x] A conta deve ter apenas os atributos número e saldo