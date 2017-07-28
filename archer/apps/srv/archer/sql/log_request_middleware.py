# -*- coding: UTF-8 -*- 
import re
from django.http import HttpResponseRedirect
import logging

log = logging.getLogger(__name__)
print(__name__)


class LogRequestMiddleware(object):
    def process_request(self, request):
        if request.path.startswith("/static"):
            pass
        if request.path.startswith("/favicon.ico"):
            pass
        params = {}
        if request.method == "GET":
            params = request.GET
        else:
            params = request.POST
        log.info("[Path:%s][Params:%s][Method:%s][Host:%s][ClientIp:%s][UserName:%s]" % (
            request.path, params, request.method, request.META['HTTP_HOST'],
            request.META['REMOTE_ADDR'],
            request.session.get('login_username', False)))
