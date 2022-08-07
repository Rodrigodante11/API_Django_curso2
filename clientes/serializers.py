from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import cpd_valido, nome_valido, rg_valido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpd_valido(data['cpf']):
            raise serializers.ValidationError({'CPF': 'O CPF deve ter 11 Digitos'})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'Nome': 'Nao inclua Numeros no Nome'})

        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'RG': 'O RG  deve ter 9 Digitos'})
        return data

    # def validate_celular(self, celular):
    #     if len(celular) != 11:
    #         raise serializers.ValidationError('O celular  deve ter 9 Digitos no Minimo')
    #     return celular
