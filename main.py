from discord.ext import commands

bot commands.Bot(command_prefix='.')

bot.lavalink_nodes = [

{"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},

#Can have multiple nodes here

1

#If you want to use spotify search

bot.spotify_credentials = {

'client_id': 'fd08c3c7768746849a12743a66f8f97f',

'client_secret': 'CLIENT SECRET_HERE'

bot.load_extension('dismusic')

bot.run('')
