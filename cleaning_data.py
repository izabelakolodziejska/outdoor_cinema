import json 
import itertools

with open("cinemas.jsonl", "r", encoding='utf8') as file:
    for line in file:
        data = json.loads(line.strip()) #single line 
        content = [data["content"]]
        content_per_cinema = list(itertools.chain.from_iterable(content))
        content_per_screenings = list(itertools.chain.from_iterable(content_per_cinema))
        #print(content_per_screenings)

        # it is a list for screenings in given cinema
        for screening in content_per_screenings:
            #print(screening)
            title = screening.split("–", 1)[1]

            # removing additional titles (eg. in one cinema there is movie title / tv show episode screening, we dont need tv show in this project so I remove this title
            if "/" in title:
                title = title.split("/")[0]
            print(title)
            print(f"\n NEXT \n")