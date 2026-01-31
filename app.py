from flask import Flask, render_template, redirect

app = Flask(__name__)
from flask import request


# =========================
# SKILLS SECTION DATA (6)
# =========================

SKILLS = {
    "python": {
        "roadmap": [
            "Python basics & syntax",
            "Control statements",
            "Functions & modules",
            "OOP concepts",
            "Libraries (NumPy, Pandas)",
            "Projects & GitHub"
        ],
        "resources": [
            ("Official Python Docs", "https://docs.python.org/3/"),
            ("W3Schools Python", "https://www.w3schools.com/python/"),
            ("FreeCodeCamp Full Course", "https://www.youtube.com/watch?v=rfscVS0vtbw"),
            ("Telusko Python Playlist", "https://www.youtube.com/@Telusko"),
            ("HackerRank Python Practice", "https://www.hackerrank.com/domains/python"),
            ("CodeChef Python Practice", "https://www.codechef.com/practice/python"),
            ("GeeksforGeeks Python Practice", "https://practice.geeksforgeeks.org/explore/?category[]=Python")
        ]
    },

    "java": {
        "roadmap": [
            "Java Basics",
            "OOP in Java",
            "Arrays & Strings",
            "Collections Framework",
            "JDBC",
            "Mini Projects"
        ],
        "resources": [
            ("Official Java Docs", "https://docs.oracle.com/javase/tutorial/"),
            ("W3Schools Java", "https://www.w3schools.com/java/"),
            ("FreeCodeCamp Java", "https://www.youtube.com/watch?v=GoXwIVyNvX0"),
            ("Telusko Java", "https://www.youtube.com/@Telusko"),
            ("HackerRank Java", "https://www.hackerrank.com/domains/java")
        ]
    },

    "web": {
        "roadmap": [
            "HTML Basics",
            "CSS Styling",
            "JavaScript Basics",
            "Responsive Design",
            "Backend Basics",
            "Deploy Website"
        ],
        "resources": [
            ("MDN Web Docs", "https://developer.mozilla.org/"),
            ("W3Schools Web", "https://www.w3schools.com/"),
            ("FreeCodeCamp Web", "https://www.youtube.com/watch?v=G3e-cpL7ofc"),
            ("Traversy Media", "https://www.youtube.com/@TraversyMedia"),
            ("Frontend Mentor", "https://www.frontendmentor.io/")
        ]
    },

    "ai": {
        "roadmap": [
            "Python for AI",
            "Math Basics",
            "Machine Learning",
            "ML Algorithms",
            "Model Training",
            "AI Mini Projects"
        ],
        "resources": [
            ("Google ML Crash Course", "https://developers.google.com/machine-learning/crash-course"),
            ("FreeCodeCamp ML", "https://www.youtube.com/watch?v=NWONeJKn6kc"),
            ("StatQuest", "https://www.youtube.com/@statquest"),
            ("Kaggle Learn", "https://www.kaggle.com/learn"),
            ("Scikit-learn Docs", "https://scikit-learn.org/stable/")
        ]
    },

    "datascience": {
        "roadmap": [
            "Python Basics",
            "Statistics",
            "NumPy & Pandas",
            "Data Visualization",
            "Machine Learning",
            "Data Projects"
        ],
        "resources": [
            ("Kaggle Learn", "https://www.kaggle.com/learn"),
            ("FreeCodeCamp DS", "https://www.youtube.com/watch?v=ua-CiDNNj30"),
            ("StatQuest", "https://www.youtube.com/@statquest"),
            ("GeeksforGeeks DS", "https://www.geeksforgeeks.org/data-science/"),
            ("Analytics Vidhya", "https://www.analyticsvidhya.com/")
        ]
    },

    "sql": {
        "roadmap": [
            "Database Basics",
            "SQL Syntax",
            "CRUD Operations",
            "Joins & Subqueries",
            "Indexes",
            "Real-world Queries"
        ],
        "resources": [
            ("W3Schools SQL", "https://www.w3schools.com/sql/"),
            ("SQLZoo", "https://sqlzoo.net/"),
            ("FreeCodeCamp SQL", "https://www.youtube.com/watch?v=HXV3zeQKqGY"),
            ("Mode SQL", "https://mode.com/sql-tutorial/"),
            ("HackerRank SQL", "https://www.hackerrank.com/domains/sql")
        ]
    }
}

# =========================
# PROJECTS DATA
# =========================

PROJECTS = [
    {"id": "ai_resume", "title": "AI Resume Analyzer"},
    {"id": "face_attendance", "title": "Smart Attendance System using Face Recognition"},
    {"id": "online_exam", "title": "Online Examination System"},
    {"id": "student_prediction", "title": "Student Performance Prediction System"},
    {"id": "internship_reco", "title": "Internship Recommendation Platform"},
    {"id": "helpdesk_chatbot", "title": "Campus Helpdesk Chatbot"},
    {"id": "expense_tracker", "title": "Smart Expense Tracker"},
    {"id": "weather_app", "title": "Weather Forecast Web App"},
    {"id": "online_voting", "title": "Online Voting System"},
    {"id": "library_mgmt", "title": "Library Management System"},
    {"id": "job_portal", "title": "Job Portal Website"},
    {"id": "skill_reco", "title": "Skill Recommendation System"},
    {"id": "chat_app", "title": "Real-Time Chat Application"},
    {"id": "elearning", "title": "E-Learning Platform"},
    {"id": "blood_donation", "title": "Blood Donation Management System"},
    {"id": "event_mgmt", "title": "College Event Management System"},
    {"id": "fake_news", "title": "Fake News Detection System"},
    {"id": "food_order", "title": "Online Food Ordering System"},
    {"id": "portfolio_builder", "title": "Personal Portfolio Builder"},
    {"id": "traffic_sign", "title": "Traffic Sign Recognition System"}
]

# =========================
# BASIC ROUTES
# =========================

@app.route("/")
def opening():
    return render_template("opening.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # later you can add real username/password check
        return redirect("/dashboard")

    # GET request → show login page
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect("/dashboard")

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# =========================
# SKILLS ROUTES
# =========================

@app.route("/skills")
def skills():
    return render_template("skills.html", skills=SKILLS.keys())

@app.route("/skills/<skill>")
def skill_detail(skill):
    return render_template(
        "skill_detail.html",
        skill=skill.capitalize(),
        data=SKILLS.get(skill)
    )

@app.route("/skills/<skill>/roadmap")
def skill_roadmap(skill):
    return render_template(
        "skill_roadmap.html",
        skill=skill.capitalize(),
        roadmap=SKILLS.get(skill)["roadmap"]
    )

@app.route("/skills/<skill>/resources")
def skill_resources(skill):
    return render_template(
        "skill_resources.html",
        skill=skill.capitalize(),
        resources=SKILLS.get(skill)["resources"]
    )

@app.route("/skills/<skill>/quiz")
def skill_quiz(skill):
    return render_template("skill_quiz.html", skill=skill)

# =========================
# PROJECTS ROUTE (ONLY ONE)
# =========================

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/projects/<project_id>")
def project_overview(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    return render_template("project_overview.html", project=project)


@app.route("/projects/<project_id>/create")
def choose_language(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    return render_template("choose_language.html", project=project)


@app.route("/projects/<project_id>/<language>")
def project_details(project_id, language):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    return render_template(
        "project_build.html",
        project=project,
        language=language.capitalize()
    )
@app.route("/projects/<project_id>/<language>/build")
def build_project(project_id, language):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)

    return render_template(
        "project_build.html",
        project=project,
        language=language.capitalize()
    )

@app.route("/ai-mentor", methods=["GET", "POST"])
def ai_mentor():
    response = ""

    if request.method == "POST":
        user_input = request.form.get("question", "").lower()

        # EMOTIONAL SUPPORT
        if any(word in user_input for word in ["sad", "demotivated", "tired", "lost", "failure"]):
            response = (
                "I know it feels heavy right now 💙 "
                "Remember, every successful person once felt exactly like this. "
                "Take a small break, breathe, and start again. You can do this."
            )

        # PARENTS / FAMILY
        elif any(word in user_input for word in ["parents", "father", "mother", "family"]):
            response = (
                "Your parents’ sacrifices are real and powerful ❤️ "
                "Even small efforts you make today can make them proud tomorrow. "
                "Keep going for them — and for yourself."
            )

        # PYTHON
        elif "python" in user_input:
            response = (
                "Start with Python basics → practice daily → build small projects. "
                "Good beginner projects are Calculator, To-Do App, Expense Tracker."
            )

        # JAVA
        elif "java" in user_input:
            response = (
                "Learn Java basics → OOP → Collections → JDBC. "
                "Try building Student Management or Library Management systems."
            )

        # WEB DEVELOPMENT
        elif "web" in user_input:
            response = (
                "Learn HTML → CSS → JavaScript → build responsive websites. "
                "Then learn Flask or Django for backend."
            )

        # AI / ML
        elif any(word in user_input for word in ["ai", "ml", "machine learning"]):
            response = (
                "Start with Python, then learn ML basics like regression and classification. "
                "Practice on Kaggle and build mini AI projects."
            )

        # CAREER CONFUSION
        elif any(word in user_input for word in ["career", "future", "confused"]):
            response = (
                "Feeling confused is part of growth 🌱 "
                "Explore one skill deeply for 30 days. "
                "Clarity comes from action, not overthinking."
            )
                # EXAMS / PRESSURE
        elif any(word in user_input for word in ["exam", "tests", "pressure", "marks"]):
            response = (
                "Exams can be stressful, but remember — marks don’t define your worth 📘 "
                "Study smart, revise daily, and focus on understanding, not memorizing. "
                "You are capable of more than you think."
            )

        # BACKLOGS
        elif any(word in user_input for word in ["backlog", "failed", "arrear"]):
            response = (
                "Backlogs are not the end — many successful people had them 💪 "
                "Clear one subject at a time. Make a small plan and stick to it. "
                "Consistency beats panic."
            )

        # INTERNSHIPS
        elif "internship" in user_input:
            response = (
                "Start with small internships or virtual internships 🌟 "
                "Focus on skills, not stipend first. "
                "Platforms like Internshala, LinkedIn, and government portals help."
            )

        # HACKATHONS
        elif "hackathon" in user_input:
            response = (
                "Hackathons are about learning, not winning 🚀 "
                "Join with a simple idea, learn teamwork, and build something basic. "
                "Participation itself boosts confidence and resumes."
            )

        # CONFIDENCE ISSUES
        elif any(word in user_input for word in ["confidence", "fear", "scared", "nervous"]):
            response = (
                "Low confidence means you care — and that’s good 💙 "
                "Skill + practice = confidence. "
                "Start small, fail safely, and grow steadily."
            )

        # CODING FEAR
        elif any(word in user_input for word in ["coding is hard", "cant code", "not good at coding"]):
            response = (
                "Coding feels hard for everyone at first 👨‍💻👩‍💻 "
                "Confusion means your brain is learning. "
                "Practice daily for 30 minutes — that’s enough to grow."
            )

        # PLACEMENTS / JOB
        elif any(word in user_input for word in ["placement", "job", "interview"]):
            response = (
                "Placements reward preparation, not perfection 🎯 "
                "Work on one language, basic DSA, and communication. "
                "Confidence and clarity matter more than knowing everything."
            )

        # DAILY ROUTINE
        elif any(word in user_input for word in ["routine", "daily plan", "schedule"]):
            response = (
                "A simple routine works best 🕒 "
                "Study 2–3 focused hours, practice one skill daily, and rest well. "
                "Balance creates long-term success."
            )

        # NIGHT DEMOTIVATION
        elif any(word in user_input for word in ["night", "alone", "overthinking"]):
            response = (
                "Night thoughts hit harder, but they aren’t permanent 🌙 "
                "You survived 100% of your worst days. "
                "Sleep well — tomorrow is a new chance."
            )


        # DEFAULT
        else:
            response = (
                "Tell me how you're feeling or what you want to learn 😊 "
                "I can help with motivation, career guidance, Python, Java, Web, or AI."
            )
            
        

    return render_template("ai_mentor.html", response=response)

@app.route('/motivation')
def motivation():
    return render_template('motivation.html')

@app.route("/hackathons")
def hackathons():
    return render_template("hackathons.html")


@app.route("/hackathons/best")
def best_hackathons():
    return render_template("best_hackathons.html")


@app.route("/hackathons/beginner")
def beginner_hackathons():
    return render_template("beginner_hackathons.html")


@app.route("/hackathons/ongoing")
def ongoing_hackathons():
    return render_template("ongoing_hackathons.html")
@app.route("/hackathon/<idea_slug>")
def hackathon_idea(idea_slug):

    ideas = {
        "ai-career-guidance": {
            "title": "AI Career Guidance System",
            "description": "Helps students choose the right career using AI-based recommendations.",
            "importance": "Very useful in hackathons because it solves a real student problem using AI.",
            "tech": ["Python", "Flask", "Machine Learning"],
            "steps": [
                "Collect career dataset",
                "Build ML model for recommendations",
                "Create Flask web app",
                "Show career results"
            ],
            "resources": [
                ("GitHub Sample Project", "https://github.com/topics/career-guidance"),
                ("ML Roadmap", "https://roadmap.sh/ai-data-scientist"),
                ("Flask Docs", "https://flask.palletsprojects.com/")
            ]
        },

        "internship-recommender": {
            "title": "Smart Internship Recommender",
            "description": "Suggests internships based on skills and interests.",
            "importance": "Judges like recommendation systems with real-world value.",
            "tech": ["Python", "ML", "Web"],
            "steps": [
                "Collect internship data",
                "Build recommendation logic",
                "Create UI",
                "Display results"
            ],
            "resources": [
                ("GitHub Projects", "https://github.com/topics/recommendation-system"),
                ("ML Basics", "https://scikit-learn.org/stable/")
            ]
        },
    "mental-health": {
    "title": "Student Mental Health App",
    "description": "Daily mood tracking and motivation support.",
    "importance": "Mental health projects show strong social impact and are highly valued in hackathons.",
    "tech": ["Web", "UI", "Flask"],
    "steps": [
        "Design mood input interface",
        "Store daily mood logs",
        "Show motivational messages and tips"
    ],
    "resources": [
        ("Flask Documentation", "https://flask.palletsprojects.com/"),
        ("UI Inspiration", "https://dribbble.com/")
    ]
},

"campus-chatbot": {
    "title": "Campus Helpdesk Chatbot",
    "description": "AI chatbot for answering college-related queries.",
    "importance": "Chatbots reduce workload and improve student experience.",
    "tech": ["AI", "NLP", "Python"],
    "steps": [
        "Collect common student questions",
        "Train chatbot using NLP",
        "Integrate chatbot into website"
    ],
    "resources": [
        ("NLTK", "https://www.nltk.org/"),
        ("Chatbot Guide", "https://realpython.com/")
    ]
},

"attendance-system": {
    "title": "Smart Attendance System",
    "description": "Automates attendance using face recognition.",
    "importance": "Automation and AI-based projects score high in hackathons.",
    "tech": ["AI", "OpenCV", "Python"],
    "steps": [
        "Capture student images",
        "Train face recognition model",
        "Mark attendance automatically"
    ],
    "resources": [
        ("OpenCV Docs", "https://opencv.org/"),
        ("Face Recognition", "https://github.com/ageitgey/face_recognition")
    ]
},
     "fake-news": {
    "title": "Fake News Detection",
    "description": "Detects fake news using machine learning.",
    "importance": "Fake news detection is a real-world AI problem and judges love NLP-based solutions.",
    "tech": ["ML", "Python", "NLP"],
    "steps": [
        "Collect real and fake news datasets",
        "Train ML model using text classification",
        "Build a web interface to test news"
    ],
    "resources": [
        ("Kaggle Dataset", "https://www.kaggle.com/c/fake-news"),
        ("Scikit-learn", "https://scikit-learn.org/")
    ]
},

"expense-tracker": {
    "title": "Expense Tracker",
    "description": "Tracks and analyzes student expenses.",
    "importance": "Shows practical problem-solving and clean UI skills.",
    "tech": ["Web", "Python", "Flask"],
    "steps": [
        "Create expense input form",
        "Store expenses in database",
        "Show charts and monthly summaries"
    ],
    "resources": [
        ("Flask Tutorial", "https://flask.palletsprojects.com/"),
        ("Chart.js", "https://www.chartjs.org/")
    ]
},

"skill-recommendation": {
    "title": "Skill Recommendation Platform",
    "description": "Suggests skills based on career goals.",
    "importance": "AI recommendation systems are very attractive in hackathons.",
    "tech": ["AI", "Web", "Python"],
    "steps": [
        "Collect career goals from users",
        "Map goals to required skills",
        "Recommend learning paths"
    ],
    "resources": [
        ("Recommendation Systems", "https://realpython.com/"),
        ("Flask", "https://flask.palletsprojects.com/")
    ]
},

"online-exam": {
    "title": "Online Exam System",
    "description": "Secure online examination platform.",
    "importance": "Shows system design, security, and backend skills.",
    "tech": ["Web", "Flask", "Database"],
    "steps": [
        "Create login system",
        "Add exam and question modules",
        "Evaluate answers automatically"
    ],
    "resources": [
        ("Flask Login", "https://flask-login.readthedocs.io/"),
        ("SQLite", "https://www.sqlite.org/")
    ]
},

"blood-donation": {
    "title": "Blood Donation App",
    "description": "Connects donors with patients in need.",
    "importance": "Social impact projects score very high in hackathons.",
    "tech": ["Web", "Python", "Flask"],
    "steps": [
        "Register donors and patients",
        "Match blood groups and location",
        "Notify nearby donors"
    ],
    "resources": [
        ("Flask Docs", "https://flask.palletsprojects.com/"),
        ("Google Maps API", "https://developers.google.com/maps")
    ]
},
     # =========================
        # BEGINNER FRIENDLY IDEAS (NEW)
        # =========================

        "todo-app": {
            "title": "To-Do List App",
            "description": "A simple app to manage daily tasks.",
            "importance": "Very beginner friendly and great for first hackathon.",
            "tech": ["HTML", "CSS", "Python", "Flask"],
            "steps": [
                "Create task input form",
                "Display task list",
                "Add delete option"
            ],
            "resources": [
                ("Flask Tutorial", "https://flask.palletsprojects.com/"),
                ("HTML Basics", "https://www.w3schools.com/html/")
            ]
        },

        "weather-app": {
            "title": "Weather App",
            "description": "Shows real-time weather using API.",
            "importance": "API usage impresses judges even for beginners.",
            "tech": ["Python", "API", "Flask"],
            "steps": [
                "Get weather API key",
                "Fetch weather data",
                "Display temperature"
            ],
            "resources": [
                ("OpenWeather API", "https://openweathermap.org/api"),
                ("Flask API Guide", "https://flask.palletsprojects.com/")
            ]
        },

        "calculator": {
            "title": "Calculator",
            "description": "Performs basic arithmetic operations.",
            "importance": "Best project to understand logic and UI.",
            "tech": ["HTML", "CSS", "Python"],
            "steps": [
                "Design calculator UI",
                "Add operation logic",
                "Show results"
            ],
            "resources": [
                ("Python Basics", "https://www.w3schools.com/python/")
            ]
        },

        "quiz-app": {
            "title": "Quiz App",
            "description": "MCQ quiz with score calculation.",
            "importance": "Shows logic building and user interaction.",
            "tech": ["Python", "Flask"],
            "steps": [
                "Create questions",
                "Accept answers",
                "Calculate score"
            ],
            "resources": [
                ("Flask Forms", "https://flask.palletsprojects.com/")
            ]
        },

        "digital-clock": {
            "title": "Digital Clock",
            "description": "Displays real-time digital clock.",
            "importance": "Simple but effective UI project.",
            "tech": ["HTML", "JavaScript"],
            "steps": [
                "Get current time",
                "Update time every second",
                "Display in UI"
            ],
            "resources": [
                ("JavaScript Date", "https://www.w3schools.com/js/")
            ]
        },

        "expense-tracker": {
            "title": "Expense Tracker",
            "description": "Tracks daily expenses.",
            "importance": "Real-life student problem.",
            "tech": ["Python", "Flask", "Database"],
            "steps": [
                "Create expense form",
                "Store data",
                "Show summary"
            ],
            "resources": [
                ("SQLite", "https://www.sqlite.org/"),
                ("Flask DB", "https://flask.palletsprojects.com/")
            ]
        },

        "notes-app": {
            "title": "Notes App",
            "description": "Create and manage notes.",
            "importance": "CRUD project – very important for beginners.",
            "tech": ["Python", "Flask"],
            "steps": [
                "Add notes",
                "Edit notes",
                "Delete notes"
            ],
            "resources": [
                ("CRUD Flask", "https://realpython.com/")
            ]
        },

        "password-generator": {
            "title": "Password Generator",
            "description": "Generates secure passwords.",
            "importance": "Security-based simple project.",
            "tech": ["Python"],
            "steps": [
                "Take length input",
                "Generate password",
                "Display output"
            ],
            "resources": [
                ("Python Random", "https://docs.python.org/3/library/random.html")
            ]
        },

        "stopwatch": {
            "title": "Stopwatch App",
            "description": "Start, stop and reset timer.",
            "importance": "Good JS logic practice.",
            "tech": ["HTML", "JavaScript"],
            "steps": [
                "Start timer",
                "Stop timer",
                "Reset timer"
            ],
            "resources": [
                ("JS Timer", "https://www.w3schools.com/js/")
            ]
        },

        "portfolio": {
            "title": "Portfolio Website",
            "description": "Personal website to showcase skills.",
            "importance": "Very useful for placements.",
            "tech": ["HTML", "CSS"],
            "steps": [
                "Create sections",
                "Add projects",
                "Deploy website"
            ],
            "resources": [
                ("Portfolio Guide", "https://www.freecodecamp.org/")
            ]
        }
    }

    idea = ideas.get(idea_slug)

    if not idea:
        return "Idea not found", 404

    return render_template("hackathon_idea.html", idea=idea)










# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)
