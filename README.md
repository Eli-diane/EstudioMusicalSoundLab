# 🎸 Studio Sound Lab - AI Audio Splitter

> Uma estação de trabalho para músicos baseada em Inteligência Artificial, capaz de separar faixas de áudio (stems), controlar velocidade e criar loops para ensaio.

![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)
![Badge Python](http://img.shields.io/static/v1?label=PYTHON&message=3.10%2B&color=blue&style=for-the-badge)
![Badge Django](http://img.shields.io/static/v1?label=DJANGO&message=FRAMEWORK&color=green&style=for-the-badge)


## 🧠 Sobre o Projeto

O **Studio Sound Lab** é uma aplicação web Fullstack desenvolvida para auxiliar músicos no processo de tirar músicas e ensaiar. O sistema utiliza modelos de **Deep Learning (Demucs)** para desconstruir arquivos MP3 brutos em 4 faixas isoladas: Bateria, Baixo, Voz e Outros (Teclado/Guitarra).

Além da separação, o projeto oferece um **Player/Mixer interativo** no navegador, permitindo controle total sobre o playback para fins de estudo.

## ✨ Funcionalidades

- **Separador de Áudio com IA:** Integração com a biblioteca `Demucs` (Meta/Facebook Research) para separação de fontes sonoras.
- **Mixer Multi-track:** Controle de volume independente para cada instrumento.
- **Controle de Velocidade (Time Stretch):** Acelere ou desacelere a música (0.5x a 1.5x) sem alterar a afinação (Pitch), ideal para aprender solos rápidos.
- **Sistema de Loop A-B:** Marque pontos de início e fim para repetir trechos específicos automaticamente.
- **Atalhos de Teclado:** Controle de Play/Pause e navegação temporal sem usar o mouse (mãos livres para o instrumento).
- **Download de Stems:** Exportação das faixas separadas para uso em DAWs.
- **Interface Dark Mode:** UI moderna e responsiva focada na usabilidade noturna.

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3:** Linguagem base.
- **Django:** Framework web robusto para gerenciamento de rotas, views e banco de dados.
- **Demucs:** Modelo de Redes Neurais para separação de fontes musicais.
- **Subprocess & OS:** Gerenciamento de processos do sistema operacional para execução da IA e manipulação de arquivos.

### Frontend
- **HTML5 & CSS3:** Estrutura semântica e estilização responsiva (Dark Theme).
- **JavaScript (Vanilla):** Lógica do Player, sincronização de áudios, controle de loop e manipulação do DOM.

### Ferramentas Externas
- **FFmpeg:** Framework multimídia para decodificação e processamento de áudio.

## 🚀 Como rodar o projeto localmente

### Pré-requisitos
* Python 3 instalado.
* FFmpeg instalado e configurado nas variáveis de ambiente do sistema.

### Passo a passo

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/SEU-USUARIO/studio-sound-lab.git](https://github.com/SEU-USUARIO/studio-sound-lab.git)
   cd studio-sound-lab
   ´´´

2. **Crie e ative um ambiente virtual**

bash
# No Windows
python -m venv venv
.\venv\Scripts\activate


# No Linux/Mac
python3 -m venv venv
source venv/bin/activate
´´´
# INSTALAÇÕES

3. **Instale as dependências**

Bash
pip install django demucs

4. **Realize as migrações do banco de dados**

Bash
python manage.py migrate

5. **Inicie o servidor**

Bash
python manage.py runserver

6. **Acesse no navegador Vá para http://127.0.0.1:8000/**

# ⌨️ **Atalhos de Teclado**
Uma vez selecionada uma música no mixer:

**Espaço**: Play / Pause (Toda a banda sincronizada)

**Seta Esquerda**: Voltar 5 segundos

**Seta Direita**: Avançar 5 segundos

#📝 Licença
Este projeto foi desenvolvido para fins de estudo e portfólio. Sinta-se à vontade para contribuir!

Feito com ❤️ por Eli Santos
