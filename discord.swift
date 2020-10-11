import 'Sword'

len bot = Sword(token: '123456789')

bot.on(.messageCreate) { data in
    let msg = data as! Message

    if msg.content == '!ping' {
        msg.reply(with: "Pong!")
    }
}
bot.connect()