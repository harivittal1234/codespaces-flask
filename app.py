from flask import Flask
from datetime import datetime
import os
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Fetch the required details
    name = "Hari Vittal Appinedi"  # Replace with your full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    top_output = subprocess.check_output("top -b -n 1 | head -n 20", shell=True).decode()

    # Generate HTML response
    response = f"""
    <html>
    <body>
        
        <p><strong>Name:</strong> {name}</p>
        <p><strong>User:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre><strong>TOP output:</strong>\n\n{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == "__main__":
    # Run the Flask application on all interfaces
    app.run(host="0.0.0.0", port=8080)