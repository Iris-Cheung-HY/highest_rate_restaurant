def get_highest_rated(restaurants):
    highest_rate_restaurants = {}
    highest_rating = 0

    if restaurants == []:
        return None

    for restaurant in restaurants:
            
        restaurant_name = restaurant["name"]
        restaurant_rating = restaurant["rating"]
        
    
        if restaurant_rating > highest_rating:
            highest_rating = restaurant_rating
            highest_rate_restaurants["name"] = restaurant_name
            highest_rate_restaurants["rating"]= highest_rating
 
    return highest_rate_restaurants


# Another Solution

# def get_highest_rated(restaurants):
#     if not restaurants:
#         return None

#     highest_rated = restaurants[0]
#     for restaurant in restaurants:
#         if restaurant["rating"] > highest_rated["rating"]:
#             highest_rated = restaurant

#     return highest_rated


