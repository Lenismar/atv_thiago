# Historia 3: Missão Espacial

print("Você é um astronauta em missão para Marte!")
print("ALERTA: Falha no sistema de oxigênio!")

# Cena 1: O Alerta
print("\n--- CENA 1: Emergência a bordo ---")
print("A) Tentar consertar manualmente")
print("B) Usar o sistema reserva")
escolha1 = input("Sua escolha (A ou B): ").upper()

# Cena 2: depende da escolha 1
if escolha1 == "A":
    print("\n--- CENA 2: Compartimento externo ---")
    print("Você precisa sair da nave para consertar.")
    print("A) Sair sem cabo de segurança")
    print("B) Usar o cabo de segurança")
    escolha2 = input("Sua escolha (A ou B): ").upper()

    if escolha2 == "A":
        print("\nVocê se desprendeu da nave e não conseguiu voltar...")
        print("FICOU À DERIVA NO ESPAÇO. ☠")
    else:
        if escolha2 == "B":
            print("\nCom segurança você consertou tudo e continuou a viagem!")
            print("MISSÃO CUMPRIDA, CHEGOU EM MARTE! 🚀")
        else:
            print("\nOpção inválida! Digite apenas A ou B.")

elif escolha1 == "B":
    print("\n--- CENA 2: Sistema reserva também falhou! ---")
    print("A situação piorou. O que fazer agora?")
    print("A) Entrar em contato com a base na Terra")
    print("B) Usar os tanques de emergência")
    escolha2 = input("Sua escolha (A ou B): ").upper()

    if escolha2 == "A":
        print("\nA Terra enviou uma nave de resgate que chegou a tempo!")
        print("RESGATADO POR OUTRA NAVE! 🛸")
    else:
        if escolha2 == "B":
            print("\nOs tanques deram oxigênio suficiente para voltar!")
            print("VOLTA PARA A TERRA EM SEGURANÇA! 🌍")
        else:
            print("\nOpção inválida! Digite apenas A ou B.")

else:
    print("\nOpção inválida! Digite apenas A ou B.")