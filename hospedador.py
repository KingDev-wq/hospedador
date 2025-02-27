import os
import time
from colorama import init, Fore

# Inicializa o Colorama
init(autoreset=True)

bots_dir = "bots"
logs_dir = "logs"

if not os.path.exists(bots_dir):
    os.makedirs(bots_dir)

if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Créditos
def mostrar_creditos():
    os.system("clear")
    print(Fore.RED + """
    ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗ 
    ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔═══██╗
    ██████╔╝█████╗  ██████╔╝███████╗█████╗  ██║   ██║
    ██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██╔══╝  ██║   ██║
    ██║     ███████╗██║  ██║███████║███████╗╚██████╔╝
    ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ 
    """)

    print(Fore.CYAN + "📌 Hospedador de Bots Discord")
    print(Fore.YELLOW + "🔹 Desenvolvido por: King")
    print(Fore.YELLOW + "🔹 Equipe: DedSec.py")
    print(Fore.RED + "\n⚠️ PROIBIDO ROUBAR OU ALTERAR O CÓDIGO ⚠️")
    print(Fore.RED + "🚀 Se encontrar bugs, entre em contato com a DedSec.py\n")
    time.sleep(3)

mostrar_creditos()

def menu():
    os.system("clear")
    print(Fore.CYAN + "1. Adicionar Bot")
    print("2. Ver Meus Bots")
    print("3. Ligar Bot")
    print("4. Excluir Bot")
    print("5. Ver Logs")
    print(Fore.RED + "00. Sair")
    
    escolha = input(Fore.YELLOW + "\nEscolha uma opção: ")
    
    if escolha == "1":
        adicionar_bot()
    elif escolha == "2":
        ver_bots()
    elif escolha == "3":
        ligar_bot()
    elif escolha == "4":
        excluir_bot()
    elif escolha == "5":
        ver_logs()
    elif escolha == "00":
        print(Fore.RED + "Saindo...")
        exit()
    else:
        print(Fore.RED + "Opção inválida!")
        time.sleep(2)
        menu()

def adicionar_bot():
    os.system("clear")
    print(Fore.GREEN + "📥 Adicionar Bot")
    nome = input(Fore.YELLOW + "Nome do bot: ")
    link = input(Fore.YELLOW + "Link do Google Drive: ")

    bot_pasta = f"{bots_dir}/{nome}"
    if os.path.exists(bot_pasta):
        print(Fore.RED + "⚠️ Esse bot já existe!")
        time.sleep(2)
        menu()
    
    os.makedirs(bot_pasta)
    
    print(Fore.CYAN + "Baixando arquivos do bot...")
    os.system(f"wget '{link}' -O {bot_pasta}/bot.zip")
    os.system(f"unzip {bot_pasta}/bot.zip -d {bot_pasta}")
    
    if not os.path.exists(f"{bot_pasta}/Dedsec.config"):
        print(Fore.RED + "❌ O arquivo 'Dedsec.config' não foi encontrado. Removendo bot...")
        os.system(f"rm -rf {bot_pasta}")
        time.sleep(2)
        menu()
    
    print(Fore.GREEN + "✅ Bot adicionado com sucesso!")
    time.sleep(2)
    menu()

def ver_bots():
    os.system("clear")
    print(Fore.CYAN + "🤖 Meus Bots")
    
    bots = os.listdir(bots_dir)
    if not bots:
        print(Fore.RED + "⚠️ Nenhum bot encontrado!")
    else:
        for bot in bots:
            print(Fore.YELLOW + f"📌 {bot}")
    
    input("\nPressione Enter para voltar...")
    menu()

def ligar_bot():
    os.system("clear")
    print(Fore.GREEN + "🚀 Ligar Bot")
    nome = input(Fore.YELLOW + "Nome do bot: ")
    bot_pasta = f"{bots_dir}/{nome}"
    log_file = f"{logs_dir}/{nome}.log"
    
    if not os.path.exists(bot_pasta):
        print(Fore.RED + "⚠️ Bot não encontrado!")
        time.sleep(2)
        menu()
    
    print(Fore.CYAN + "Instalando dependências...")
    os.system(f"cd {bot_pasta} && pip install -r requirements.txt")
    
    print(Fore.GREEN + "Iniciando bot...")
    os.system(f"cd {bot_pasta} && nohup python bot.py > {log_file} 2>&1 &")
    
    print(Fore.GREEN + f"✅ Bot iniciado! Logs salvos em {log_file}")
    time.sleep(2)
    menu()

def excluir_bot():
    os.system("clear")
    print(Fore.RED + "🗑️ Excluir Bot")
    nome = input(Fore.YELLOW + "Nome do bot: ")
    bot_pasta = f"{bots_dir}/{nome}"
    log_file = f"{logs_dir}/{nome}.log"
    
    if not os.path.exists(bot_pasta):
        print(Fore.RED + "⚠️ Bot não encontrado!")
        time.sleep(2)
        menu()
    
    os.system(f"rm -rf {bot_pasta}")
    os.system(f"rm -f {log_file}")
    print(Fore.GREEN + "✅ Bot excluído com sucesso!")
    time.sleep(2)
    menu()

def ver_logs():
    os.system("clear")
    print(Fore.BLUE + "📜 Ver Logs")
    
    logs = os.listdir(logs_dir)
    if not logs:
        print(Fore.RED + "⚠️ Nenhum log encontrado!")
        time.sleep(2)
        menu()

    print(Fore.YELLOW + "Logs disponíveis:")
    for log in logs:
        print(Fore.CYAN + f"📂 {log}")

    nome = input(Fore.YELLOW + "\nDigite o nome do bot para ver os logs: ")
    log_file = f"{logs_dir}/{nome}.log"

    if not os.path.exists(log_file):
        print(Fore.RED + "⚠️ Nenhum log encontrado para esse bot!")
        time.sleep(2)
        menu()

    print(Fore.GREEN + f"📜 Logs do bot {nome}:\n")
    os.system(f"cat {log_file}")

    input("\nPressione Enter para voltar...")
    menu()

menu()
