# turbit

# Step One - Run the docker
docker compose up --build -d

# Step Two - Run the main application
uvicorn main:app --reload

# Step Three - if you want to shut down docker
docker compose down
