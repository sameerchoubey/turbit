# turbit

# Steps to run this.
1. Install Docker.
2. Install dependencies from requirements.txt
3. Run docker with this command in sleep mode - docker compose up --build -d
4. Load data by running the load_data.py
5. Run the main.py file using uvicorn main:app --reload

# Step Two - Run the main application
uvicorn main:app --reload

# Step Three - if you want to shut down docker
docker compose down
