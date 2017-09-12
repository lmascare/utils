# Twitter

Accessing twitter feeds using Python
 
### Create a virtualenv
 * virtualenv twitter
 * source twitter/bin/activate
 * pip install twitter
 
### Important Twitter URLs
 * https://dev.twitter.com/rest/reference/get/trends/place  
    Returns top 50 trends for a specific WOEID (WOEID --> Where On Earth ID)
 * https://developer.yahoo.com/geo/geoplanet/ (Yahoo's Where-On-Earth ID)
 * http://apps.twitter.com  
    Setup your application
 * 
    
### Configure credentials
 * Setup application at http://apps.twitter.com eg Mining_Larry_Masc
 * Create the CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN & ACCESS_TOKEN_SECRET tokens
 * Update the tweet.py with these values
 * You need the WOEID. Register with Yahoo https://developer.yahoo.com/geo/geoplanet/
    * Get Client ID and Client Secret
  
    