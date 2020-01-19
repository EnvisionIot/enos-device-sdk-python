class StringUtil:

    @staticmethod
    def is_empty(string):
        if string is None or string.strip() == "":
            return True
        else:
            return False

    @staticmethod
    def is_not_empty(string):
        return not StringUtil.is_empty(string)
