# committee-communications-lookup

## web app stuff

I think the way to do this is actually to use
[FooTable](https://fooplugins.github.io/FooTable/docs/getting-started.html)
(which requires
[Bootstrap](http://getbootstrap.com/getting-started/)), which will
allow us to pretty easily make a
[filter table](https://fooplugins.github.io/FooTable/docs/examples/advanced/filter-dropdown.html). 

So we'll use pandas to get the data in the right format and to an html
[table](https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html),
then we use flask to get it set up as a web app and FooTable to do all
the nifty other stuff.

## Testing

To test on Windows, open up command prompt (Windows-x c), then go to the
repo's directory (`cd "Documents\Cong list\committee-communications-lookup"`)
and deploy the app locally (`heroku local -f Procfile.windows`).

To commit any changes and get them on the Github, open the Github desktop
application and press Sync in the top left, adding a message to explain what
you've done.

This will not change the deployed app on the website (at committee-
communications.herokuapp.com). To do that, you'll need to commit the changes
(which you do in the previous step) and then, on the command line from within
the committee-communications-lookup directory, type `git push heroku origin`
to deploy it on the web.

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
