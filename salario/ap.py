# FUNÇÕES PARAMETRIZADAS


# verificar quanto o calaborador ganha por hora 
def valor_hora(salario,carga):
    return salario/carga


# verificar quanto ganha por hora extra
def valor_hora_extra(valor_hora):
    return valor_hora * 1.5


# quantas horas extras ele fez
def quantidade_vesus(quan, h_e_t):
    return quan * h_e_t



def quantidade_h():
    quantidade = float(input('Quantidade hora extra: '))
    return quantidade


# qual o salário que ele ganha no final do mês
def sal(q_h, salario):
    return q_h + salario


def hr_system():
    while True:    
        print('---' * 10)
        print('Calculo de horas: ')
        salario = float(input('Salário: '))
        carga = float(input('Carga horária: '))


        # função 1
        valor_da_hora  =  valor_hora(salario, carga)
        print('Salario hora: ', round(valor_da_hora,2))


        # função 2
        extra = valor_hora_extra(valor_da_hora)
        print('Extrar :', float(round(extra,2)))


        # função 3
        quant = quantidade_h()
        print('quantidade de extra realizadas:', quant)
        
        total_extra =  quantidade_vesus(extra,quant)
        print('Extra a receber  -  R$', float(round(total_extra,2)))



        # função 4
        salario_ =  sal(total_extra, salario)
        print('Salario total - R$',float(round(salario_,2)))




hr_system()
2

input('DIGITE ENTER PARA SAIR')
