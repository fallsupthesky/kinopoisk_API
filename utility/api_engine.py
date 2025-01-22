import requests
import json
import config.config as config
from utility import yaml_io


class Api_engine():

    api_key: str
    headers: set
    URL: str

    def __init__(self):

        self.api_key = config.api_key
        self.URL = config.URL_id
        self.headers = {'X-API-KEY': str(self.api_key)}

    def __get_movie_id(self):
        """get movie by it's kinopoisk ID in string format from yml file"""

        my_yaml = yaml_io.My_yaml()
        try:
            movie = my_yaml.file_open('C:/Users/Pavel/PycharmProjects/kinopoisk/data/movie_id.yml')
        except Exception as e:
            print('Error while opening movie-id.yml')


        return str(movie.get('id'))


    def get_movie_info(self):
        """ Get movie info from kinopoisk unofficial API"""

        try:
            self.URL += self.__get_movie_id() # making up correct URL with certain movie id
        except Exception as e:
            print('Can\'t get movie ID')

        try:
            r = requests.get(url=self.URL, headers=self.headers)
        except Exception as e:
            print('Can\'t get correct response from server')

        try:
            json_data = r.json()
            movie_info = json.dumps(json_data, indent=4, ensure_ascii=False)
            #print(movie_info)  # С отступами
        except ValueError:
            print("Ответ не содержит JSON.")

        return movie_info


    def write_movie_info(self):
        try:
            data = self.get_movie_info()
            name = 'C:/Users/Pavel/PycharmProjects/kinopoisk/data/movie_info.yaml'
            my_yaml = yaml_io.My_yaml()
            my_yaml.file_save(data, name)
        except Exception as e:
            print('Error while writing file')


#my_req = Api_engine()
#print(my_req.get_movie_info())
#my_req.write_movie_info()
