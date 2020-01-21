from aiohttp import web, ClientSession

async def hello(request):
    return web.Response(text="Hello, world")

async def c10k(request):
    async with ClientSession() as session:
        async with session.get('https://en.wikipedia.org/wiki/C10k_problem', allow_redirects=True) as response:
            html = await response.text()
            return web.Response(text=html, headers={'Content-Type': 'text/html'})

handlers = [
    web.get('/', hello),
    web.get('/c10k', c10k),
]

app = web.Application()
app.add_routes(handlers)

web.run_app(app)
