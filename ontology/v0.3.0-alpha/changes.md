Converted all skos:preflabel annotation properties to the more standard rdfs:label
Removed vann namespace and converted preferredNamespacePrefix to skos:altLabel
Added rdfs:isDefinedBy with the current IRI to every class

Added Speakeasy under Bars
Redefined Pets
Redefined Bachelors
Redefined Bachelorette
Redefined Family
Redefined Health
Renamed Style to Fashion
  I think this was left as Style originally to allow for stuff like home and furniture styles... we can add it later if needed, e.g., Style > Fashion and whatever other subclasses we want
  For now, there is an AltLabel on Fashion: "Style"
Added Home Improvement under Home
-Redefined Babysitting
Added Teenage Years under Child Life Stages
  I now believe the classes Elementary Years, High School Years, Junior High Years and Middle School Years are somewhat unnecessary, but still may provide web authors with more flexibility
Renamed State to US State
Fixed typo in Tampa Bay definition
Added Cape Canaveral under Space Coast
Redefined Exercise
Redefined Gyms
Redefined Author
  Is this the same as Writer?
Renamed and redefined New Smyrna to New Smyrna Beach
Renamed and redefined Palm Beaches to Palm Beach
Removed Johns Pass
Added Fernandina Beach under Northeast Florida
Fixed the newly added classes having the '/' delimiter instead of '#'
Added definitions to all locations
Redefined Dating, Engagement and Marriage
Redefined Holidays
Defined all terms in the Holidays tree
  Can be changed later with a script
Added dashes to the Trick or Treating label
Renamed National Chocolate Day to World Chocolate Day
Added apostrophes to Mothers Day, Fathers Day, New Years, New Years Eve and New Years Eve Fireworks
Redefined Season
Redefined Shopping
Redefined Parade
Added an apostrophe to Farmers Market
Moved Contests under Events
Moved Festivals under Events
Added new class Music Festivals under Festivals
Defined the Team Sports subclasses

Added outgoing links to DBPedia and Wikidata to the Animals tree
Added outgoing links to DBPedia and Wikidata to the Audience tree
Added outgoing links to DBPedia and Wikidata to the Health tree
Added outgoing links to DBPedia and Wikidata to the News tree
Added outgoing links to DBPedia and Wikidata to Work
Added outgoing links to DBPedia and Wikidata to the People tree
Added outgoing links to DBPedia and Wikidata to the Home tree
  DBPedia/Wikidata equate Junior High and Middle School, but in my understanding of it, the two are slightly different; in any case, having the two terms gives web authors more flexibility
Added outgoing links to DBPedia and Wikidata to the Family tree
Added outgoing links to DBPedia and Wikidata to the Region tree
Added outgoing links to DBPedia and Wikidata to the Things To Do tree

Because of issues with pyLODE, had to change outgoing link predicates
  rdfs:seeAlso to skos:example
  owl:sameAs to dct:source

Added dbpedia and wikidata as prefixes

Classes missing outgoing link(s):
The entire Special Content tree
  Not applicable
Back To School
Schools by Governance
Schools by Life Stage
Elementary Years
High School Years
Junior High Years
Pre Pregnancy
Southeast Florida
Interesting People
  Not applicable
Cultural Holidays
Holiday Months
Religious Holidays
Scene
Date Night
Family Fun
Girls Night Out
Live Music
Special Occasions
Accomodation
Birthday Party Venue
Camps
Fall Festival
Pumpkin Patch
Deals
Getaways
Weekend Getaway
Things To Do