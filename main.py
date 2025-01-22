from utility import api_engine
import yaml

class Main:

    def run(self):
        engine = api_engine.Api_engine()
        engine.write_movie_info()

obj = Main()
obj.run()


