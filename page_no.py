import json

# Function to load JSON data from a file
def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Function to find pages a user might like based on common interests
def find_pages_you_might_like(user_id, data):
    user_pages = {}
    
    # Dictionary to store user interactions with pages
    for user in data["users"]:
        user_pages[user["id"]] = set(user["liked_pages"])
        
    # If the user is not found, return an empty list
    if user_id not in user_pages:
        return []
        
    user_liked_pages = user_pages[user_id]
    page_suggestions = {}
    
    # Compare with all other users to find similar interests
    for other_user, pages in user_pages.items():
        if other_user != user_id:
            # Find the intersection (common pages liked by both)
            shared_pages = user_liked_pages.intersection(pages)
            
            # If they share common interests, suggest other pages liked by this user
            if shared_pages:
                for page in pages:
                    if page not in user_liked_pages:
                        # Weight the suggestion by the number of common pages shared
                        page_suggestions[page] = page_suggestions.get(page, 0) + len(shared_pages)
                        
    # Sort recommended pages based on the highest total weight of shared interactions
    sorted_pages = sorted(page_suggestions.items(), key=lambda x: x[1], reverse=True)
    
    # Return only the page IDs of the recommended pages
    return [page_id for page_id, _ in sorted_pages]

# Load data (using the cleaned data file from your second task)
data = load_data("cleaned_data.json")

# Example: Finding recommendations for Amit (user_id = 1)
user_id = 1
page_recommendations = find_pages_you_might_like(user_id, data)

print(f"Pages You Might Like for User {user_id}: {page_recommendations}")