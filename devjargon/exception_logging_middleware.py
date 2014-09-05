import logging
import traceback

class ExceptionLoggingMiddleware(object):

    def process_exception(self, request, exception):
        traceback.print_exc()