from configparser import ConfigParser


class IniFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = ConfigParser()
            self.data.read_file(config_file)

    def get_browser(self):
        value = self.data.get('environment', 'browser', fallback=None)
        if value is None:
            raise Exception("Browser option is not present in the config file")
        return value

    def get_wait_time(self):
        value = self.data.get('environment', 'wait', fallback=None)
        if value is None:
            raise Exception("Wait_time option is not present in the config file")
        return int(value)

    # AN my code starts
    def get_email(self, section_name):
        value = self.data.get(section_name, 'email', fallback=None)
        if value is None:
            raise Exception("email option is not present in the config file")
        return value

    def get_password(self, section_name):
        value = self.data.get(section_name, 'password', fallback=None)
        if value is None:
            raise Exception("password option is not present in the config file")
        return value

    def get_width_viewport(self, section_name):
        value = self.data.get(section_name, 'width', fallback=None)
        if value is None:
            raise Exception("width option is not present in the config file")
        return value

    def get_height_viewport(self, section_name):
        value = self.data.get(section_name, 'height', fallback=None)
        if value is None:
            raise Exception("height option is not present in the config file")
        return value

    def get_user_name(self, section_name):
        value = self.data.get(section_name, 'user_name', fallback=None)
        return value

    def get_access_key(self, section_name):
        value = self.data.get(section_name, 'access_key', fallback=None)
        return value

    def get_desired_cap(self, section_name):
        value = self.data.get(section_name, 'desired_cap', fallback=None)
        return value
    # AN code ends
