from django.db import models
from django.contrib.auth.models import User

# Aqui é criado o modelo do banco de dados 
# Django usa ORM, não precisa interagir com o BD diretamente. Cria o BD em formado de classes, abstrai em código, coda o banco. Camada models. Django converte em SQL.


# Tabela do Modelo de Clientes

class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,  # Irá proteger caso alguma tentativa de deletar o usuário que está ligado no cliente - consistência de dados
        blank=True,                # Coloca em campos que não são obrigatórios
        null=True,                 # Coloca em campos que não são obrigatórios
        related_name='Customers',  # Relação inversa da Query
        verbose_name='Usuário',    # Requisito que vai aparecer na tela do sistema "Usuário", motivo de estar em pt-br, usado como um label
    )

    name = models.CharField(
        max_length=100, 
        verbose_name='Nome',
    )

    cpf = models.CharField(        # CPF é do tipo charfield
        max_length=15,             # Tamanho
        blank=True, 
        null=True,
        verbose_name='CPF'
     )
    
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone',
    )

    # Create e Update são campos que 

    create_at = models.DateTimeField(
        auto_now_add=True,             # Vai setar data e hora atual
        verbose_name='Criado em ',
    )

    update_at = models.DateTimeField(
        auto_now=True,                 # Armazena todas vez que for feito uma atualização e pega a data e hora
        verbose_name='Atualizado em ', 
    )

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __str__(self):
        return self.name  # Representação em string dos registros
