# === VARIÁVEIS PARA PERSONALIZAR ===
#
# Quando usamos chr() em Python, estamos convertendo um número em caractere.
# Os números de 0 a 31 são chamados de caracteres de controle ASCII — eles
# não são símbolos visuais, e sim comandos antigos de terminal (como "enter",
# "beep", etc.), criados nos anos 80 para o MS-DOS. Por isso, a maioria dos
# terminais modernos não os exibe.
#
# Para exibir símbolos de verdade, usei os códigos Unicode, que é o padrão
# atual. Por exemplo, chr(0x266A) exibe ♪ porque 0x266A é o endereço desse
# símbolo na tabela Unicode, que contém mais de 140 mil caracteres de todas as
# línguas e culturas do mundo.
#
# Use Unicode (ex.: chr(0x2665) para ♥) ou o próprio caractere literal e
# garanta que o terminal esteja em UTF-8 (no Windows: `chcp 65001`) e uma
# fonte compatível.


nome_perfil = "THIAGO"
localidade = "Brasil"
idade = 20
conteudo_post = "Hoje aprendi sobre variáveis em Python!\nÉ incrível como podemos guardar informações e usá-las no código."
curtidas = 42

# Símbolos ASCII com chr()
seta    = chr(0x25BA)   # ►
coracao = chr(0x2665)   # ♥
sol     = chr(0x263C)   # ☼
nota    = chr(0x266A)   # ♪
seta_cima = chr(0x2191) # ↑



# Arte do perfil (rosto e moldura usando chr() quando possível)
face = "(◕‿◕)"
box_tl = chr(0x256D)  # ╭
box_tr = chr(0x256E)  # ╮
box_bl = chr(0x2570)  # ╰
box_br = chr(0x256F)  # ╯
box_h = chr(0x2501)   # ━
box_v = chr(0x2503)   # ┃

# === MONTANDO O POST ===

print()
print(sol * 30)
print("  MEU PERFIL")
print(sol * 30)

print()
print("  " + face)
print("  " + box_tl + box_h * 8 + box_tr)
print("  " + box_v + "  FOTO  " + box_v)
print("  " + box_bl + box_h * 8 + box_br)

print()
print("  👤 Nome: " + nome_perfil)
print("  📍 Local: " + localidade)
print("  🎂 Idade: " + str(idade) + " anos")

print()
print("━" * 30)
print("  📝 POST")
print()
print("  " + conteudo_post)
print()
print("━" * 30)

print()
print("  " + coracao + " " + str(curtidas) + " curtidas")

print()
print("  💬 COMENTÁRIOS:")
print("  " + seta + " Maria: Que incrível! " + coracao)
print("  " + seta + " Lucas: Python é demais! " + nota)
print("  " + seta + " Ana: Continue estudando! " + seta_cima)

print()
print("━" * 30)