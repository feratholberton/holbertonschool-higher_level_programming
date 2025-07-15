# Get Image to use
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /python-server_side_rendering

# Install Flask
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project tasks code
COPY . ./

CMD ["flask", "run", "--host=0.0.0.0"]
