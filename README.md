# fate-bot
This project is a personal hobby for gaining experience with Python - specifically web scraping and database interaction with live sites - and the Discord API
---------------------------------------------------------------------------------------------------------------------------------------------------------------
Discord.py bot that retrieves info from the [FGO Atlas Academy API](https://api.atlasacademy.io/docs#/) and [FGO Fandom](https://fategrandorder.fandom.com/wiki/Fate/Grand_Order_Wikia#English_Server)

Available commands: 

* $servant [servant name]
  * Returns information pertaining to the specified servant
  
    ![Image of example command](https://i.gyazo.com/3460078bdbf4ac43d8a8739c0f748da8.png)
    
* $asc [servant name] [ascension stage]
  *  Returns the art for the specified servant ascension level
  
     ![Image of example command](https://i.gyazo.com/17a579c1023328c08e7ae3ad254d8a77.png)
     
* $spr [servant name] [sprite stage]
  *  Returns the image for the specified servant sprite level
  
     ![Image of example command](https://i.gyazo.com/17a579c1023328c08e7ae3ad254d8a77.png)
     
Future functions:
1. Calculate material cost depending on provided character/skill level
2. Retrieve in-game sprites (COMPLETE)
3. Retrieve April Fools art (similar to $asc command)
4. Might expand to include other gacha games once Fate related work is complete
5. Get new example images
