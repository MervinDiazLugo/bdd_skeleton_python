import os

class Config():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"

    Environment = 'Test'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/DataTest.xlsx'

    if Environment == 'Dev':
        URL = 'https://dev.spotify.com/py/signup/'

    if Environment == 'Test':
        URL = 'https://test.spotify.com/py/signup/'








