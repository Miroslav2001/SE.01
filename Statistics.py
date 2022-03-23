import datetime
import pandas as pd
import arcade
from pathlib import Path
import openpyxl


class Statistics:

    def display_statistics(self):
        exel_file = pd.read_csv('store-result.csv')
        Name_gold = str(exel_file['Name'].iloc[0])
        Name_silver = str(exel_file['Name'].iloc[1])
        Name_bronze = str(exel_file['Name'].iloc[2])
        Score_gold = str(exel_file['Score'].iloc[0])
        Score_silver = str(exel_file['Score'].iloc[1])
        Score_bronze = str(exel_file['Score'].iloc[2])
        message = (Name_gold + "  -  " + Score_gold)
        arcade.draw_text(message, 200, 500, arcade.color.BLACK, 30)
        message = (Name_silver + "  -  " + Score_silver)
        arcade.draw_text(message, 200, 400, arcade.color.BLACK, 30)
        message = (Name_bronze + "  -  " + Score_bronze)
        arcade.draw_text(message, 200, 300, arcade.color.BLACK, 30)

    def sort_table(self):
        exel_file = pd.read_csv("store-result.csv")
        # the .sort_values method returns a new dataframe, so make sure to
        # assign this to a new variable.
        sorted_exel_file = exel_file.sort_values(by=["Score"], ascending=False)
        # Index=False is a flag that tells pandas not to write
        # the index of each row to a new column. If you'd like
        # your rows to be numbered explicitly, leave this as
        # the default, True
        sorted_exel_file.to_csv('store-result.csv', index=False)

    def storeResult(self, user_name, player_score):  # Store result, player name/ date and time of each game played
        mydate = datetime.datetime.now()
        csvstrdate = datetime.datetime.strftime(mydate, '%Y/%m/%d')
        csvstrtime = datetime.datetime.strftime(mydate, ' %H:%M:%S')
        resultTable = open('store-result.csv', 'a')
        # Here could be added any other feuture that would be needed for future development on the databse
        resultTable.write(csvstrdate + ',' + csvstrtime + ',' + str(user_name) + ',' + str(player_score) + '\n')  # Here is the order of how each attribute will be stored.
        resultTable.close()
