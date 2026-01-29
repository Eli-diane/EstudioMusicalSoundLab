from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicaForm
from .models import Musica
import subprocess
import os
from django.conf import settings

def index(request):
    musicas = Musica.objects.all().order_by('-data_envio')

    if request.method == 'POST':
        form = MusicaForm(request.POST, request.FILES)
        if form.is_valid():
            musica = form.save()
            
            # --- CONFIGURAÇÕES ---
            caminho_ffmpeg = r"C:\ffmpeg\bin"
            os.environ["PATH"] += os.pathsep + caminho_ffmpeg
            
            caminho_arquivo = musica.arquivo_original.path
            
            # Definir que a saída será na pasta MEDIA, para o navegador conseguir ler
            # Cria a pasta media/separated se não existir
            pasta_media_absoluta = os.path.join(settings.MEDIA_ROOT, 'separated')
            if not os.path.exists(pasta_media_absoluta):
                os.makedirs(pasta_media_absoluta)

            # Comando com -o (output) apontando para a pasta certa
            comando = f'demucs --mp3 -n htdemucs -o "{pasta_media_absoluta}" "{caminho_arquivo}"'
            
            print("⏳ PROCESSANDO NA PASTA MEDIA...")
            subprocess.run(comando, shell=True, check=True)
            
            # --- DESCOBRINDO OS ARQUIVOS ---
            nome_arquivo_sem_extensao = os.path.splitext(os.path.basename(caminho_arquivo))[0]
            
            # Caminho onde os arquivos ficaram fisicamente
            pasta_final_musica = os.path.join(pasta_media_absoluta, 'htdemucs', nome_arquivo_sem_extensao)
            
            # Caminho RELATIVO para salvar no banco (para o Django montar a URL certa)
            # O replace resolve o problema das barras invertidas do Windows
            caminho_db_base = f"separated/htdemucs/{nome_arquivo_sem_extensao}"
            
            print(f"📂 Verificando arquivos em: {pasta_final_musica}")

            # Salvar no banco
            if os.path.exists(os.path.join(pasta_final_musica, 'bass.mp3')):
                musica.faixa_baixo = f"{caminho_db_base}/bass.mp3"
            
            if os.path.exists(os.path.join(pasta_final_musica, 'drums.mp3')):
                musica.faixa_bateria = f"{caminho_db_base}/drums.mp3"

            if os.path.exists(os.path.join(pasta_final_musica, 'vocals.mp3')):
                musica.faixa_voz = f"{caminho_db_base}/vocals.mp3"
                
            if os.path.exists(os.path.join(pasta_final_musica, 'other.mp3')):
                musica.faixa_outros = f"{caminho_db_base}/other.mp3"
            
            musica.save()
            return redirect('index')
    else:
        form = MusicaForm()

    return render(request, 'index.html', {'form': form, 'musicas': musicas})

def deletar_musica(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)
    musica.delete()
    return redirect('index')