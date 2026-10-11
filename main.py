
import os

import discord
from discord.ext import commands
from discord import app_commands

# =========================
# CONFIGURAÇÃO DO BOT 
# =========================

intents = discord.Intents.default()


class MeuBot(commands.Bot):
    async def setup_hook(self):
        comandos = await self.tree.sync()
        print(f"{len(comandos)} comando(s) slash sincronizado(s).")


bot = MeuBot(
    command_prefix="!",
    intents=intents
)


# =========================
# JOGADORES DO GER TIME PES 2013 V2 E DATA DE ATUALIZAÇÃO
# =========================

att = "10/10/2026"

jogadores = {
    "Jubileu": 88,
    "Michael Jackson": 86,
    "Carlos Ycáro": 84,
    "Necus": 84,
    "Dudu": 83,
    "Gin Gagamaru": 84,
    "Gutte": 83,
    "Taddei": 83,
    "Bitata Teco": 82,
    "Jonas Valim": 82,
    "Képler Lima": 82,
    "Macols Tulyio": 82,
    "Shanks": 82,
    "Cadiony": 81,
    "Garrincha": 81,
    "Ardolf Hiitos": 80,
    "Kadielvis Jota": 80,
    "Tizil": 80,
    "Pazhuerto": 74
}


# =========================
# EVENTO DE INICIALIZAÇÃO
# =========================

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


# =========================
# COMANDO /timegerv2
# MOSTRA TODOS OS JOGADORES
# =========================

@bot.tree.command(
    name="timegerv2",
    description="Mostra todos os jogadores e seus GERs"
)
async def timegerv2(interaction: discord.Interaction):
    descricao = "\n".join(
        f"**{nome}** — {ger} GER"
        for nome, ger in jogadores.items()
    )

    embed = discord.Embed(
        title="GER TIME PES 2013 V2",
        description=descricao,
        color=discord.Color.blue()
    )

    embed.set_footer(
        text=f"Última atualização: {att} • 19 jogadores"
    )

    await interaction.response.send_message(embed=embed)


# =========================
# COMANDO /gerjogador
# MOSTRA UM JOGADOR POR VEZ
# =========================

@bot.tree.command(
    name="gerjogador",
    description="Mostra o GER individual de um jogador"
)
@app_commands.describe(
    jogador="Escolha o jogador que deseja consultar"
)
@app_commands.choices(
    jogador=[
        app_commands.Choice(name=nome, value=nome)
        for nome in jogadores
    ]
)
async def gerjogador(
    interaction: discord.Interaction,
    jogador: app_commands.Choice[str]
):
    nome = jogador.value
    ger = jogadores[nome]

    embed = discord.Embed(
        title="GER TIME PES 2013 V2",
        description=(
            f"**Jogador:** {nome}\n"
            f"**GER:** {ger} GER"
        ),
        color=discord.Color.blue()
    )

    embed.set_footer(
        text=f"Última atualização: {att}"
    )

    await interaction.response.send_message(embed=embed)


# =========================
# INICIAR O BOT
# =========================

bot.run(os.environ.get("DISCORD_TOKEN", ""))