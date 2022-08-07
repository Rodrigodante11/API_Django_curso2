from rest_framework import serializers


def cpd_valido(numero_cpf):
    return len(numero_cpf) == 11


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(numero_rg):
    return len(numero_rg) == 9



