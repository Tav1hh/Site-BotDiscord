def servers():
    import discord
    from discord import app_commands
    from discord.ext import commands
    import requests

    #Fala se o Bot foi ligado com sucesso
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='*', intents= discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'Conectado como {client.user}')

        def acessivel(url):
            response = requests.get(url)
            # Verifica se a resposta foi bem sucedida (código 2xx)
            # Verifica se a resposta foi bem sucedida (código 2xx)
            # if response.status_code == 200 and 'gif' not in url:
            if response.status_code == 200:
                return True
            else:
                return False

        # Abre o arquivo para escrever as informações com codificação UTF-8
        with open('imagens_servidores.txt', 'w', encoding='utf-8') as file:
            for guild in client.guilds:
                try:
                    invites = await guild.invites()
                    file.write(f'Nome do Servidor: {guild.name}\n')
                    file.write(f'Link da Imagem: {guild.icon.url if guild.icon and acessivel(guild.icon.url) else "https://wallpapercave.com/wp/wp8761712.jpg"}\n')
                    if invites:
                        # Se houver convites existentes, pega o primeiro
                        invite = invites[0]
                        file.write(f'Link de Convite: {invite.url}\n\n')
                    else:
                        # Se não houver convites existentes, cria um novo convite
                        file.write(f'Link de Convite: {await guild.text_channels[0].create_invite()}\n\n') # Obtém o link de convite do primeiro canal de texto
                except Exception as e:
                    print(f'Erro ao escrever servidor {guild.name}: {e}')

        print('Informações salvas em imagens_servidores.txt')
        await client.close()

    # Executa o bot com o token fornecido
    client.run("Token")

servers()