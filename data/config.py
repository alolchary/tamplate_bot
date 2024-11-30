from configparser import ConfigParser
import os


class Config:
    
    def __init__(self, path: str = "settings.ini") -> None:
        self.path = path
        self.config = ConfigParser()
        
        self.architecture = {
            "Bot": {
                    "token": "", 
                    "admin_ids": ""
                    },
            
            "DataBase": {
                    "session_url": ""
                        }
        }

    def create_config(self) -> None:

        for item in self.architecture:
            self.config.add_section(item)
            for i in self.architecture[item]:
                self.config.set(item, i, self.architecture[item][i])



        with open(self.path, "w") as config_file:
            self.config.write(config_file)

        print(f'[!] Успешно создал конфиг, выключаю бота (Заполните {self.path})')
        exit()

    def load_config(self) -> None:
        if not os.path.exists(self.path):
            self.create_config()

        self.config.read(self.path)
        self.BOT_TOKEN: str = self.config.get("Bot", "token")
        self.ADMINS: list[int] = self.config.get("Bot", "admin_ids").replace(" ", "").split(',')
        self.session_url: str = self.config.get('DataBase', "session_url")