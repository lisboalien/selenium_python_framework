import configparser

from selenium import webdriver


def set_chrome_driver(path, binary):
    # Function that sets chromedriver
    # Please configure all the paths that are needed in the config.ini file
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.binary_location = binary

    return webdriver.Chrome(chrome_options=options, executable_path=path)


def set_firefox_driver(path, binary):
    # Function that sets firefoxdriver
    # Please configure all the paths that are needed in the config.ini file
    from selenium.webdriver.firefox.options import Options

    options = Options()
    options.binary_location = binary

    return webdriver.Firefox(firefox_options=options, executable_path=path)


def set_edge_browser(path):
    # Function that sets edgedriver
    # Please configure all the paths that are needed in the config.ini file

    return webdriver.Edge(executable_path=path)


class Driver:
    # Driver class that defines and returns which driver will be used for the automated tests
    # The default driver is Google Chrome
    browser = 'Chrome'

    @staticmethod
    def set_driver(browser):
        # Function that sets the driver that you choose
        # The possible values for browser are: Chrome, Firefox or Edge
        # Please configure all the paths that are needed in the config.ini file

        config = configparser.ConfigParser()
        config.read('config.ini')

        if browser == 'Chrome':
            path = config.get('DRIVER_PATHS', 'chromedriver')
            binary = config['DRIVER_BINARIES']['chromebinary']
            return set_chrome_driver(path, binary)
        elif browser == 'Firefox':
            path = config['DRIVER_PATHS']['firefoxdriver']
            binary = config['DRIVER_BINARIES']['firefoxbinary']
            return set_firefox_driver(path, binary)
        elif browser == 'Edge':
            path = config['DRIVER_PATHS']['edgedriver']
            return set_edge_browser(path)
