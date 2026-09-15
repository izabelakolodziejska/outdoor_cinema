# Warsaw outdoor cinema project


# Developer logs:
### 05.07
- project starts, base idea and setup
### 13.07
- virtual environment configuration, running docker container with postgres, run into an issue services.container_name must be a mapping: it was because of wrong indents
### 19.07
- connected to database via DBeaver
- research about outdoor cinemas (cinemas.md)
### 23.07
- python script **scraping_urls.py** for fetching suburls about individual cinema 
- results match those written out manually in **cinemas.md** (apart from those cinemas where schedule is on facebook, here manual addition will probably be a must)
### 25.07
- writing project objectives in **premise.md**
- moving text files into *notes* folder
- database schema created
### 09.08
- creating tables in database (**create.sql**)
### 23.08
- inserting test rows into database, find out primal key wasn't set to serial (fixed)
- extracting cinema's names from subpages
### 06.09
- scraped screening info and location of the cinemas
- dump results into a jsonl file (**cinemas.jsonl**)
### 10.09
- began working on data cleaning part
### 15.09
- figure out how to unflatten jsonl content (string from list of lists)
- splitting of movie title (works for first example)
- removing unnecessary tv show title (after "/")

### to-do's
- remove "" from titles
- extracting movie titles from file
- extracting cinema names 
- extracting date and time of screenings
- extracting address of cinema
- extracting district name of cinema
- inserting records into database
- handle duplicate logic 
- automate everything into one script
- optional: create automatic refresh schema
- dashboard research and implementation
- add script for searching extra data about movies (genre, etc)
- extend dashboard to this new data