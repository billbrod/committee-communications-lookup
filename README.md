# committee-communications-lookup

## web app stuff

Will try and use Bokeh to generate the table I want, with dropdown
widget. Most of work will be in attempting to learn enough JavaScript
to use dropdown as a filter.

Will also attempt to embed bokeh table within flask app so that we can
modify the appearance of the resulting html more. 

Useful links:

- [flask and pandas](https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html)
- [flask, bokeh, and heroku](http://blog.thedataincubator.com/2015/09/painlessly-deploying-data-apps-with-bokeh-flask-and-heroku/)
- [how to embed bokeh charts](http://bokeh.pydata.org/en/0.11.0/docs/user_guide/embed.html)
- [stackoverflow post about embedding bokeh in flask](http://stackoverflow.com/questions/33450773/embedding-a-bokeh-plot-in-flask)
- [bokeh interactive components](http://bokeh.pydata.org/en/0.11.1/docs/user_guide/interaction.html)

## functionality

This is a web app to get a roster of the contact info for senators/reps in specific committees or sub-committees. You will be able to select the committee you are interested in, and then receive pertinent Washington contact information.

TERMINOLOGY: For the remainder of this README, "congressperson" will be abbreviated to "CP." The "House of Representatives" is "HR."

GOAL: Generate lists of contact information for easy contacting of multiple CPs. Target specific committees for specific issues and bills.

STAGE 1: Select a committee, generate roster with contact info, with
checkboxes to select what info to display . Roster can be downloaded.
  - Use "bioguide" as marker for each CP.
  - From **"committees-current.yaml"** :
    - `["type"]` 
    - `["name"]`
    - `["senate_committee_id"]`
    - `["house_committee_id"]`
    - `["subcommittees"]["name"]`
    - `["subcommittees"]["thomas_id"]`
    - `["subcommittees"]["phone"]`
  - From **"committee-membership-current"** :
    - the "senate_committee_id" or "house_committee_id" with&without subcommittee thomas numbers. Example: "SSAP17" . Underneath:
    - `["bioguide"]`
    - `["title"]`
  - From **"legislators-current.yaml"** : (after `"id"`)
    - `["bioguide"]`
    - `["name"]["official_full"]`
    - `["bio"]["gender"]`
    - Term, one that ends after the current date
      - `["type"]`
      - `["state"]`
      - `["district"]` (only relevant for HR)
      - `["address"]` in zip code "20510"
      - `["phone"]` beginning with "202"
      - `["fax"]` beginning with "202"
      - `["contact_form"]`
      - `["office"]`
  - From **"legistlators-social-media.yaml"** : (after `"id"`)
      - `["bioguide"]`
      - `["social"]["twitter"]`
      - `["social"]["facebook"]`


Stage 2: Choose a bill, it generates the roster contact list for the relevant committee.

Stage 3: Roster contact list can be texted to a phone number or a group chat.

Stage 4: Roster contact list numbers can be called through Google Hangouts or similar program.
