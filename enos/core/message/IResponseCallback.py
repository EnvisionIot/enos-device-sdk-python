class IResponseCallback:

    def on_response(self, response):
        """handle the async response of the mqtt request
        :param response:
        :return:
        """
        print('[async] receive {} successfully, code: {}'.format(response.get_class(), str(response.get_code())))

    def on_failure(self, exception):
        """ Handle exception we hit while waiting for the response
        :param exception:
        :return:
        """
        print('[async] publish failed, exception: {}'.format(exception))

