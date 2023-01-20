from typing import List
from bs4 import BeautifulSoup
import requests
import wikipedia


class WikiRacer:
    @staticmethod
    def find_path(start: str, finish: str) -> List[str]:
        wikipedia.set_lang('uk')
        page_object = wikipedia.page(start)
        page_links = page_object.links
        for i in page_links:
            if i in page_links:
                r = requests.get(f'https://uk.wikipedia.org/wiki/{i}')
                soup = BeautifulSoup(r.content, features='html.parser')
                all_rows = soup.find_all('span', {'class': 'mw-page-title-main'})
                for el in all_rows:
                    titles_on_page = el.get_text()
                    r = requests.get(f'https://uk.wikipedia.org/wiki/{titles_on_page}')
                    soup = BeautifulSoup(r.content, features='html.parser')
                    hrefs = [(soup.find('title'), b.get('href')) for b in soup.select(f'a[title="{finish}"]')]
                    for element in hrefs:
                        if element in hrefs:
                            bannedWord = ['Вікіпедія', '—']
                            title = element[0].get_text()
                            clear_title = (' '.join(i for i in title.split() if i not in bannedWord))
                            final_list = [f'{start}, {clear_title}, {finish}']
                            return print(final_list)
                        else:
                            print('Совпадений не найдено')


a = WikiRacer()
a.find_path(start='Гра', finish='Кіберспорт')
