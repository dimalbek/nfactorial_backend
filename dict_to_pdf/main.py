from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def create_pdf(data):
    pdfmetrics.registerFont(TTFont('ArialUnicode', 'Arial Unicode.TTF'))

    c = canvas.Canvas("simple_pdf.pdf")
    c.setFont('ArialUnicode', 12)
    counter = 0
    for k, v in data.items():
        c.drawString(100, 750 - 20 * counter, f'{k} : {v}')
        counter += 1
    c.save()


if __name__ == "__main__":
    data = {
          'bin': '21B030999',
          'fio': 'TIMA TIMA TIMA TIMA',
          'id': 0,
          'ip': False,
          'katoAddress': 'АСТАНА Қ., ЕСІЛ АУДАНЫ, Мәңгілік Ел Даңғылы, '
                         '8-ғимарат',
          'katoCode': '711210000',
          'katoId': 268017,
          'kfsCode': '12',
          'kfsName': 'Республикалық  меншік',
          'krpBfCode': '305',
          'krpBfName': None,
          'krpCode': '305',
          'krpName': None,
          'kseCode': '1311',
          'kseName': 'Орталық басқару органдары, әлеуметтік қамтамасыз ету '
                     'қорларынан басқа ',
          'name': None,
          'okedCode': '84111',
          'okedName': None,
          'registerDate': '1997-01-05T00:00:00.000+0000',
          'secondOkeds': None
        }
    create_pdf(data)
