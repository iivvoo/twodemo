from two.ol.base import RESTLikeHandler
from twodemo.demoapp.models import Demo
from twodemo.demoapp.views import DemoForm

class MainHandler(RESTLikeHandler):
    model = Demo
    formclass = DemoForm

    def list(self):
        return self.template("demoapp/index.html", demos=Demo.objects.all())

    def view(self):
        if self.user().is_anonymous():
            self.redirect("/")
        return self.template("demoapp/view.html")

    def update(self):
        if self.user().is_anonymous():
            self.redirect("/")
        if self.post and self.form.is_valid():
            self.form.save()
            self.redirect("/", success="Demo updated")
        return self.template("demoapp/edit.html")

    def create(self):
        if self.user().is_anonymous():
            self.redirect("/")
        if self.post and self.form.is_valid():
            self.form.save()
            ## XXX path/absolute_url magic
            self.redirect("/", success="Demo created")
        return self.template("demoapp/create.html")


