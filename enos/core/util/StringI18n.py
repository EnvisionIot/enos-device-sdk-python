
class StringI18n(object):
    """tsl string internationalization"""

    def __init__(self, default_value=None):
        self.__default_value = default_value
        self.__i18n_value = dict()

    def get_default_value(self):
        return self.__default_value

    def set_default_value(self, default_value):
        self.__default_value = default_value

    def get_localized_value(self, locale):
        return self.__i18n_value.get(locale)

    def set_localized_value(self, locale, localized_value):
        self.__i18n_value[locale] = localized_value

    def encode(self):
        payload = dict()
        if self.get_default_value() is not None:
            payload['defaultValue'] = self.get_default_value()
        if self.get_i18n_value() is not None:
            payload['i18nValue'] = self.get_i18n_value()
        return payload

    def get_i18n_value(self):
        return self.__i18n_value

    def set_i18n_value(self, i18n_value):
        self.__i18n_value = i18n_value

    def __str__(self):
        return "StringI18n [defaultValue=" + self.__default_value + "]"

    def __hash__(self):
        prime = 31
        result = 1
        if not self.__default_value:
            result = prime * result
        else:
            result = prime * result + hash(self.__default_value)
        if not self.__i18n_value:
            result = prime * result
        else:
            result = prime * result + hash(self.__i18n_value)
        return result
