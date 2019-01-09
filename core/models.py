from django.db import models

from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATE_FORMAT = "d M Y"
pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"


class Tema(models.Model):
    nome = models.CharField('Nome', max_length=100)
    valor_aluguel = models.DecimalField('Valor do aluguel', max_digits=8, decimal_places=2, default=0)
    cor_toalha = models.CharField('Cor da Toalha', max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'


class ItemTema(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Item do Tema'
        verbose_name_plural = 'Itens do Tema'


class Aluguel(models.Model):
    data_festa = models.DateField('Data da Festa')
    hora_inicio = models.TimeField('Horario de Inicio')
    hora_termino = models.TimeField('Horario de Termino')
    valor_cobrado = models.DecimalField('Valor cobrado', max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Alugueis'

    def __str__(self):
        return '{} - {} - {}'.format(
            self.dataFesta
        )


class Endereco(models.Model):
    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.CharField('Numero', max_length=10)
    complemento = models.CharField('Complemento', max_length=100)
    bairro = models.CharField('Bairro', max_length=20)
    cidade = models.CharField('Cidade', max_length=20)
    uf = models.CharField('UF', max_length=3)
    cep = models.CharField('CEP', max_length=10)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class Cliente(models.Model):
    nome = models.DateField()
    telefone = models.TimeField()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
