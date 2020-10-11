const Discord = require('discord.js');
const bot = new Discord.Client();

client.on('message', message => {
    if (message.content === '+ping') {  
      message.channel.send('Pong!');
    }
  });
