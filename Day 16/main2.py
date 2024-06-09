from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",['Pikachu','Squirtle','Ditto'])
table.add_column("type",['thunder','Water','Unknown'])

print(table)