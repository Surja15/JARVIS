import google.generativeai as genai

# Configure the API key
genai.configure(api_key="YOUR_API_KEY")

# Create the model
model = genai.GenerativeModel("gemini-pro")

# Generate the response
response = model.generate_content([
    {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
    {"role": "user", "content": "What is coding?"}
])

# Print the result
print(response.text)