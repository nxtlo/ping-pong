require 'discordrb'

bot = Discordrb::Bot.new token: '123456789'

bot.message(content: 'ping' do |event|)
    event.respond 'Pong!'
end

bot.run