from BrainBucket.utils.json_file_reader import JsonFileReader
from BrainBucket.utils.ini_file_reader import IniFileReader


class ConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        elif filename.endswith(".ini"):
            self.reader = IniFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self):
        return self.reader.get_browser()

    def get_wait_time(self):
        return self.reader.get_wait_time()

    # AN my code starts
    def get_email(self, section_name):
        return self.reader.get_email(section_name)

    def get_password(self, section_name):
        return self.reader.get_password(section_name)

    def get_width_viewport(self, section_name):
        return self.reader.get_width_viewport(section_name)

    def get_height_viewport(self, section_name):
        return self.reader.get_height_viewport(section_name)

    def get_browserstack_url(self, section_name):
        user_name = self.reader.get_user_name(section_name)
        access_key = self.reader.get_access_key(section_name)
        browserstack_url = f'http://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub'

        return browserstack_url

    def get_desired_cap(self, section_name):
        return self.reader.get_desired_cap(section_name)


    # AN my code ends