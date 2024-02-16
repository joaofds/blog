from django.db import models

class PostModel(models.Model):
    titulo = models.CharField(
        max_length = 120,
        null = False,
        blank = False
    )

    descricao = models.CharField(
        max_length = 255,
        null = False,
        blank = False
    )

    created_at = models.DateTimeField(auto_now_add = True)
    objetos = models.Manager()