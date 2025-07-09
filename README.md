
# TripSync - Smart Travel Assistant

TripSync is a smart travel assistant web app that generates and optimizes personalized travel itineraries using real-time data from the Gemini API. Users can create custom itineraries, access detailed destination information, and export their plans as PDF files.

## Features
- **Personalized Itineraries**: Generate optimized travel plans based on user preferences.
- **Real-Time Data**: Fetch live destination details using the Gemini API.
- **Customizable Plans**: Modify generated itineraries to suit your needs.
- **PDF Export**: Download and share your itinerary in a structured PDF format.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Database**: ConvexDB
- **APIs**: Google Generative AI SDK (Gemini API)
- **PDF Generation**: jsPDF

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Node.js (for frontend dependencies, if any)
- Pip (Python package manager)
- Virtual environment (`venv`)

### Clone the Repository
```sh
git clone https://github.com/meera0709/tripsync.git
cd tripsync
```

### Backend Setup (Flask)
1. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables (create a `.env` file and add API keys):
   ```sh
   GEMINI_API_KEY=your_gemini_api_key
   SECRET_KEY=your_secret_key
   ```
4. Run the Flask server:
   ```sh
   python app.py
   ```

### Frontend Setup
1. Navigate to the frontend directory (if applicable):
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend server:
   ```sh
   npm start
   ```

### Access the Application
Once both frontend and backend servers are running, open the app in your browser:
```
http://localhost:3000  # If using React frontend
http://localhost:5000  # If running Flask only
```

## Usage
1. **Sign Up/Login**: Create an account or log in.
2. **Enter Preferences**: Input your travel preferences and constraints.
3. **Generate Itinerary**: Get AI-powered recommendations.
4. **Modify & Optimize**: Adjust the plan as needed.
5. **Export PDF**: Save and share your itinerary.

## Deployment
For production deployment, consider using:
- **AWS (EC2, S3, RDS)**
- **Vercel (for frontend)**
- **Render/Heroku (for backend)**

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature X'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License
MIT License. See `LICENSE` for details.

