#
# autores:
# michel

# data: 25/01/2023

# instalar o módulo youtube_dl
# https://github.com/ytdl-org/youtube-dl
# pip install youtube_dl


# Importa o módulo tkinter

import tkinter as tk # Importa o módulo tkinter
from tkinter import ttk # Importa o módulo ttk do tkinter para usar widgets modernos do Tkinter
import youtube_dl # Importa o módulo youtube_dl para fazer o download de vídeos do 
#                  # YouTube e outros sites

# Cria a classe DownloadWindow que herda de tk.Frame
class Janela02(tk.Frame):
    def __init__(self, principal): # Método construtor da classe Janela que recebe como parâmetro a janela principal (master)
        self.principal = principal # Atribui a janela principal à variável self.master
        self.principal.title("YouTube download") # Define o título da janela principal

        self.label = ttk.Label(self.principal, text="YouTube URL:")
        self.label.grid(row=0, column=0, padx=5, pady=5) # Exibe o Label na janela principal (master)

        self.url_entry = ttk.Entry(self.principal)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5) # Exibe o Entry na janela principal (master) 

        self.download_button = ttk.Button(self.principal, text="Download", command=self.download) # Cria o botão de download  
        # e define a função que será executada quando o botão for clicado
        self.download_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, ipadx=100) # Exibe o botão na janela principal (master)

    def download(self):
        url = self.url_entry.get() # Obtém a URL do vídeo do YouTube que o usuário digitou no Entry
        
        # baixar video
        opcoes = { # Define as opções de download do vídeo do YouTube que serão passadas para o youtube_dl
            'format': 'bestvideo+bestaudio/best', # Define o formato do vídeo que será baixado (melhor vídeo + melhor áudio ou melhor vídeo)
            'outtmpl': '%(title)s.%(ext)s', # Define o nome do arquivo de saída
        }
        
        
        # extrair o audio do video
        """
        ydl_opts = { # Define as opções de download do vídeo do YouTube que serão passadas para o youtube_dl
            'format': 'bestaudio/best', # Define o formato do vídeo que será baixado (melhor áudio ou melhor vídeo) 
            'outtmpl': '%(title)s.%(ext)s', # Define o nome do arquivo de saída
            'postprocessors': [{  # Define o postprocessador que será usado para extrair o áudio do vídeo
                'key': 'FFmpegExtractAudio',  # Define o postprocessador como o FFmpegExtractAudio
                'preferredcodec': 'mp3', # Define o codec de áudio que será extraído do vídeo
                'preferredquality': '192',  # Define a qualidade do áudio que será extraído do vídeo
            }],
        }
        """
        
        with youtube_dl.YoutubeDL(opcoes) as ydl: # Cria um objeto do youtube_dl com as opções de download definidas acima 
            ydl.download([url]) # Faz o download do vídeo do YouTube com as opções definidas acima e a URL do vídeo do YouTube




######### só para testar a classe #########
if __name__ == "__main__": # Verifica se o arquivo está sendo executado diretamente e não importado por outro arquivo Python
    root = tk.Tk() # Cria a janela principal (master)
    app = Janela02(root) # Cria um objeto da classe Janela passando a janela principal como parâmetro para o construtor
    root.mainloop() # Inicia o loop principal da janela principal (master)
