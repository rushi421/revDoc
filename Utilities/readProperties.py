import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\rushe\\PycharmProjects\\revDoc\\Configurations\\config.ini")

class ReadCofig:

    @staticmethod
    def getApplicationURL():
        url = config.get('basic information', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('basic information', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('basic information', 'password')
        return password

    @staticmethod
    def getSupplyID():
        supplyID = config.get('basic information', 'supplyID')
        return supplyID

    @staticmethod
    def getLabName():
        labName = config.get('basic information', 'labName')
        return labName
