import web

urls = (
  '/', 'Index'
)

app = web.application (urls, globals())

render = web.template.render ('templates/')

class Index(object):
  def GET (self):
<<<<<<< HEAD
    greeting = "Hello People"
=======
    greeting = "Hello People of the World"
>>>>>>> newer
    return render.index (greeting = greeting)

if __name__ == "__main__":
  app.run()
