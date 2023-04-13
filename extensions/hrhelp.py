import lightbulb
import hikari
import miru


plugin = lightbulb.Plugin('hrhelp', 'HRhelp')




rest = hikari.RESTApp()
@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass






@plugin.command
@lightbulb.command('hrhelp', 'HRhelp')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ban(ctx):
  embed = hikari.Embed(
    title="HRHELP",
    description="Use the below buttons to access the links.\n1️⃣ - Onboard a new candidate\n2️⃣ - Offboard an Employee \n3️⃣ - Give Raise\n4️⃣ - Change Employment Type\n5️⃣ - Issue Equity to an Employee\n6️⃣ - Run Manual Payroll"
  )
  view = miru.View()
  view.add_item(miru.Button(label="1️⃣", url="https://app.process.st", row=1))
  view.add_item(miru.Button(label="2️⃣", url="https://app.process.st", row=1))
  view.add_item(miru.Button(label="3️⃣", url="https://app.process.st", row=1))
  view.add_item(miru.Button(label="4️⃣", url="https://app.process.st", row=2))
  view.add_item(miru.Button(label="5️⃣", url="https://app.process.st", row=2))
  view.add_item(miru.Button(label="6️⃣", url="https://app.process.st", row=2))

  await ctx.respond(embed=embed, components=view)








def load(bot):
    bot.add_plugin(plugin)
