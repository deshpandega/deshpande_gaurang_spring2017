Final
========
-----------
Synopsis
------------
I am following the **Pattern 2** for finals.
This folder contains the the following files for Final submission:
>  ```final/DataCollection.ipynb```  file to collect data from 3 different APIs to gather data about English Premier League for analysis 1, 2 and 3
>  
>  ```final/data/*``` All the folders with json responses in them from each api link used for analysis. For eg. `teams` folder will contain `teams_response` from `teams` api 
>  ```final/analysis/ana[1-3]```*.ipynb* files for analysis 1, 2 and 3 
>  ```final/analysis/ana[1-3]/*``` *output* files for analysis 1, 2 and 3
>  
> 

-----------
Collecting Data
------------
Wrote *.ipynb* files to gather data about English Premier League. 
**```request```** module is used to fetch data, **```current_dir = os.path.dirname('__file__')```** is used to get current folder's relative path. 
```DataCollection.ipynb``` file is used to collect data about premier league from 3 different APIs providers. Two of them (The Sports DB and Fantasy Premier League) don't require any API key whereas the third one (Crowdscores) does require the api key. To get the API key, go to [this](https://customer.fastestlivescores.com/login) link and register. I have registered so I will send en email to Hari, TJ and Spandan my API key as backup.
APIs listed under **The Sports DB** are used to gather league details, team details and match details. 
APIs listed under **Crowdscores** are used to gather player details like goals scored, assists, yellow and red cards awarded to players. 
APIs listed under **Fantasy Premier League** are used to gather team details, more player stats like goals saved, penalties saved, penalties missed, own goals conceded, goals conceded, minutes played, player position, etc. 

####Data_Collection.ipynb
> **Logic:**
> 
> - Exported the crowdscore api key to bash terminal and read as an *environment variable*. 
> - Used a list to store the api names which will be used to fetch data. The list of apis used are:
> - -
> **From Sports DB:**
>  `search_all_leagues` to get league id for English Premier League
>  `lookup_all_teams`  to get list of team ids and details of all teams according to league id sent as input parameter
>  `lookup_all_players` to get details of all players according to team ids sent as input parameter. All team ids are stored in a list and the api is called in a for loop for each team id as input parameter and a single list of all players is maintained. Player details for each team are extended in a single list.
>  `eventsseason` to get details about each match in EPL according to league id retrived above and current season going on. If the current month is *July or before*, the season is *last year - current year*. If current month is *August or after*, season is *this year - next year*
>  **From Crowdscores.com**
>  `teams` to get list of team ids with api key and competition id as input parameters, (competition id 2 for EPL)
>  `seasons` to get season id with api key as input parameter
>  `rounds` to get round id with api key and competition id as input parameters, (competition id 2 for EPL)
>  `playerstats` to get player stats (goals, assists, yellow cards, red cards till now for current season) with api key, team id, round id, competition id, season id. The api is called in a for loop for each team id and response for players of each team are stored in separate file with name playerstats_response_< team_id >.json
>  **From Fantasy Premier League**
>  `bootstrap-static` to get list of all players, all teams, player positions and more player stats like saves, penalties saved, own goals scored, clean sheets, minutes played, penalties missed, goals conceded, etc.
>  
> - -
> - Wrote functions to create folder structure as follows:
> ```data/<api_name>/<api_name>_response.json``` except playerstats as mentioned above where I am using team id as well with the api name. Used relative path to create folders and to store json response in json file
> - Wrote a function to fetch response from APIs with input parameter as mentioned before. This method is  called for all the APIs so parameters for all APIs are sent as input parameters where required. Using ```if``` condition kept a check on API to fetch response from. Used ```payload``` to pass API key and rest of parameters. And returned the ```response``` object.
> - Wrote a method to process the response fetched from all the APIs and wrote to a json file. Check if the file exists, otherwise create the file. If the file is already present, get its content and compare with the content from response. If any player details or team details from response is already present in the file already existing, don't append it to the file. 
> - In a for loop, extract each API's name from its directory name and fetch its response. Send the response to process method mentioned above. Use ```time.sleep``` to make the system wait for some time before sending next request. This lets us fetch multiple responses in a for loop. 
> - The sequence of API calls is maintained strictly as response from first API is used as input parameter for next API and response from next API is used as input parameter for the API after that and so on. 
> - The response from each API will be stored in respective folder under data folders in json format.


-----------
Analysis 1
------------
Analysis 1 is about finding the highest contributing player in terms of goal scored. Goals scored by player to total goals scored by his team over the season is calculated and the ratio of player goals to team goals is considered. Relative path is used to read player stats for each team, all team names and matches played by each team; from ```final/data/playerstats/*```, `final/data/teams/*` and `final/data/eventsseason/*` folder. All players and teams are considered for this analysis. **```pandas DataFrame```** are used to hold all the details necessary for analysis.  **```seaborn```** bar plots are used to plot the graph and save to ```final/analysis/ana_1/biggest_contributors.png``` file

####ana_1.ipynb
> **Logic:**

> - Used relative path to fetch data from the sibling folder of parent folder of current file using `data_dir = os.path.join(current_dir, '..', 'data','playerstats','*')`, `team_dir = os.path.join(current_dir, '..', 'data','teams','*')` and `matches_dir = os.path.join(current_dir, '..', 'data','eventsseason','*')` 
> - Used `glob` to read file and `json.load(file)` to fetch data.
> - Details of all teams from `team_dir` are loaded into a dataframe and unwanted columns are removed.
> - Name of some of the teams are modified as to maintain consistency among other response from `matches_dir` and this dataframe is converted into a *dict*.
> - From each file having `playerstats`, team id is retrieved from file name and team name is retrieved from above *dict* using this team id
> - From each file having `playerstats`, list of players is created and list of goals scored by each player is created.
> - According to the team name retrieved from `team_dir`, goals scored by that team is retrieved from `matches_dir` (home + away)
> - A final dataframe is created with player, goals scored by player, player team and total goals scored by team as columns
> - Percent contribution by each player is calculated by player goals / team goals.
> - The dataframe is sorted by player contribution and goals scored
> - top 10 highest contributing players are loaded into a different data frame to plot.
> - Used 2 `barplot` from `seaborn` library to plot top 10 player goals and team goals on top of one another in a single plot. 
> - Populated x axis with top 10 player and y axis with their contribution, modified legends using `mpatches` library from matplotlib for better understanding.
> - Saved the plot using `fig.savefig()` method as a `.png` file with name **biggest_contributors.png**
> - The file with all players and their contributions is saved in `final/analysis/ana_1/biggest_contributors.csv`

####Plots


####Conclusion
This analysis gives insight about which team is most dependent on which of their players for goals. This analysis can be used to study about the players you need to mark if you are facing that particular team, or to identify replacement player if your top contributor is injured or unavailable for a game.

-----------
Analysis 2
------------
For Analysis 2, I am finding the statistics for each team per game. I am retrieving the goals scored by each team, shots on target by each team, yellow cards received by each team and red cards conceded by each team per match. I am also finding the shots on target and goals scored by each team vs the shots on target and goals scored by opposition team per game. Saving the output in a *csv* format and images in *png* format at ```final/analysis/ana_2/*```.
####ana_2.ipynb
> **Logic:**

> - Used relative path to fetch data from the sibling folder of parent folder of current file using ```matches_dir = os.path.join(current_dir, '..', 'data','eventsseason','*.json')```.
> - Used `glob` to read file and `json.load(file)` to fetch all match details from `eventsseason` API.
> - Using `for` comprehension, generated a `team_name` list with home team names for each match and restricted the search for date before today date using `datetime` module 
> - Using `for` comprehension, extended the same `team_name` list with away team names for each match and restricted the search for date before today date using `datetime` module.
> - Using `for` comprehension, generated a `team_score` list with home team score for each match and restricted the search for date before today date using `datetime` module
> - Using `for` comprehension, extended the same `team_score` list with away team score for each match and restricted the search for date before today date using `datetime` module.
> - Using `for` comprehension, generated a `team_shots` list with home team shots on target for each match and restricted the search for date before today date using `datetime` module
> - Using `for` comprehension, extended the same `team_shots` list with away team shots on target for each match and restricted the search for date before today date using `datetime` module.
> - Using `for` comprehension, generated a `team_yellow_cards` list with home team yellow cards count for each match and restricted the search for date before today date using `datetime` module
> - Using `for` comprehension, extended the same `team_yellow_cards` list with away team yellow cards count for each match and restricted the search for date before today date using `datetime` module.
> - Using `for` comprehension, generated a `team_red_cards` list with home team red cards count for each match and restricted the search for date before today date using `datetime` module
> - Using `for` comprehension, extended the same `team_red_cards` list with away team red cards count for each match and restricted the search for date before today date using `datetime` module.
> - Count the name and occurrence of each team name in `team_name` list which will give us the matches played by that team
> - Generate a separate list of all distinct teams and for each team, calculate the goals scored by that team vs goals scored by its opposition team in each match.
> - Similarly calculate the shots on target by each team vs shots on target be opposition team. 
> - Generate a data frame `team_df` with team name, score, shots on target, yellow cards and red cards for each match. This will have multiple entries for each team name with different set of data for all other columns.
> - Generate a second data frame `data` with team name, games played, goals scored, goals scored by opposition, shots on target by team, shots on target by opposition, goals per game, opposition goals per game, shots on target per gaema dn opposition shots on target per game.
> - Wrote a function to store `team_df` dataframe in csv format under `final/analysis/ana_2/team_stats.csv`.
> - Generated a custom color pallet with each color representing team jersey color.
> - Using `seaborn` library, plotted 3 `boxplot`and 1 `violin plot` showing shots per game, score per game, yellow cards per game and red cards per game respectively. For each plot, x axis represent the count and y axis represent the team name. Violin plot is very similar to boxplot except violin plot shows the *kernel density estimation* of the underlying distribution.
> - Saved the 3 box and 1 violin plots under `final/analysis/ana_2/*` folder with names `shots_per_game.png`, `score_per_game.png`, `yellow_cards_per_game.png` and `red_cards_per_game.png` respectively
> - Generated two copies of `data` as `data_shots` and `data_score`; each sorted by number of shots per game and number of goals scored per game respectively and stored in *csv* format with names `team_shots_performance.csv` and `team_score_performance.csv`.
> - Using `seaborn` library, plotted 2 `pointplot` showing shots on target per game and goals scored per game by each team. X axis represents count whereas y axis represent the team name.
> - Gridlines are made visible using `set_minor_locator` and `grid`properties
> - The plots are saved under `final/analysis/ana_2/*` folder with names `shots_on_target_per_game_for_all_teams_vs_opposition.png`, and `goals_scored_per_game_for_all_teams_vs_opposition.png`

####Conclusion
This analysis gives insight about teams performance over the season. It also helps in drafting what kind of strategy and formation you should be using while playing against any of the teams.

-----------
Analysis 3
------------
For Analysis 3, I am finding the top 30 best players from premier league. The player can be a goal keeper, a forward, a midfielder or a defender. The rating for each player is calculated using multiple parameters such that:
+goal, +assist, +penalties saved, +saves, +clean sheets will give positive score where as -yellow card, -red card, -penalties missed, -own goal, -goal conceded will give negative score
For each player, the minutes played is also considered
Output is stored in a *csv* format in `final/analysis/ana_3/best_players.csv` file and the graph is stored in `final/analysis/ana_3/best_players.png` file.
####ana_3.ipynb
> **Logic:**

> - Used relative path to fetch data from the sibling folder of parent folder of current file using ```data_dir = os.path.join(current_dir, '..', 'data','fpl','*.json')```.
> - Used `glob` to read file and `json.load(file)` to fetch all players details from `bootstrap-static` API from **Fantasy Premier League.**
> - Used separate lists to capture player name, goals scored, assists, penalties saved, saves made, clean sheets, yellow cards received, red cards received, penalties missed, own goals conceded, goals conceded and minutes played for each player.
> - Created dict having team id as key and team name as values and another dict having player type id as key and player role as value.
> - Create list of team name and player role according to team id and role id for that player.
> - Generated a data frame with player name, team name, role, goals, assists, penalties saved, saves, clean sheets, yellow cards, red cards, penalties missed, own goals, goals conceded, minutes played.
> - Score for each player is calculated such that: 
> each goals +3, each assists +1, each penalties saved +3, each saves +0.5, each clean sheet +0.5, each yellow -0.5, each red -1, each penalties missed -3, each own goal -3, each goal conceded -1
> - Rating for each player is calculated as score * 60 * 1.5 / minutes played (minutes played / 60 = hours played and hours played * 1.5 = 1 match played)
> - If the player is getting rating as `NaN` i.e. he has not played for even a singloe minute, mark his rating as 0.00
> - Sort the data frame according to rating, goals, assists, saves in descending order
> - Copy top 30 of them in a different dataframe for plotting.
> - Save the file with all players in `final/analysis/ana_3/best_players.csv`
> - Plotted a swarm plot using `seaborn` library showing top 30 best rated players in EPL. Saved this plot in file `final/analysis/ana_3/best_players.png`

####Conclusion
This analysis gives insight about player performance over the season. It helps in finding the best performing team for next matches. It also helps in finding the right player you may want to sign in the transfer window in future.