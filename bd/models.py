from django.db import models

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=120)
    senha = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return self.nome


class Vacas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = (
        ('parida', 'Parida'),
        ('solteira', 'Solteira'),
        ('no_cio', 'No cio'),
        ('inseminada', 'Inseminada'),
        ('prenha', 'Prenha')
    )
    nome_vaca = models.CharField('NOME:', max_length=30)
    raca = models.CharField(max_length=100)
    lote = models.CharField(max_length=22)
    numero_v = models.CharField(max_length=52,unique=True)
    origem = models.CharField(max_length=200, null=True)
    data_nascimento = models.DateField()
    statu = models.CharField(max_length=14, choices=status, blank=False, null=False)

    def __str__(self):
        return self.nome_vaca


class Bezerro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
    nome_bezerro = models.CharField(max_length=120, null=True)
    numero_b = models.CharField(max_length=22, unique=True)
    raca = models.CharField(max_length=100)
    lote = models.CharField(max_length=150)
    origem = models.CharField(max_length=200, null=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome_bezerro


class Reprodutor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)
    nome_reprodutor = models.CharField(max_length=100, null=True)
    numero_r = models.CharField(max_length=22, unique=True)
    raca = models.CharField(max_length=100)
    lote = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    origem = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.nome_reprodutor
    



class Prenha(models.Model):
    vaca_id = models.IntegerField()
    data_nascimento_B = models.DateField()

    def __str__(self):
        return str(self.data_nascimento_B)


