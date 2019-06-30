# VoiceChat

Chat de voz criado através do exemplo prático da biblioteca PyAudio.
   - http://sharewebegin.blogspot.com/2013/06/real-time-voice-chat-example-in-python.html

Documentação PyAudio:
   - https://people.csail.mit.edu/hubert/pyaudio/docs/
   

### Requisitos
  
  - Python 2.7+
  - PyAudio 0.2.11.1build2+

### Configurando ambiente para o trabalho (LabRedes)

#### Criando ambiente no conda

   - conda create -n [nome_do_ambiente] (criar)
   - source activate [nome_do_ambiente] (ativar)
   - source deactivate [nome_do_ambiente] (desativar)

#### Instalando pacotes com o conda
   
   - conda install [nome_do_pacote]
      - conda install python3.6
      - conda install pyaudio

#### Resolvendo conflito PyAudio no Conda
   
   - conda install nwani::portaudio nwani::pyaudio
