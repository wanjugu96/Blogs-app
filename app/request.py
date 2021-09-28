import urllib.request,json
from app.models import Quote


base_url='http://quotes.stormconsultancy.co.uk/random.json'

def get_quote():
    with urllib.request.urlopen(base_url) as url:
        get_quote_data=url.read()
        get_quote_repsonse=json.loads(get_quote_data)

        quote_result=get_quote_repsonse

        id =quote_result.get('id')
        quote=quote_result.get('quote')
        author=quote_result.get('author')

        quote_object=Quote(author,id,quote)

        return quote_object