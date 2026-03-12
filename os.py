import subprocess
import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar comando:",e)

def mostrar_ip():
    executar_comando("ipconfig")

def renovar_ip():
    executar_comando("ipconfig /renew")

def mostrar_ip_completo():
    executar_comando("ipconfig /all")

def ping_host():
    host = input("Digite o IP ou HOSTNAME: ")
    executar_comando (f"ping {host}")

def menu():
    while True:
        print("\n==Ferramenta de rede")
        print("1 - Mostar IP")
        print("2 - Renovar IP")
        print("3 - Mostrar configurações de rede completa")
        print("4 - PING")
        print("5 - SAIR")
        print("Criado por Douglas --------------")
        opcao = str(input("Escolha: "))
        match opcao:
            case "1":
                mostrar_ip()
            case "2":
                renovar_ip()
            case "3":
                mostrar_ip_completo()
            case "4":
                ping_host()
            case "5":
                print("Saindo...")
                break
            case _:
                print("Eita caba sabido!!!")

if __name__ == "__main__":
    menu()