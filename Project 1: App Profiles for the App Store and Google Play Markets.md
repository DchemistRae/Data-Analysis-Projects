
#Profitable App Profiles for the App Store and Google Play Markets

The goal of this project is to analyse app download data, to understand what type of apps attract more users on Google Play and the App Store.


```python
from csv import reader
opened_apple = open('AppleStore.csv')
applestore = reader(opened_apple)
```


```python
opened_play = open('googleplaystore.csv')
playstore = reader(opened_play)
```


```python
playstore_list = list(playstore)
applestore_list = list(applestore)
```


```python
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
```


```python
apple_explore = explore_data(applestore_list,1,5)
print('\n')
play_explore = explore_data(playstore_list,1,5)
```

    ['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']
    
    
    ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']
    
    
    ['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1']
    
    
    ['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1']
    
    
    
    
    ['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']
    
    
    ['Coloring book moana', 'ART_AND_DESIGN', '3.9', '967', '14M', '500,000+', 'Free', '0', 'Everyone', 'Art & Design;Pretend Play', 'January 15, 2018', '2.0.0', '4.0.3 and up']
    
    
    ['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']
    
    
    ['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up']
    
    



```python
print(applestore_list[0])
print('\n')
print(playstore_list[0])
```

    ['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']
    
    
    ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']



```python
for row in playstore_list:
    if len(row) != len(playstore_list[0]):
        print(playstore_list.index(row),'\n',row)
        

```

    10473 
     ['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']



```python
del playstore_list[10473]
```


```python
unique = []
duplicates = []
for apps in playstore_list:
    name = apps[0]
    if name in unique:
        duplicates.append(name)
    else:
        unique.append(name)
```


```python
print(duplicates[0:6])
```

    ['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business', 'ZOOM Cloud Meetings', 'join.me - Simple Meetings', 'Box']


Duplicates would be removed using a criteria, app with highest number of reviews would remain. While its duplicates with lower numbers would be deleted


```python
reviews_max = {}
for apps in playstore_list[1:]:
    name = apps[0]
    n_review = float(apps[3])
    if name in reviews_max and reviews_max[name] < n_review:
        reviews_max[name] = n_review
    if name not in reviews_max:
        reviews_max[name] = n_review       
```


```python
len(reviews_max) #correct
```




    9659



A new list `android_clean` would take the list of list of new cleaned duplicate free data. While already added would store names of new added apps.


```python
android_clean = []
already_added = []
for apps in playstore_list[1:]:
    name = apps[0]
    n_reviews = float(apps[3])
    if (n_reviews == reviews_max[name]) and (name not in already_added):
        android_clean.append(apps)
        already_added.append(name)
```


```python
len(android_clean)
```




    9659



We will now check for non English alphabets in apps name to detect non English apps, and later delete them. If non English aplhabets are more than 3 function returns False, else the function should return True.


```python
def checkstring(word):
    count = 0
    for characters in word:
        chars = characters
        if ord(chars) > 127:
            count += 1
            if count > 3:
                return False
    return True
```


```python
checkstring('Instagram')
```




    True




```python
checkstring("爱奇艺PPS -《欢乐颂2》电视剧热播")
```




    False




```python
checkstring('Docs To Go™ Free Office Suite')
```




    True




```python
checkstring('Instachat 😜')
```




    True



Non English apps removed below


```python
english_droid_apps = []
english_apple_apps = []
for apps in android_clean:
    name = apps[0]
    if checkstring(name) == True:
        english_droid_apps.append(apps)
        
for app in applestore_list:
    name = app[0]
    if checkstring(name) == True:
        english_apple_apps.append(app)
```


```python
len(english_droid_apps)
```




    9614




```python
len(english_apple_apps)
```




    7198



Isolate the free apps from both datasets


```python
free_droid_apps = []
free_ios_apps = []
for apps in english_droid_apps:
    price = apps[6]
    if price == 'Free':
        free_droid_apps.append(apps)
for apps in english_apple_apps:
    price = apps[4]
    if price == '0.0':
        free_ios_apps.append(apps)
```


```python
len(free_droid_apps)
```




    8863




```python
len(free_ios_apps)
```




    4056



Because our end goal is to add the app on both Google Play and the App Store, we need to find app profiles that are successful on both markets.  


```python
def freq_table(dataset,index):
    freq_dict = {}
    for items in dataset:
        value = items[index]
        if value in freq_dict:
            freq_dict[value] += 1
        else:
            freq_dict[value] = 1 
    table_percentages = {}
    for key in freq_dict:
        percentage = (freq_dict[key] / len(freq_dict)) * 100
        table_percentages[key] = percentage 
    
    return table_percentages
    
```


```python
def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
```


```python
print("Prime genres")
display_table(free_ios_apps,11)
```

    Prime genres
    Games : 9813.04347826087
    Entertainment : 1452.1739130434783
    Photo & Video : 726.0869565217391
    Social Networking : 621.7391304347826
    Education : 573.9130434782609
    Shopping : 526.0869565217391
    Utilities : 473.9130434782608
    Lifestyle : 408.69565217391306
    Finance : 365.2173913043478
    Sports : 343.47826086956525
    Health & Fitness : 330.4347826086956
    Music : 291.30434782608694
    Book : 286.95652173913044
    Productivity : 269.5652173913044
    News : 252.17391304347828
    Travel : 243.47826086956525
    Food & Drink : 186.95652173913044
    Weather : 134.7826086956522
    Reference : 86.95652173913044
    Navigation : 86.95652173913044
    Business : 86.95652173913044
    Catalogs : 39.130434782608695
    Medical : 34.78260869565217


For prime genre column English apps in Apple store; 
Games are the most common genre, entertainment apps are generally more downloaded than productivity apps.


```python
print('Genres')
display_table(free_droid_apps,9)
```

    Genres
    Tools : 657.0175438596491
    Entertainment : 471.9298245614035
    Education : 415.7894736842105
    Business : 357.01754385964915
    Productivity : 302.6315789473684
    Lifestyle : 302.6315789473684
    Finance : 287.719298245614
    Medical : 274.56140350877195
    Sports : 269.2982456140351
    Personalization : 257.89473684210526
    Communication : 251.75438596491227
    Action : 241.2280701754386
    Health & Fitness : 239.47368421052633
    Photography : 228.9473684210526
    News & Magazines : 217.54385964912282
    Social : 207.01754385964915
    Travel & Local : 180.70175438596493
    Shopping : 174.56140350877195
    Books & Reference : 166.66666666666669
    Simulation : 158.7719298245614
    Dating : 144.73684210526315
    Arcade : 143.859649122807
    Video Players & Editors : 137.71929824561403
    Casual : 136.8421052631579
    Maps & Navigation : 108.77192982456141
    Food & Drink : 96.49122807017544
    Puzzle : 87.71929824561403
    Racing : 77.19298245614034
    Role Playing : 72.80701754385966
    Libraries & Demo : 72.80701754385966
    Auto & Vehicles : 71.9298245614035
    Strategy : 70.17543859649122
    House & Home : 64.03508771929825
    Weather : 62.28070175438597
    Events : 55.26315789473685
    Adventure : 52.63157894736842
    Comics : 47.368421052631575
    Beauty : 46.49122807017544
    Art & Design : 46.49122807017544
    Parenting : 38.59649122807017
    Card : 35.08771929824561
    Casino : 33.33333333333333
    Trivia : 32.45614035087719
    Educational;Education : 30.701754385964914
    Board : 29.82456140350877
    Educational : 28.947368421052634
    Education;Education : 26.31578947368421
    Word : 20.175438596491226
    Casual;Pretend Play : 18.421052631578945
    Music : 15.789473684210526
    Racing;Action & Adventure : 13.157894736842104
    Puzzle;Brain Games : 13.157894736842104
    Entertainment;Music & Video : 13.157894736842104
    Casual;Brain Games : 10.526315789473683
    Casual;Action & Adventure : 10.526315789473683
    Arcade;Action & Adventure : 9.649122807017543
    Action;Action & Adventure : 7.894736842105263
    Educational;Pretend Play : 7.017543859649122
    Simulation;Action & Adventure : 6.140350877192982
    Parenting;Education : 6.140350877192982
    Entertainment;Brain Games : 6.140350877192982
    Board;Brain Games : 6.140350877192982
    Parenting;Music & Video : 5.263157894736842
    Educational;Brain Games : 5.263157894736842
    Casual;Creativity : 5.263157894736842
    Art & Design;Creativity : 5.263157894736842
    Education;Pretend Play : 4.385964912280701
    Role Playing;Pretend Play : 3.508771929824561
    Education;Creativity : 3.508771929824561
    Role Playing;Action & Adventure : 2.631578947368421
    Puzzle;Action & Adventure : 2.631578947368421
    Entertainment;Creativity : 2.631578947368421
    Entertainment;Action & Adventure : 2.631578947368421
    Educational;Creativity : 2.631578947368421
    Educational;Action & Adventure : 2.631578947368421
    Education;Music & Video : 2.631578947368421
    Education;Brain Games : 2.631578947368421
    Education;Action & Adventure : 2.631578947368421
    Adventure;Action & Adventure : 2.631578947368421
    Video Players & Editors;Music & Video : 1.7543859649122806
    Sports;Action & Adventure : 1.7543859649122806
    Simulation;Pretend Play : 1.7543859649122806
    Puzzle;Creativity : 1.7543859649122806
    Music;Music & Video : 1.7543859649122806
    Entertainment;Pretend Play : 1.7543859649122806
    Casual;Education : 1.7543859649122806
    Board;Action & Adventure : 1.7543859649122806
    Video Players & Editors;Creativity : 0.8771929824561403
    Trivia;Education : 0.8771929824561403
    Travel & Local;Action & Adventure : 0.8771929824561403
    Tools;Education : 0.8771929824561403
    Strategy;Education : 0.8771929824561403
    Strategy;Creativity : 0.8771929824561403
    Strategy;Action & Adventure : 0.8771929824561403
    Simulation;Education : 0.8771929824561403
    Role Playing;Brain Games : 0.8771929824561403
    Racing;Pretend Play : 0.8771929824561403
    Puzzle;Education : 0.8771929824561403
    Parenting;Brain Games : 0.8771929824561403
    Music & Audio;Music & Video : 0.8771929824561403
    Lifestyle;Pretend Play : 0.8771929824561403
    Lifestyle;Education : 0.8771929824561403
    Health & Fitness;Education : 0.8771929824561403
    Health & Fitness;Action & Adventure : 0.8771929824561403
    Entertainment;Education : 0.8771929824561403
    Communication;Creativity : 0.8771929824561403
    Comics;Creativity : 0.8771929824561403
    Casual;Music & Video : 0.8771929824561403
    Card;Action & Adventure : 0.8771929824561403
    Books & Reference;Education : 0.8771929824561403
    Art & Design;Pretend Play : 0.8771929824561403
    Art & Design;Action & Adventure : 0.8771929824561403
    Arcade;Pretend Play : 0.8771929824561403
    Adventure;Education : 0.8771929824561403



```python
print('Category')
display_table(free_droid_apps,1)
```

    Category
    FAMILY : 5075.757575757576
    GAME : 2612.121212121212
    TOOLS : 2272.7272727272725
    BUSINESS : 1233.3333333333335
    LIFESTYLE : 1048.4848484848485
    PRODUCTIVITY : 1045.4545454545455
    FINANCE : 993.939393939394
    MEDICAL : 948.4848484848485
    SPORTS : 912.1212121212121
    PERSONALIZATION : 890.9090909090909
    COMMUNICATION : 869.6969696969697
    HEALTH_AND_FITNESS : 827.2727272727274
    PHOTOGRAPHY : 790.9090909090909
    NEWS_AND_MAGAZINES : 751.5151515151515
    SOCIAL : 715.1515151515151
    TRAVEL_AND_LOCAL : 627.2727272727273
    SHOPPING : 603.030303030303
    BOOKS_AND_REFERENCE : 575.7575757575758
    DATING : 500.0
    VIDEO_PLAYERS : 481.8181818181818
    MAPS_AND_NAVIGATION : 375.75757575757575
    FOOD_AND_DRINK : 333.33333333333337
    EDUCATION : 312.1212121212121
    ENTERTAINMENT : 257.57575757575756
    LIBRARIES_AND_DEMO : 251.5151515151515
    AUTO_AND_VEHICLES : 248.4848484848485
    HOUSE_AND_HOME : 221.2121212121212
    WEATHER : 215.15151515151513
    EVENTS : 190.9090909090909
    PARENTING : 175.75757575757575
    ART_AND_DESIGN : 172.72727272727272
    COMICS : 166.66666666666669
    BEAUTY : 160.6060606060606


It seems that a good number of apps on playstore are designed for practical purposes (family, tools, business, lifestyle, productivity, etc.). However, if we investigate this further, we can see that the family category (which accounts for almost 19% of the apps) are mostly games for kids.

Up to this point, we found that the App Store is dominated by apps designed for fun, while Google Play shows a more balanced landscape of both practical and for-fun apps.


```python
genres_ios = freq_table(free_ios_apps, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in free_ios_apps:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)
```

    Utilities : 14010.100917431193
    Music : 56482.02985074627
    Reference : 67447.9
    Medical : 459.75
    News : 15892.724137931034
    Navigation : 25972.05
    Health & Fitness : 19952.315789473683
    Travel : 20216.01785714286
    Finance : 13522.261904761905
    Education : 6266.333333333333
    Business : 6367.8
    Food & Drink : 20179.093023255813
    Entertainment : 10822.961077844311
    Book : 8498.333333333334
    Social Networking : 53078.195804195806
    Sports : 20128.974683544304
    Lifestyle : 8978.308510638299
    Catalogs : 1779.5555555555557
    Weather : 47220.93548387097
    Productivity : 19053.887096774193
    Photo & Video : 27249.892215568863
    Games : 18924.68896765618
    Shopping : 18746.677685950413


Reference apps have the highest number of user reviews as shown above

Displays the install column for android apps


```python
display_table(free_droid_apps, 5) #installs columns
```

    1,000,000+ : 6970.0
    100,000+ : 5120.0
    10,000,000+ : 4675.0
    10,000+ : 4520.0
    1,000+ : 3720.0000000000005
    100+ : 3065.0
    5,000,000+ : 3025.0
    500,000+ : 2465.0
    50,000+ : 2115.0
    5,000+ : 2000.0
    10+ : 1570.0
    500+ : 1440.0
    50,000,000+ : 1019.9999999999999
    100,000,000+ : 944.9999999999999
    50+ : 850.0
    5+ : 350.0
    1+ : 225.0
    500,000,000+ : 120.0
    1,000,000,000+ : 100.0
    0+ : 20.0



```python
categories_android = freq_table(free_droid_apps, 1)

for category in categories_android:
    total = 0
    len_category = 0
    for app in free_droid_apps:
        category_app = app[1]
        if category_app == category:            
            n_installs = app[5]
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    print(category, ':', avg_n_installs)
```

    SHOPPING : 7036877.311557789
    TOOLS : 10801391.298666667
    BOOKS_AND_REFERENCE : 8767811.894736841
    TRAVEL_AND_LOCAL : 13984077.710144928
    AUTO_AND_VEHICLES : 647317.8170731707
    LIFESTYLE : 1437816.2687861272
    HOUSE_AND_HOME : 1331540.5616438356
    PERSONALIZATION : 5201482.6122448975
    FAMILY : 3697848.1731343283
    EVENTS : 253542.22222222222
    PARENTING : 542603.6206896552
    DATING : 854028.8303030303
    VIDEO_PLAYERS : 24727872.452830188
    LIBRARIES_AND_DEMO : 638503.734939759
    WEATHER : 5074486.197183099
    HEALTH_AND_FITNESS : 4188821.9853479853
    EDUCATION : 1833495.145631068
    ART_AND_DESIGN : 1986335.0877192982
    BEAUTY : 513151.88679245283
    FOOD_AND_DRINK : 1924897.7363636363
    MAPS_AND_NAVIGATION : 4056941.7741935486
    GAME : 15588015.603248259
    PHOTOGRAPHY : 17840110.40229885
    FINANCE : 1387692.475609756
    SOCIAL : 23253652.127118643
    COMICS : 817657.2727272727
    NEWS_AND_MAGAZINES : 9549178.467741935
    COMMUNICATION : 38456119.167247385
    BUSINESS : 1712290.1474201474
    SPORTS : 3638640.1428571427
    MEDICAL : 120550.61980830671
    ENTERTAINMENT : 11640705.88235294
    PRODUCTIVITY : 16787331.344927534



```python
From the result above, we can immediately notice that communication apps have 
```
