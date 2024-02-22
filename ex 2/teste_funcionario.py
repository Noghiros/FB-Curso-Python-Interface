from funcionario import Funcionario

funcionario = Funcionario('Stefano','stefanoc.stringhini@gmail.com')

funcionario.cadastro_hora('Jan',200)
funcionario.cadastro_hora('Fev',200)
funcionario.cadastro_salario_hora('Jan',25)
funcionario.cadastro_salario_hora('Fev',30)
print(funcionario)
print(funcionario.calcula_salario('Jan'))
print(funcionario.calcula_salario('Fev'))