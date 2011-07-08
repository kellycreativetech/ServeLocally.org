from django.http import HttpResponseRedirect

class NoWWW:
    def process_request(self, request):
        if request.get_host() != "servelocally.org":
            return HttpResponseRedirect("http://servelocally.org%s" % request.get_full_path())