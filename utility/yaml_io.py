import yaml


class My_yaml:
    name: str
    data: str

    def file_save(self, data, name):
        self.data = data
        self.name = name
        try:
            with open(name, 'w') as yml_file:
                yaml_file = yaml.dump(self.data, yml_file)
        except Exception as e:
            print('Error while saving file')


    def file_open(self, name):
        self.name = name
        try:
            with open(name, 'r') as yml_file:
                my_file = yaml.load(yml_file, Loader=yaml.FullLoader)
        except Exception as e:
            print('Error while opening file')

        return my_file
