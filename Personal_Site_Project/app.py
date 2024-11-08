from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="dist", static_url_path="/")
CORS(
    app,
    resources={
        r"/api/*": {
            "origins": ["http://localhost:5173", "http://127.0.0.1:5173"],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type"],
        }
    },
)

# Sample project data - in a real app, this would come from a database
PROJECTS = [
    {
        "id": 1,
        "title": "Full-Stack Web Application",
        "description": "Modern web application built with React and Node.js, featuring real-time updates and responsive design",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "link": "https://github.com/da13oss",
        "technologies": ["React", "Node.js", "MongoDB", "WebSocket"],
    },
    {
        "id": 2,
        "title": "Data Analysis Pipeline",
        "description": "Python-based data processing pipeline for large-scale data analysis and visualization",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
        "link": "https://github.com/da13oss",
        "technologies": ["Python", "pandas", "scikit-learn", "Matplotlib"],
    },
    {
        "id": 3,
        "title": "API Gateway Service",
        "description": "Scalable API gateway service handling authentication, rate limiting, and request routing",
        "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=80",
        "link": "https://github.com/da13oss",
        "technologies": ["Express.js", "Redis", "JWT", "Docker"],
    },
]


@app.route("/")
def root():
    return jsonify(
        {
            "message": "Welcome to DA13OSS Portfolio API",
            "version": "1.0.0",
            "endpoints": {
                "projects": "/api/projects",
                "contact": "/api/contact",
                "health": "/api/health",
            },
        }
    )


@app.route("/api/projects", methods=["GET"])
def get_projects():
    response = make_response(jsonify(PROJECTS))
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/api/contact", methods=["POST"])
def contact():
    if not request.is_json:
        return make_response(
            jsonify({"error": "Content-Type must be application/json"}), 400
        )

    data = request.json
    if not data:
        return make_response(jsonify({"error": "No data provided"}), 400)

    # Here you would typically implement email sending logic
    return jsonify({"message": "Message received successfully", "data": data}), 200


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "version": "1.0.0"})


@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify(
            {"error": "Not found", "message": "The requested resource does not exist"}
        ),
        404,
    )


@app.errorhandler(500)
def internal_error(error):
    return make_response(
        jsonify(
            {
                "error": "Internal server error",
                "message": "Something went wrong on our end",
            }
        ),
        500,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
