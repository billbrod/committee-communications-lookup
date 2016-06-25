# committee-communications-lookup
This is a web app to get a roster of the contact info for senators/reps in specific committees or sub-committees. You will be able to select the committee you are interested in, and then receive pertinent Washington contact information.

TERMINOLOGY: For the remainder of this README, "congressperson" will be abbreviated to "CP." The "House of Representatives" is "HR."

GOAL: Generate lists of contact information for easy contacting of multiple CPs. Target specific committees for specific issues and bills.

STAGE 1: Select a committee, generate roster with contact info. Roster can be downloaded.
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
  -From **"legistlators-social-media.yaml"** : (after `"id"`)
      - `["bioguide"]`
      - `["social"]["twitter"]`
      - `["social"]["facebook"]`

Stage 2: Choose a bill, it generates the roster contact list for the relevant committee.

Stage 3: Roster contact list can be texted to a phone number or a group chat.

Stage 4: Roster contact list numbers can be called through Google Hangouts or similar program.
