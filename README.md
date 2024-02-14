# Small data analysis and viz projects

Repository for small-ish analysis and data viz projects. 

### 12/2021 UK Charities and their activities

Analysis using a new dataset that classifies and tags all active and inactive charities in the UK according to their activity/sector. This analysis explores how number of charities in specific activities have changed, whether specific sectors were more "trendy" at some point and whether others have died out. First time doing a streamgraph in python. Data available [here](https://charityclassification.org.uk/data/data-downloads/). 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2021/2112-charity-class/notebooks/Charity-classification-analysis.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187970817-49afe9b8-abb5-4560-a7ef-c2d2897176a5.png" width="500">

### 03/2022 Star Wars characters

Been playing around with some Star Wars data using [SWAPI](https://t.co/KSn5X00PmE) and found a great template for making nice looking tables in [matplotlib](https://matplotlib.org/matplotblog/posts/how-to-create-custom-tables/). 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2022/2203-starwars-table/notebooks/most-popular-characters-table-viz.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187971376-06c19d63-4133-4537-8d24-3779935cd7b6.png" width="350">

### 04/2022 Sourdough Google searches

First time using a new library ([pytrends](https://pypi.org/project/pytrends/)) to pull data from the Google Search API. Following a [blog I wrote](https://inside-numbers.com/kneading-to-relax-exploring-lockdown-baking-trends) last year on sourdough baking, was curious if interest in sourdough was only a peak during the pandemic or remained high.

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2022/2204-sourdough-google-trends/sourdough-google-trends-2019-2022.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187973494-33df8246-ee3f-467c-a090-e7a94771acce.png" width="500">

### 04/2022 Google searches of 'bike' across Europe

Another project using Google Search API to look at Google searches of 'bike' across Europe before & since the pandemic. Not much change in Scandinavia but higher interest in some countries suggesting a new normal? 🚲📈 

Heavily inspired by Google Trends [The New Normal](http://thenewnormal.is).

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2022/2204-bike-europe-google-trends/bike-searches-pandemic-europe.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187972006-03a0b617-79bf-4716-8fcc-d82aa0d5185b.png" width="350">

### 04/2022 Cycling rates in London

Been looking at London cycling rates and found rates of regular cyclists are higher in inner + SW London. Latest data ending Nov 2020 shows increases in some boroughs since the pandemic. Data sourced from [Active Life Survey](https://www.gov.uk/government/statistical-data-sets/walking-and-cycling-statistics-cw). The map layout is based on the squared map from the [London Data Store](https://data.london.gov.uk/dataset/excel-mapping-template-for-london-boroughs-and-wards). Checkout [my Twitter thread](https://twitter.com/LisaHornung_/status/1514551012694102018?s=20&t=kroA3czupkueRsOOz1DlTw) to see how it's put together. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2022/2204-prop-cycling-London-borough/cycling-rates-london-grid-tile-map.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187972669-bcd007ef-b0ec-46e9-8ae3-d765be3668d6.png" width="500">

### 07/2022 Gender pay gap (WIP)

Triggered by #TidyTuesday, got my hands on some gender pay gap data again. Worked up a couple of charts but wasn't too convinced where this was going. Wanted to focus on Tech vs charities, but haven't fully managed to do that yet. Was focused on trying out some new chart types, including beeswarm and ridge line plots. Might pick it up another time. Data comes from the [TidyTuesday repository](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-06-28). 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2022/2207-gender-pay-gap/GenderPayGap.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/187974455-73488cdf-e77b-4413-8684-2bd19e24e465.png" width="500">

### 08/2022 Exploring OSMnx for mapping in python

Discovered [OSMnx](https://osmnx.readthedocs.io/en/stable/), a python library to easily extract geospatial data from OpenStreetMaps. Explored a few different ways to extract and display data. Definitely quite a powerful tool. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2022/2208-OSMnx/Exploring-osmnx.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/213873819-8f1f6d6a-01b2-4985-8e50-15c0b76c14ad.png" height="250"><img src="https://user-images.githubusercontent.com/50448656/213873848-24580d8f-7af0-436e-86b4-2b33eb29cb37.png" height="250">

### 10/2022 Cycling in London

Continued playing around with cycling data for London. Updated the tilegrid map and created a few more charts. Definitely getting better at customising charts in matplotlib and using different chart types. Also turned the tile grid map into a Streamlit app (live app available [here](https://liloho-london-cycling-rates-app-kgvppz.streamlit.app/)).

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2022/2210-london-cycling/london_cycling_rates_exploration.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/213873978-e80b3788-3e8c-46c4-b34e-df7cd5c5f624.png" height="250"><img src="https://user-images.githubusercontent.com/50448656/213873988-6559bea2-7b41-4cdb-98a6-9e7b1d269866.png" height="250"><img src="https://user-images.githubusercontent.com/50448656/213874002-72192250-c7a7-4eb9-8917-18f412e13564.png" height="250">

### 01/2023 Cultural venues in London

Follow up from maps I created as part of the #30DayMapChallenge 2022. Fun to play around with fishnet grids in python and created some maps that display aggregate data per square km (here: cultural venues in London). Definitely something I'll come back to at some point.

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2301-culture-venues-london/cultural-venues-london-maps.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/213877655-1c1503a5-33dc-4fb4-b455-60203ea47fa4.png" width="500">

### 01/2023 Ridgemapp (WIP)

After falling in love with the ridge-map libarary, I'm currently working on a streamlit app that allows users to create their own ridge map designs. Watch this space ...

### 02/2023 Car ownership vs cycling rates in London

For #MapPromptMonday bivariate, created this quick map of cycling rates versus car ownership. Definitely want to dig a bit deeper into car ownership rates at some point. Also created a helper script to speed up bivariate colourmap creation in the future. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2302-car-ownership/cycling-vs-carowners-london-bivariate.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/219940282-353a8426-1b38-42b9-aff9-6cef9cc0d521.png" width="500">

### 04/2023 Artificial grass

A few weeks ago, I read an article about an increase in number of households replacing their lawns with artificial grass. I was wondering how sellers are promoting artificial grass and manually scraped some websites. Good project to get back to some NLP and text analysis. And I've always wanted to create a histogram that shows text instead of bars. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2304-artificial-grass/artificial-grass-marketing.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/235359833-66d6cb17-f11e-43b2-9210-ac3d52b00545.png" width="500">

### 05/2023 Google Search Autocomplete

Fun playing around with data from Google Search Autcomplete on "Why do cyclists ...". Managed to create a more complex layout in matplotlib using paths and bezier curves. Quite happy with the end result. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2305-google-search-autocomplete/google-search-autocomplete.ipynb)

<img src="https://user-images.githubusercontent.com/50448656/235903239-f5a90892-eb03-4f68-8342-a9bceabd9913.png" width="500">

### 06/2023 Trees of London

Map for #MapPromptMonday Plants showing total trees and main type per 4sqkm. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2306-trees-london/trees-london.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/9bcbc61a-4b5b-4900-826a-d9edcfbf3590" width="500">

### 07/2023 Gelaterias of Italy

Map for  #MapPromptMonday Desserts showing Ice cream shops in Italy. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2307-gelaterias/gelaterias-map.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/64d0397e-b0ae-466b-8ea8-1ee43ef4c841" width="350">

### 08/2023 Fix your bike voucher scheme

Came across the evaluation report for the Fix Your Bike voucher scheme that was run by the UK Department for Transport in 2020-2021 in an effort to increase active travel. The evaluation shows that reported levels of cycling have increased for people who have used their vouchers and got their bikes fixed. Read the full report [here](https://www.gov.uk/government/publications/fix-your-bike-voucher-scheme-evaluation)

Rough sketch for the chart made in python, final design tweaks in Figma. [Code here](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2308-fix-it-boris/fix-it-boris.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/f20bf0b8-0d38-4b4e-a667-cfea07c561be" width="500">

### 08/2023 Star Wars Scripts - Each line of Anakin episode 1

Found data for all six Star Wars scripts in [this Github repository](https://github.com/jcwieme/data-scripts-star-wars) by Jean Wieme. He kindly made this data available for others to experiment and use it in data viz. So I did. Wanted to plot each line of Anakin and who he speaks to for the first three episodes, but the addressant is only available for the first one. So I focused on getting the chart right for just one episode. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2308-star-wars-scripts/star-wars-scripts.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/67b09cc7-f596-4dfa-8666-123621d2309b" width="350">

### 10/2023 US grant opportunities

Contribution to #TidyTuesday exploring grant opportunities in the US. Found a great tutorial on how to create streamgraphs in python with the exact type of curve smoothing I wanted. Can't wait to use it for making a bumpchart. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2310-us-grants/us-grant-opportunities.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/78567697-4cd3-4189-b154-73d113fe4570" width="500">


### 12/2023 What C-3PO says

Reused data from Star Wars scripts I cleaned before to try bigram analysis (ie. co-occurence) of words said by 3-CPO. Network graph shows most common words that occured together. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2023/2312-starwars-what-XY-says/starwars-what-XY-says.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/f7c310b4-8a2d-4b39-aa2c-05e6fbf0960a" width="450">

### 01/2024 Birthdays of Canadian NHL Players

Chart for #TidyTuesday week 2 exploring birth dates of NHL players. Settled on a dotplot/stripplot and spent some time figuring out how to create a broken y-axis. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2024/2401-canadian-nhl-players/canadian-nhl-players.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/e118b643-c056-46e0-95d2-35c129ca82f0" width="450">


### 01/2024 Highest Paid Athletes

Chart for #MakeoverMonday looking at the World's Highest Paid Athletes. Used this simple data set to explore `plottable` - an awesome python library for creating stunning tables. 

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2024/2401-highest-paid-athletes/highest-paid-athletes.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/7c55b18f-84ab-449b-83bc-2ce29d4ee43c" width="500">


### 02/2024 Du Bois Visualization Challenge: 2024

Contributions to the [Du Bois Visualization Challenge 2024](https://github.com/ajstarks/dubois-data-portraits/tree/master/challenge/2024).

The goal is to celebrate the data visualization legacy of W.E.B Du Bois by recreating the visualizations from the 1900 Paris Exposition using modern tools - in my case Python.

[Full code](https://github.com/Lisa-Ho/small-data-projects/blob/main/2024/2402-dubois-challenge/dubois-challenge.ipynb)

<img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/b8902f90-a90c-49e7-8813-b893e58c3ae5" width="250"><img src="https://github.com/Lisa-Ho/small-data-projects/assets/50448656/e03740b1-77a0-441b-b14a-dd4dfd81802e" width="250">


