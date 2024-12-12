import time


def parabens():
    mensagem = """
    🎉🎂 Parabéns 🎂🎉

    Hoje é o seu dia! Vamos comemorar!
    Aqui vai uma função especial de aniversário criada especialmente para você:
    """

    print(mensagem)
    time.sleep(2)  # Pausa de 2 segundos para aumentar a expectativa


    def saudacao(nome):
        return f"Parabéns, {nome}! Você é incrível!"


    nome = "Katia"

    print(saudacao(nome))

    time.sleep(1)

    # contagem regressiva
    print("\nPreparando o presente...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    print("\n🚀 Seu presente chegou!")
    time.sleep(1)

    # Mensagem final
    print("\nQue seu código seja sempre limpo, seus bugs poucos e seus deploys suaves!")
    print("Você é uma pessoa espetacular, que sua vida esteja repleta de sucesso, conquistas e projetos incríveis!\n")
    print("🎉 Feliz Aniversário, minha amiga! 🎉")


if __name__ == "__main__":
    parabens()
