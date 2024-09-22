from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask import render_template, jsonify
import json
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content  # Import content for Schema

app = Flask(__name__)
app.secret_key = 'sample'  # Replace with your actual secret key

location = ''
style = ''
activities = ''
budget = ''
duration = ''
accommodation = ''
transport = ''
group_tours = ''
cuisine = ''

# Configure Google Generative AI API
genai.configure(api_key="your_api_key")  # Update with environment variable

# Update generation_config with response_schema
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'password':
        return redirect(url_for('index1'))
    else:
        flash('Invalid username or password.')
        return redirect(url_for('home'))

@app.route('/index1')
def index1():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def index():
    return redirect(url_for('preferences'))

@app.route('/preferences')
def preferences():
    return render_template('preferences.html')

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if request.method == 'POST':
        # Capture user preferences from the form
        global location, style, activities, budget, duration, accommodation, transport, group_tours, cuisine
        location = request.form.getlist('location')
        style = request.form.getlist('style')
        activities = request.form.getlist('activities')
        budget = request.form.get('budget')
        duration = request.form.get('duration')
        accommodation = request.form.get('accommodation')
        transport = request.form.get('transport')
        group_tours = request.form.get('group-tours')
        cuisine = request.form.get('cuisine')

        # Render confirm.html with the user preferences
        return render_template('confirm.html', 
                               location=', '.join(location),
                               style=', '.join(style),
                               activities=', '.join(activities),
                               budget=budget,
                               duration=duration,
                               accommodation=accommodation,
                               transport=transport,
                               group_tours=group_tours,
                               cuisine=cuisine)
    
@app.route('/itinerary', methods=['POST', 'GET'])
def itinerary():
    if request.method == 'POST':
        # Get selected destinations/events from the form
        selected_items = request.form.getlist('selected_items')
        
        # Prompt for optimized itinerary using the Gemini API
        prompt = f"""
        Generate an optimized itinerary for the selected destinations/events: {', '.join(selected_items)}. Provide the details in JSON format with the following fields: 'destination/event', 'timings', 'date', 'weather', 'traffic', and 'order of visit'.
        """

        # Generate optimized itinerary using the model with updated prompts
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config
        )

        response = model.generate_content([
            f"input: Generate an optimized itinerary for the selected destinations/events: {', '.join(selected_items)}. Provide the details in JSON format with the following fields: 'destination/event', 'timings', 'date', 'weather', 'traffic', and 'order of visit'.",
            "output: Provide a JSON array of objects with 'destination/event', 'timings', 'date', 'weather', 'traffic', and 'order of visit' fields."
        ])

        generated_content = response.text

        try:
            itinerary_dict = json.loads(generated_content)
        except json.JSONDecodeError:
            itinerary_dict = {}

        # Render the itinerary.html with the optimized itinerary data
        return render_template('itinerary.html', itinerary_dict=itinerary_dict)
    else:
        return redirect(url_for('dashboard'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    input_text = f"""
    What is your location? What is your preferred travel style? What are your preferred activities? What is the budget range? What is your preferred travel duration for the trip? What is your preferred accommodation type? What is your transportation preference? Are you open to group tours? Are you interested in exploring local cuisine? 
    
    Location: {location}
    Preferred Travel Style: {style}
    Preferred Activities: {activities}
    Budget Range: {budget}
    Preferred Travel Duration: {duration}
    Preferred Accommodation Type: {accommodation}
    Transportation Preference: {transport}
    Group Tours: {group_tours}
    Local Cuisine Exploration: {cuisine}
    """

    # Generate recommendations using the model with updated prompts
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )

    response = model.generate_content([
        "input: What is your location? What is your preferred travel style? What are your preferred activities? What is the budget range? What is your preferred travel duration for the trip? What is your preferred accommodation type? What is your transportation preference? Are you open to group tours? Are you interested in exploring local cuisine? ",
        "output: Provide a set of destinations and current real-time events happening in India according to the user preferences. Format the response as a JSON array of objects. Each object should contain 'destination/event' and 'description' fields. For example: [{\"destination/event\": \"Chennai\", \"description\": \"A vibrant coastal city with a rich history and culture.\"}, {\"destination/event\": \"Mahabalipuram Shore Temple Festival\", \"description\": \"Annual festival celebrating the iconic Shore Temple.\"}]",
        f"input: Location: {location}, Travel Style: {style}, Activities: {activities}, Budget: {budget}, Duration: {duration}, Accommodation: {accommodation}, Transport: {transport}, Group Tours: {group_tours}, Local Cuisine: {cuisine}",
        "output: Provide a JSON array of objects with 'destination/event' and 'description' fields based on the user's preferences. For example: [{\"destination/event\": \"Chennai\", \"description\": \"A vibrant coastal city with a rich history and culture.\"}, {\"destination/event\": \"Mahabalipuram Shore Temple Festival\", \"description\": \"Annual festival celebrating the iconic Shore Temple.\"}]"
    ])

    generated_content = response.text

    try:
        content_dict = json.loads(generated_content)
    except json.JSONDecodeError:
        content_dict = {}

    return render_template('dashboard.html', content_dict=content_dict)

if __name__ == '__main__':
    app.run(port=8080)
