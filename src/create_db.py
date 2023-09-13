from db import DBO


class CreateDB(DBO):
    CREATE_REGIONS = """
        CREATE TABLE IF NOT EXISTS region (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        );"""

    CREATE_COUNTRY = """
        CREATE TABLE IF NOT EXISTS country (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            alpha2Code TEXT,
            alpha3Code TEXT,
            population INTEGER,
            region_id INTEGER,
            FOREIGN KEY (region_id) REFERENCES region(id)
        );"""

    def run(self):
        self.cursor.execute(self.CREATE_REGIONS)
        self.cursor.execute(self.CREATE_COUNTRY)


if __name__ == "__main__":
    CreateDB().run()
