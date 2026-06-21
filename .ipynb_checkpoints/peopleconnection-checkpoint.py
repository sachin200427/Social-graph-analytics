import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

def find_people_you_may_know(user_id, data):
    user_friends = {}
    
    # Map each user to a set of their friends' IDs
    for user in data["users"]:
        user_friends[user["id"]] = set(user["friends"])
        
    # If the user doesn't exist in the data, return empty suggestions
    if user_id not in user_friends:
        return []
        
    direct_friends = user_friends[user_id]
    suggestions = {}
    
    # Iterate through all direct friends to find friends-of-friends (mutuals)
    for friend in direct_friends:
        if friend in user_friends:
            for mutual in user_friends[friend]:
                # Exclude themselves and people they are already direct friends with
                if mutual != user_id and mutual not in direct_friends:
                    # Count mutual connections
                    suggestions[mutual] = suggestions.get(mutual, 0) + 1
                    
    # Sort recommendations by the highest number of mutual friends
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    
    # Return only the user IDs of the recommended people
    return [u_id for u_id, count in sorted_suggestions]

# Load the cleaned data from your previous step
data = load_data("cleaned_data.json")

# Find suggestions for Amit (user_id = 1)
user_id = 1
recommendations = find_people_you_may_know(user_id, data)

print(f"People You May Know for User {user_id}: {recommendations}")