import json

def clean_data(data):
    # Remove users with missing names
    data["users"] = [user for user in data["users"] if user["name"].strip()]
    
    # Remove duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))
        
    # Remove inactive users (who have no friends AND no liked pages)
    data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]
    
    # Remove duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]] = page
    data["pages"] = list(unique_pages.values())
    
    return data

# Load, clean, and display the cleaned data
# Changed "codebook_data.json" to "data.json" to match your actual file
with open("data.json", "r") as file:
    data = json.load(file)

cleaned_data = clean_data(data)

# Save the cleaned data into a new file
with open("cleaned_data.json", "w") as file:
    json.dump(cleaned_data, file, indent=4)

print("Data cleaned successfully!")