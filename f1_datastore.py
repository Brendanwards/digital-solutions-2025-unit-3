import sqlite3
import csv


class Datastore:
    """
    Datastore for the f1 driver database
    """

    def __init__(self, database_file: str, data_file: str):
        """
        initialises the datastore
        """
        self.database_file = database_file
        self.data_file = data_file
        self.conn = sqlite3.connect(self.database_file)
        self.cursor = self.conn.cursor()

        self.populate_database()
        self.conn.commit()
    def populate_database(self):
        """
        populates the database with data from the csv file
        """
        with open(self.data_file, mode="r", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)

            # process the CSV data
            for record in csv_reader:

                name = record["Driver"]
                nationality = record["Nationality"]
                race_entries = int(float(record["Race_Entries"]))
                race_starts = int(float(record["Race_Starts"]))
                pole_positions = int(float(record["Pole_Positions"]))
                race_wins = int(float(record["Race_Wins"]))
                podiums = int(float(record["Podiums"]))
                fastest_laps = int(float(record["Fastest_Laps"]))
                points = float(record["Points"])

                # view the driver data
                self.add_driver(
                    name,
                    nationality,
                    race_entries,
                    race_starts,
                    pole_positions,
                    race_wins,
                    podiums,
                    fastest_laps,
                    points,
                )

    def add_driver(
        self,
        name: str,
        nationality: str,
        race_entries: int,
        race_starts: int,
        pole_positions: int,
        race_wins: int,
        podiums: int,
        fastest_laps: int,
        points: float,
    ):
        """
        adds a driver to the database
        """
        self.cursor.execute(
            """
            INSERT INTO Driver (name, nationality, race_entries, race_starts, pole_positions, race_wins, podiums, fastest_laps, points)
            VALUES (:name, :nationality, :race_entries, :race_starts, :pole_positions, :race_wins, :podiums, :fastest_laps, :points)
            """,
            {
                "name": name,
                "nationality": nationality,
                "race_entries": race_entries,
                "race_starts": race_starts,
                "pole_positions": pole_positions,
                "race_wins": race_wins,
                "podiums": podiums,
                "fastest_laps": fastest_laps,
                "points": points,
            },
        )

