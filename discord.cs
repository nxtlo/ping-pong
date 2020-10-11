using System;
using System.Threading;
using System.Threading.Tasks;
using Discord;
using Discord.WebSocket;

public class ping : BaseCommandModule
{
    [command("ping")]
    public async Task ping(CommandContext ctx)
    {
        await ctx.Channel.SendMessageAsync("pong!").ConfigureAwait(false);
    }

}