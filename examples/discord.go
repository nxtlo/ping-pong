package main

import (
	"fmt"
	"github.com/andersfylling/disgord"

)

client.On(disgord.EvtMessageCreate, func(s disgord.Session, evt *disgord.MessageCreate) {
	msg := evt.Message
	if msg.Content == "ping" {
		_, _ = msg.Reply(context.Background(), s, "pong")
	}
})
}
