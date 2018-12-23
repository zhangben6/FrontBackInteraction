class UrlManager(object):
    @staticmethod
    def buildUrl(path):
        return path
    
    @staticmethod
    def buildStaticUrl(path):
        path = path + '?ver=' + '20181220'
        return UrlManager.buildUrl(path)
    