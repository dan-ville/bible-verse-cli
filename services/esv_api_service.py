import requests
from services.base_service import BaseService

class ESVService(BaseService):
    def __init__(self):
        super().__init__('bible_cli_config')
        self.api_key = self.get_config('ESV', 'ApiKey')
        self.base_url = 'https://api.esv.org/v3/passage'

    def get_bible_verse(self, reference):
        params = {'q': reference}
        params['include-footnotes'] = 'false'

        headers = {'Authorization': f'Token {self.api_key}'}
        response = requests.get(f'{self.base_url}/text', headers=headers, params=params)

        if not response.status_code == 200:
            return "Error: Unable to retrieve the verse."
        
        data = response.json()
        passages = data.get('passages', [])

        if len(passages) == 0:
            return "Passage not found"
        else:
            return passages[0]
