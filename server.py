from __future__ import unicode_literals
from ably import AblyRest
import web

apiKey = '6WX-UA.hB1OXA:n1sFldnLsS31H6od'

client = AblyRest(apiKey)

render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index()

class publish:
    def GET(self):
        return render.publish()

    def POST(self):
        message = web.input().get('message')
        if message is not None:
            channel = client.channels.get('sport')
            channel.publish('update', message)
        raise web.seeother('/publish')

urls = (
    '/', index,
    '/publish', publish
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()