from django.db import models

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100, blank=True)
    arquivo_original = models.FileField(upload_to='musicas/')
    data_envio = models.DateTimeField(auto_now_add=True)

    # --- Novos Campos para as Faixas Separadas ---
    # blank=True e null=True significam que eles podem ficar vazios 
    # (porque quando a gente sobe a música, eles ainda não existem)
    faixa_voz = models.FileField(upload_to='processados/', blank=True, null=True)
    faixa_bateria = models.FileField(upload_to='processados/', blank=True, null=True)
    faixa_baixo = models.FileField(upload_to='processados/', blank=True, null=True) # Especial pro namorado!
    faixa_outros = models.FileField(upload_to='processados/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
