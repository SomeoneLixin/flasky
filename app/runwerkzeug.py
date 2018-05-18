from hellowerkzeug import WebApp, View
class Index(View):
    def GET(self, request):
        return "hello world"

class Test(View):
    def GET(self, request):
        return "test"

urls = [
{
    'url': '/',
    'view': Index
},
{
   'url': '/test',
   'view': Test
}
]


app = WebApp()

app.add_url_rule(urls)

app.run()