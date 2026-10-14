
import json


class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename
        self.favorites = {}

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            if isinstance(data, dict):
                self.favorites = {
                    name.lower(): location
                    for name, location in data.items()
                }

        except (FileNotFoundError, json.JSONDecodeError, OSError):
            self.favorites = {}

    def add(self, name, location):
        name = name.lower()

        if name in self.favorites:
            return False

        self.favorites[name] = location
        self._save()
        return True

    def remove(self, name):
        name = name.lower()

        if name not in self.favorites:
            return False

        del self.favorites[name]
        self._save()
        return True

    def list_all(self):
        return self.favorites.copy()

    def get_location(self, name):
        return self.favorites.get(name.lower())

    def _save(self):
        with open(self.filename, "w") as file:
            json.dump(self.favorites, file, indent=4)
