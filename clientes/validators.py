from rest_framework import serializers
import re
from validate_docbr import CPF


def cpd_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(numero_rg):
    return len(numero_rg) == 9


def validate_celular(numero_celular):
    """Verifica se o celular valido (35 99808-1515)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    return re.findall(modelo, numero_celular)




