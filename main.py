import hikari
import lightbulb

token = os.environ['token']
import miru







bot = lightbulb.BotApp(
  token=token,
  help_slash_command=True
)


@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.")
        raise event.exception

    # Unwrap the exception to get the original cause
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("You are not the owner of this bot.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        time = exception.retry_after /3600
        import time
        
        timestamp = round(time.time()) + exception.retry_after
        await event.context.respond(f"This command is on cooldown. Retry at <t:{round(time.time() + exception.retry_after)}> ")
    elif ...:
        ...
    else:
        raise exception



@bot.listen(hikari.StartedEvent)
async def bot_started(event):
  
    print('Bot has started.')










bot.load_extensions_from('./extensions')
miru.install(bot)
print("Miru initialized")

bot.run()


