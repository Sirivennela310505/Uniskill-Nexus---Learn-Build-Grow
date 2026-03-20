from flask import Flask, render_template, redirect
from flask import request
from datetime import date

app = Flask(__name__)


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
            ("Corey Schafer Python", "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"),
            ("CS Dojo Python", "https://www.youtube.com/playlist?list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg"),
            ("HackerRank Python Practice", "https://www.hackerrank.com/domains/python"),
            ("CodeChef Python Practice", "https://www.codechef.com/practice/python"),
            ("GeeksforGeeks Python Practice", "https://practice.geeksforgeeks.org/explore/?category[]=Python"),
            ("LeetCode Python Problems", "https://leetcode.com/problemset/?topicSlugs=array&languageTags=python3"),
            ("Python Projects GitHub", "https://github.com/topics/python-projects"),
            ("Real Python Tutorials", "https://realpython.com/"),
            ("Kaggle Python Course", "https://www.kaggle.com/learn/python"),
            ("Programiz Python", "https://www.programiz.com/python-programming")
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
            ("Apna College Java", "https://www.youtube.com/watch?v=rZ41y93P2Qo"),
            ("CodeWithHarry Java", "https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q"),
            ("HackerRank Java", "https://www.hackerrank.com/domains/java"),
            ("GeeksforGeeks Java", "https://practice.geeksforgeeks.org/explore/?category[]=Java"),
            ("LeetCode Java Problems", "https://leetcode.com/problemset/?languageTags=java"),
            ("Java Projects GitHub", "https://github.com/topics/java-projects"),
            ("Programiz Java", "https://www.programiz.com/java-programming"),
            ("JavaPoint Tutorial", "https://www.javatpoint.com/java-tutorial")
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
            ("CodeWithHarry Web", "https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg"),
            ("The Odin Project", "https://www.theodinproject.com/"),
            ("Frontend Mentor", "https://www.frontendmentor.io/"),
            ("CSS Tricks", "https://css-tricks.com/"),
            ("JavaScript Info", "https://javascript.info/"),
            ("FreeCodeCamp Practice", "https://www.freecodecamp.org/"),
            ("Web Projects GitHub", "https://github.com/topics/web-projects"),
            ("Roadmap.sh Web", "https://roadmap.sh/frontend"),
            ("Kevin Powell CSS", "https://www.youtube.com/@KevinPowell"),
            ("Fireship Web", "https://www.youtube.com/@Fireship")
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
            ("Scikit-learn Docs", "https://scikit-learn.org/stable/"),
            ("Sentdex ML Playlist", "https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v"),
            ("Andrej Karpathy AI", "https://www.youtube.com/@AndrejKarpathy"),
            ("Fast.ai Course", "https://www.fast.ai/"),
            ("HackerRank ML", "https://www.hackerrank.com/domains/ai"),
            ("AI Projects GitHub", "https://github.com/topics/machine-learning-projects"),
            ("Papers With Code", "https://paperswithcode.com/"),
            ("Roadmap.sh AI", "https://roadmap.sh/ai-data-scientist"),
            ("3Blue1Brown Neural Nets", "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi")
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
            ("Analytics Vidhya", "https://www.analyticsvidhya.com/"),
            ("Krish Naik DS", "https://www.youtube.com/@krishnaik06"),
            ("CodeBasics DS", "https://www.youtube.com/@codebasics"),
            ("Towards Data Science", "https://towardsdatascience.com/"),
            ("Pandas Docs", "https://pandas.pydata.org/docs/"),
            ("Matplotlib Docs", "https://matplotlib.org/stable/tutorials/"),
            ("DS Projects GitHub", "https://github.com/topics/data-science-projects"),
            ("Seaborn Gallery", "https://seaborn.pydata.org/examples/index.html"),
            ("DataCamp Free", "https://www.datacamp.com/courses/free")
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
            ("Mode SQL Tutorial", "https://mode.com/sql-tutorial/"),
            ("HackerRank SQL", "https://www.hackerrank.com/domains/sql"),
            ("LeetCode SQL", "https://leetcode.com/problemset/?topicSlugs=database"),
            ("MySQL Docs", "https://dev.mysql.com/doc/"),
            ("CodeWithHarry SQL", "https://www.youtube.com/watch?v=hlGoQC332VM"),
            ("SQL Projects GitHub", "https://github.com/topics/sql-projects"),
            ("PostgreSQL Tutorial", "https://www.postgresqltutorial.com/"),
            ("Khan Academy SQL", "https://www.khanacademy.org/computing/computer-programming/sql"),
            ("Programiz SQL", "https://www.programiz.com/sql")
        ]
    },

    "dsa": {
        "roadmap": [
            "Arrays & Strings",
            "Linked Lists",
            "Stacks & Queues",
            "Trees & Graphs",
            "Sorting & Searching",
            "Dynamic Programming",
            "Practice 100+ Problems"
        ],
        "resources": [
            ("Striver DSA Sheet", "https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/"),
            ("Apna College DSA", "https://www.youtube.com/watch?v=rZ41y93P2Qo"),
            ("FreeCodeCamp DSA", "https://www.youtube.com/watch?v=8hly31xKli0"),
            ("CodeWithHarry DSA", "https://www.youtube.com/playlist?list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi"),
            ("GeeksforGeeks DSA", "https://www.geeksforgeeks.org/data-structures/"),
            ("LeetCode Practice", "https://leetcode.com/problemset/"),
            ("HackerRank DSA", "https://www.hackerrank.com/domains/data-structures"),
            ("CodeChef DSA", "https://www.codechef.com/practice"),
            ("Codeforces", "https://codeforces.com/"),
            ("Neetcode DSA Roadmap", "https://neetcode.io/roadmap"),
            ("DSA Projects GitHub", "https://github.com/topics/data-structures"),
            ("Visualgo (Visualize DSA)", "https://visualgo.net/en"),
            ("CS50 Harvard", "https://cs50.harvard.edu/x/")
        ]
    }
}
# =========================
# PROJECTS DATA
# =========================
PROJECTS = [
    # AI / ML Projects
    {"id": "ai_resume", "title": "AI Resume Analyzer", "level": "Advanced", "tags": ["Python", "AI", "NLP"]},
    {"id": "face_attendance", "title": "Smart Attendance System using Face Recognition", "level": "Advanced", "tags": ["Python", "AI", "OpenCV"]},
    {"id": "student_prediction", "title": "Student Performance Prediction System", "level": "Intermediate", "tags": ["Python", "ML", "Data Science"]},
    {"id": "fake_news", "title": "Fake News Detection System", "level": "Intermediate", "tags": ["Python", "ML", "NLP"]},
    {"id": "traffic_sign", "title": "Traffic Sign Recognition System", "level": "Advanced", "tags": ["Python", "AI", "OpenCV"]},
    {"id": "sentiment_analysis", "title": "Sentiment Analysis System", "level": "Intermediate", "tags": ["Python", "NLP", "ML"]},
    {"id": "disease_prediction", "title": "Disease Prediction System", "level": "Advanced", "tags": ["Python", "ML", "Healthcare"]},
    {"id": "image_caption", "title": "AI Image Caption Generator", "level": "Advanced", "tags": ["Python", "AI", "Deep Learning"]},

    # Web Projects
    {"id": "job_portal", "title": "Job Portal Website", "level": "Intermediate", "tags": ["Web", "Flask", "Database"]},
    {"id": "elearning", "title": "E-Learning Platform", "level": "Intermediate", "tags": ["Web", "Flask", "Database"]},
    {"id": "food_order", "title": "Online Food Ordering System", "level": "Intermediate", "tags": ["Web", "Flask", "Database"]},
    {"id": "portfolio_builder", "title": "Personal Portfolio Builder", "level": "Beginner", "tags": ["Web", "HTML", "CSS"]},
    {"id": "blog_platform", "title": "Blog Platform", "level": "Beginner", "tags": ["Web", "Flask", "Database"]},
    {"id": "weather_app", "title": "Weather Forecast Web App", "level": "Beginner", "tags": ["Web", "API", "JavaScript"]},
    {"id": "url_shortener", "title": "URL Shortener App", "level": "Beginner", "tags": ["Web", "Flask", "Database"]},
    {"id": "quiz_platform", "title": "Online Quiz Platform", "level": "Intermediate", "tags": ["Web", "Flask", "JavaScript"]},
    {"id": "news_aggregator", "title": "News Aggregator Website", "level": "Intermediate", "tags": ["Web", "API", "Python"]},

    # System / Backend Projects
    {"id": "online_exam", "title": "Online Examination System", "level": "Intermediate", "tags": ["Python", "Flask", "Database"]},
    {"id": "library_mgmt", "title": "Library Management System", "level": "Beginner", "tags": ["Python", "Database", "Flask"]},
    {"id": "blood_donation", "title": "Blood Donation Management System", "level": "Intermediate", "tags": ["Web", "Flask", "Database"]},
    {"id": "event_mgmt", "title": "College Event Management System", "level": "Intermediate", "tags": ["Web", "Flask", "Database"]},
    {"id": "online_voting", "title": "Online Voting System", "level": "Intermediate", "tags": ["Python", "Flask", "Security"]},
    {"id": "expense_tracker", "title": "Smart Expense Tracker", "level": "Beginner", "tags": ["Python", "Flask", "Database"]},
    {"id": "hospital_mgmt", "title": "Hospital Management System", "level": "Advanced", "tags": ["Python", "Database", "Flask"]},
    {"id": "inventory_mgmt", "title": "Inventory Management System", "level": "Intermediate", "tags": ["Python", "Database", "Flask"]},
    {"id": "gym_mgmt", "title": "Gym Management System", "level": "Beginner", "tags": ["Python", "Database", "Flask"]},

    # AI Chatbot / Recommendation
    {"id": "helpdesk_chatbot", "title": "Campus Helpdesk Chatbot", "level": "Intermediate", "tags": ["Python", "AI", "NLP"]},
    {"id": "internship_reco", "title": "Internship Recommendation Platform", "level": "Intermediate", "tags": ["Python", "ML", "Web"]},
    {"id": "skill_reco", "title": "Skill Recommendation System", "level": "Intermediate", "tags": ["Python", "ML", "Web"]},
    {"id": "movie_reco", "title": "Movie Recommendation System", "level": "Intermediate", "tags": ["Python", "ML", "Data Science"]},
    {"id": "chat_app", "title": "Real-Time Chat Application", "level": "Advanced", "tags": ["Web", "Python", "Socket"]},

    # Data Science Projects
    {"id": "covid_analysis", "title": "COVID-19 Data Analysis Dashboard", "level": "Intermediate", "tags": ["Python", "Data Science", "Visualization"]},
    {"id": "stock_prediction", "title": "Stock Price Prediction System", "level": "Advanced", "tags": ["Python", "ML", "Data Science"]},
    {"id": "crime_analysis", "title": "Crime Data Analysis System", "level": "Intermediate", "tags": ["Python", "Data Science", "Visualization"]},
]
# =========================
# LIVE HACKATHONS DATA
# =========================

from datetime import date

HACKATHONS = [
    {
        "name": "Smart India Hackathon 2025",
        "platform": "SIH",
        "url": "https://www.sih.gov.in/",
        "start": date(2025, 11, 1),
        "end": date(2026, 12, 31),
        "tag": "Government",
        "color": "#ff6b35"
    },
    {
        "name": "Google Solution Challenge 2026",
        "platform": "Google",
        "url": "https://developers.google.com/community/gdsc-solution-challenge",
        "start": date(2026, 1, 1),
        "end": date(2026, 5, 31),
        "tag": "Global",
        "color": "#34a853"
    },
    {
        "name": "MLH Local Hack Day 2026",
        "platform": "MLH",
        "url": "https://localhackday.mlh.io/",
        "start": date(2026, 1, 1),
        "end": date(2026, 12, 31),
        "tag": "Community",
        "color": "#9b59b6"
    },
    {
        "name": "Flipkart Grid 6.0",
        "platform": "Flipkart",
        "url": "https://dare2compete.com/hackathon/flipkart-grid-60",
        "start": date(2026, 2, 1),
        "end": date(2026, 6, 30),
        "tag": "Industry",
        "color": "#f39c12"
    },
    {
        "name": "HackWithInfy 2026",
        "platform": "Infosys",
        "url": "https://www.hackerearth.com/challenges/hackathon/hackwithinfy/",
        "start": date(2026, 1, 1),
        "end": date(2026, 6, 30),
        "tag": "Industry",
        "color": "#4a90d9"
    },
    {
        "name": "Microsoft Imagine Cup 2026",
        "platform": "Microsoft",
        "url": "https://imaginecup.microsoft.com",
        "start": date(2026, 1, 1),
        "end": date(2026, 5, 31),
        "tag": "Global",
        "color": "#00a4ef"
    },
    {
        "name": "Devfolio Hackathons",
        "platform": "Devfolio",
        "url": "https://devfolio.co/hackathons",
        "start": date(2026, 1, 1),
        "end": date(2026, 12, 31),
        "tag": "Community",
        "color": "#3770ff"
    },
    {
        "name": "Unstop Hackathons 2026",
        "platform": "Unstop",
        "url": "https://unstop.com/hackathons",
        "start": date(2026, 1, 1),
        "end": date(2026, 12, 31),
        "tag": "Community",
        "color": "#e84393"
    },
    {
        "name": "HackerEarth Sprints 2026",
        "platform": "HackerEarth",
        "url": "https://www.hackerearth.com/challenges/hackathon/",
        "start": date(2026, 1, 1),
        "end": date(2026, 12, 31),
        "tag": "Industry",
        "color": "#44a0f5"
    },
    {
        "name": "Kaggle Competitions 2026",
        "platform": "Kaggle",
        "url": "https://www.kaggle.com/competitions",
        "start": date(2026, 1, 1),
        "end": date(2026, 12, 31),
        "tag": "Data Science",
        "color": "#20beff"
    },
    {
        "name": "Dare2Compete Hackathons",
        "platform": "Dare2Compete",
        "url": "https://dare2compete.com/hackathons",
        "start": date(2026, 1, 1),
        "end": date(2026, 12, 31),
        "tag": "Community",
        "color": "#ff4757"
    },
    {
        "name": "Amazon ML Challenge 2026",
        "platform": "Amazon",
        "url": "https://www.hackerearth.com/challenges/hackathon/amazon-ml-challenge/",
        "start": date(2026, 1, 1),
        "end": date(2026, 8, 31),
        "tag": "Industry",
        "color": "#ff9900"
    },
    {
        "name": "HackCBS 2026",
        "platform": "HackCBS",
        "url": "https://hackcbs.tech/",
        "start": date(2026, 1, 1),
        "end": date(2026, 11, 30),
        "tag": "Student",
        "color": "#6c5ce7"
    },
    {
        "name": "HackBMU 2026",
        "platform": "BML Munjal University",
        "url": "https://hackbmu.tech/",
        "start": date(2026, 1, 1),
        "end": date(2026, 10, 31),
        "tag": "Student",
        "color": "#00b894"
    },
    {
        "name": "HackJNU 2026",
        "platform": "JNU",
        "url": "https://devfolio.co/hackathons",
        "start": date(2026, 3, 1),
        "end": date(2026, 12, 31),
        "tag": "Student",
        "color": "#fd79a8"
    },
    {
        "name": "TCS CodeVita 2026",
        "platform": "TCS",
        "url": "https://www.tcscodevita.com/",
        "start": date(2026, 1, 1),
        "end": date(2026, 9, 30),
        "tag": "Industry",
        "color": "#e17055"
    },
    {
        "name": "Wipro Talent Next Hackathon",
        "platform": "Wipro",
        "url": "https://unstop.com/hackathons",
        "start": date(2026, 2, 1),
        "end": date(2026, 12, 31),
        "tag": "Industry",
        "color": "#0984e3"
    },
    {
        "name": "ETHIndia 2026",
        "platform": "ETHIndia",
        "url": "https://ethindia.co/",
        "start": date(2026, 6, 1),
        "end": date(2026, 12, 31),
        "tag": "Web3",
        "color": "#6c5ce7"
    },
    {
        "name": "OpenAI Hackathon 2026",
        "platform": "OpenAI",
        "url": "https://openai.com/",
        "start": date(2026, 1, 1),
        "end": date(2026, 12, 31),
        "tag": "AI",
        "color": "#00a67e"
    },
    {
        "name": "GitHub Field Day 2026",
        "platform": "GitHub",
        "url": "https://github.com/githubfieldday",
        "start": date(2026, 1, 1),
        "end": date(2026, 12, 31),
        "tag": "Global",
        "color": "#222222"
    },
]

# =========================
# BASIC ROUTES
# =========================

@app.route("/")
def opening():
    return render_template("opening.html")


@app.route("/dashboard")
def dashboard():
    today = date.today()
    live_hackathons = [h for h in HACKATHONS if h["start"] <= today <= h["end"]]
    skills_count = len(SKILLS)
    projects_count = len(PROJECTS)
    hackathons_count = len(live_hackathons)
    return render_template(
        "dashboard.html",
        skills_count=skills_count,
        projects_count=projects_count,
        hackathons_count=hackathons_count,
        live_hackathons=live_hackathons
    )

    return render_template(
        "dashboard.html",
        skills_count=skills_count,
        projects_count=projects_count,
        hackathons_count=hackathons_count
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/dashboard")
    return render_template("login.html")
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect("/dashboard")

    return render_template("register.html")





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
    import random

    question_bank = {
        "python": [
            {"question": "What keyword is used to define a function in Python?", "options": ["def", "fun", "define", "function"], "answer": "def"},
            {"question": "Which data type is immutable in Python?", "options": ["List", "Tuple", "Set", "Dictionary"], "answer": "Tuple"},
            {"question": "What does len() do?", "options": ["Returns length", "Deletes list", "Adds element", "Sorts list"], "answer": "Returns length"},
            {"question": "Which symbol is used for comments in Python?", "options": ["//", "#", "/*", "--"], "answer": "#"},
            {"question": "What is the output of 2**3 in Python?", "options": ["6", "8", "9", "5"], "answer": "8"},
            {"question": "Which method adds an element to a list?", "options": ["add()", "append()", "insert()", "push()"], "answer": "append()"},
            {"question": "What does 'import' do in Python?", "options": ["Creates a file", "Loads a module", "Deletes a module", "Runs a script"], "answer": "Loads a module"},
            {"question": "What is the correct way to create a dictionary?", "options": ["d = []", "d = ()", "d = {}", "d = <>"], "answer": "d = {}"},
            {"question": "Which loop is used to iterate over a sequence?", "options": ["while", "do-while", "for", "repeat"], "answer": "for"},
            {"question": "What does 'break' do in a loop?", "options": ["Skips current iteration", "Exits the loop", "Restarts loop", "Pauses loop"], "answer": "Exits the loop"},
            {"question": "What is the output of type(3.14)?", "options": ["int", "float", "double", "str"], "answer": "float"},
            {"question": "Which function is used to take user input?", "options": ["scan()", "read()", "input()", "get()"], "answer": "input()"},
            {"question": "How do you start an if statement in Python?", "options": ["if x == 1 then:", "if (x == 1):", "if x == 1:", "if x = 1:"], "answer": "if x == 1:"},
            {"question": "What does 'pass' do in Python?", "options": ["Exits program", "Does nothing", "Skips loop", "Throws error"], "answer": "Does nothing"},
            {"question": "What is a lambda function?", "options": ["A class method", "A named function", "An anonymous function", "A built-in function"], "answer": "An anonymous function"},
            {"question": "Which module is used for maths in Python?", "options": ["numpy", "math", "calc", "numbers"], "answer": "math"},
            {"question": "What does 'self' refer to in a class?", "options": ["The class itself", "The current object", "The parent class", "A variable"], "answer": "The current object"},
            {"question": "What is list comprehension?", "options": ["Sorting a list", "A short way to create lists", "Deleting duplicates", "Merging lists"], "answer": "A short way to create lists"},
            {"question": "What does strip() do to a string?", "options": ["Splits string", "Removes whitespace", "Reverses string", "Converts to uppercase"], "answer": "Removes whitespace"},
            {"question": "Which of these is a Python framework?", "options": ["Laravel", "Flask", "Spring", "Rails"], "answer": "Flask"},
        ],

        "java": [
            {"question": "Which keyword is used to create a class in Java?", "options": ["class", "Class", "new", "create"], "answer": "class"},
            {"question": "What is the size of int in Java?", "options": ["2 bytes", "4 bytes", "8 bytes", "1 byte"], "answer": "4 bytes"},
            {"question": "Which method is the entry point of a Java program?", "options": ["start()", "run()", "main()", "init()"], "answer": "main()"},
            {"question": "What does JVM stand for?", "options": ["Java Virtual Machine", "Java Visual Module", "Java Verified Method", "Java Version Manager"], "answer": "Java Virtual Machine"},
            {"question": "Which keyword is used for inheritance in Java?", "options": ["inherits", "extends", "implements", "super"], "answer": "extends"},
            {"question": "What is the default value of an int variable in Java?", "options": ["null", "1", "0", "undefined"], "answer": "0"},
            {"question": "Which collection does not allow duplicate values?", "options": ["ArrayList", "LinkedList", "Set", "Queue"], "answer": "Set"},
            {"question": "What does 'final' keyword mean in Java?", "options": ["Last method", "Cannot be changed", "End of program", "Private method"], "answer": "Cannot be changed"},
            {"question": "Which keyword is used to handle exceptions?", "options": ["error", "try-catch", "handle", "exception"], "answer": "try-catch"},
            {"question": "What is polymorphism in Java?", "options": ["Multiple classes", "One method many forms", "Multiple inheritance", "Abstract class"], "answer": "One method many forms"},
            {"question": "What is an interface in Java?", "options": ["A class with code", "A blueprint with no implementation", "A variable type", "An object"], "answer": "A blueprint with no implementation"},
            {"question": "Which keyword creates a new object?", "options": ["create", "new", "make", "object"], "answer": "new"},
            {"question": "What does 'static' mean in Java?", "options": ["Belongs to object", "Belongs to class", "Cannot be used", "Final variable"], "answer": "Belongs to class"},
            {"question": "What is the parent class of all Java classes?", "options": ["Base", "Super", "Object", "Root"], "answer": "Object"},
            {"question": "What is a constructor in Java?", "options": ["A method to destroy object", "A method called when object is created", "A static method", "An interface method"], "answer": "A method called when object is created"},
            {"question": "Which access modifier makes a member visible everywhere?", "options": ["private", "protected", "public", "default"], "answer": "public"},
            {"question": "What does ArrayList store?", "options": ["Fixed size array", "Dynamic size elements", "Only integers", "Only strings"], "answer": "Dynamic size elements"},
            {"question": "What is method overloading?", "options": ["Same method name different parameters", "Overwriting a method", "Deleting a method", "Calling super method"], "answer": "Same method name different parameters"},
            {"question": "Which loop checks condition after executing?", "options": ["for", "while", "do-while", "foreach"], "answer": "do-while"},
            {"question": "What is encapsulation?", "options": ["Hiding data using access modifiers", "Multiple inheritance", "Method overriding", "Creating objects"], "answer": "Hiding data using access modifiers"},
        ],

        "web": [
            {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Machine Language", "Hyper Transfer Markup Language", "None"], "answer": "Hyper Text Markup Language"},
            {"question": "Which tag is used for the largest heading?", "options": ["<h6>", "<h1>", "<head>", "<title>"], "answer": "<h1>"},
            {"question": "What does CSS stand for?", "options": ["Computer Style Sheets", "Creative Style System", "Cascading Style Sheets", "Colorful Style Sheets"], "answer": "Cascading Style Sheets"},
            {"question": "Which property changes text color in CSS?", "options": ["font-color", "text-color", "color", "foreground"], "answer": "color"},
            {"question": "What does DOM stand for?", "options": ["Document Object Model", "Data Object Module", "Document Oriented Model", "Display Object Method"], "answer": "Document Object Model"},
            {"question": "Which tag creates a hyperlink?", "options": ["<link>", "<href>", "<a>", "<url>"], "answer": "<a>"},
            {"question": "What is the correct CSS syntax?", "options": ["body {color: red}", "body: color=red", "{body; color: red}", "body | color | red"], "answer": "body {color: red}"},
            {"question": "Which JavaScript method selects an element by ID?", "options": ["getElement()", "getElementById()", "selectById()", "findId()"], "answer": "getElementById()"},
            {"question": "What does 'responsive design' mean?", "options": ["Fast loading website", "Website works on all screen sizes", "Animated website", "SEO optimized"], "answer": "Website works on all screen sizes"},
            {"question": "Which CSS property makes a flex container?", "options": ["display: block", "display: flex", "display: grid", "display: inline"], "answer": "display: flex"},
            {"question": "What is the purpose of the <meta> tag?", "options": ["Add images", "Provide metadata about the page", "Create links", "Add styles"], "answer": "Provide metadata about the page"},
            {"question": "Which HTTP method is used to send form data?", "options": ["GET", "POST", "PUT", "DELETE"], "answer": "POST"},
            {"question": "What does API stand for?", "options": ["Application Programming Interface", "Applied Program Integration", "Automated Process Interface", "App Protocol Interface"], "answer": "Application Programming Interface"},
            {"question": "What is Bootstrap used for?", "options": ["Backend development", "Database management", "Responsive front-end design", "Server configuration"], "answer": "Responsive front-end design"},
            {"question": "Which tag is used for unordered list?", "options": ["<ol>", "<li>", "<ul>", "<list>"], "answer": "<ul>"},
            {"question": "What is localStorage in JavaScript?", "options": ["Server storage", "Browser storage", "Database", "Cookie"], "answer": "Browser storage"},
            {"question": "What does 'async' do in JavaScript?", "options": ["Runs code faster", "Makes function return a Promise", "Stops execution", "Creates a loop"], "answer": "Makes function return a Promise"},
            {"question": "Which selector targets all elements of a class?", "options": ["#classname", ".classname", "*classname", "@classname"], "answer": ".classname"},
            {"question": "What is JSON?", "options": ["JavaScript Object Notation", "Java Standard Object Name", "JavaScript Online Network", "Java Source Object Node"], "answer": "JavaScript Object Notation"},
            {"question": "What does 'z-index' control in CSS?", "options": ["Font size", "Stacking order of elements", "Zoom level", "Element width"], "answer": "Stacking order of elements"},
        ],

        "ai": [
            {"question": "What does AI stand for?", "options": ["Automated Integration", "Artificial Intelligence", "Automated Interface", "Artificial Interface"], "answer": "Artificial Intelligence"},
            {"question": "What is supervised learning?", "options": ["Learning without data", "Learning with labeled data", "Learning with unlabeled data", "Reinforcement learning"], "answer": "Learning with labeled data"},
            {"question": "What is a neural network?", "options": ["A type of database", "A model inspired by the human brain", "A sorting algorithm", "A web framework"], "answer": "A model inspired by the human brain"},
            {"question": "What does ML stand for?", "options": ["Machine Language", "Machine Learning", "Model Logic", "Multi Layer"], "answer": "Machine Learning"},
            {"question": "Which algorithm is used for classification?", "options": ["Linear Regression", "K-Means", "Decision Tree", "PCA"], "answer": "Decision Tree"},
            {"question": "What is overfitting in ML?", "options": ["Model works well on test data", "Model memorizes training data too well", "Model has too few parameters", "Model trains too slowly"], "answer": "Model memorizes training data too well"},
            {"question": "What is the purpose of a training dataset?", "options": ["To test the model", "To train the model", "To deploy the model", "To clean the data"], "answer": "To train the model"},
            {"question": "What does NLP stand for?", "options": ["Natural Language Processing", "Neural Logic Programming", "Network Layer Protocol", "Node Learning Process"], "answer": "Natural Language Processing"},
            {"question": "Which library is most used for ML in Python?", "options": ["NumPy", "Flask", "Scikit-learn", "Matplotlib"], "answer": "Scikit-learn"},
            {"question": "What is a confusion matrix?", "options": ["A matrix to confuse models", "A table showing model prediction results", "A type of neural network", "A data cleaning tool"], "answer": "A table showing model prediction results"},
            {"question": "What is deep learning?", "options": ["ML with many neural network layers", "Basic machine learning", "Data cleaning process", "Feature engineering"], "answer": "ML with many neural network layers"},
            {"question": "What is reinforcement learning?", "options": ["Learning from labeled data", "Learning by trial and error with rewards", "Unsupervised learning", "Transfer learning"], "answer": "Learning by trial and error with rewards"},
            {"question": "What does CNN stand for in deep learning?", "options": ["Computer Neural Network", "Convolutional Neural Network", "Connected Node Network", "Core Neural Network"], "answer": "Convolutional Neural Network"},
            {"question": "What is the purpose of activation functions?", "options": ["To initialize weights", "To introduce non-linearity", "To normalize data", "To reduce overfitting"], "answer": "To introduce non-linearity"},
            {"question": "What is gradient descent?", "options": ["A data visualization technique", "An optimization algorithm", "A type of neural network", "A clustering method"], "answer": "An optimization algorithm"},
            {"question": "What is a feature in ML?", "options": ["A model output", "An input variable used for prediction", "A test result", "A hyperparameter"], "answer": "An input variable used for prediction"},
            {"question": "What is cross-validation?", "options": ["Testing on training data", "A technique to evaluate model performance", "A type of neural network", "Data augmentation"], "answer": "A technique to evaluate model performance"},
            {"question": "What does PCA stand for?", "options": ["Principal Component Analysis", "Primary Classification Algorithm", "Predictive Cluster Analysis", "Polynomial Curve Analysis"], "answer": "Principal Component Analysis"},
            {"question": "What is transfer learning?", "options": ["Sending data between models", "Using a pre-trained model for a new task", "Moving model to cloud", "Training from scratch"], "answer": "Using a pre-trained model for a new task"},
            {"question": "What is the role of a loss function?", "options": ["To visualize data", "To measure how wrong the model is", "To clean data", "To split dataset"], "answer": "To measure how wrong the model is"},
        ],

        "datascience": [
            {"question": "What is data science?", "options": ["Only coding", "Extracting insights from data", "Building websites", "Networking"], "answer": "Extracting insights from data"},
            {"question": "Which library is used for data manipulation in Python?", "options": ["NumPy", "Pandas", "Matplotlib", "Seaborn"], "answer": "Pandas"},
            {"question": "What does EDA stand for?", "options": ["Exploratory Data Analysis", "Extended Data Algorithm", "External Data Access", "Estimated Data Analytics"], "answer": "Exploratory Data Analysis"},
            {"question": "Which chart is best for showing distribution?", "options": ["Bar chart", "Pie chart", "Histogram", "Line chart"], "answer": "Histogram"},
            {"question": "What is a null value in a dataset?", "options": ["Zero value", "Missing value", "Negative value", "String value"], "answer": "Missing value"},
            {"question": "What does correlation measure?", "options": ["Causation between variables", "Relationship strength between variables", "Average of variables", "Sum of variables"], "answer": "Relationship strength between variables"},
            {"question": "Which Python library is used for visualization?", "options": ["Pandas", "NumPy", "Matplotlib", "Scikit-learn"], "answer": "Matplotlib"},
            {"question": "What is feature engineering?", "options": ["Building new features from raw data", "Removing all features", "Testing model features", "Deploying models"], "answer": "Building new features from raw data"},
            {"question": "What is a DataFrame in Pandas?", "options": ["A 1D array", "A 2D labeled data structure", "A chart", "A SQL table"], "answer": "A 2D labeled data structure"},
            {"question": "What does groupby() do in Pandas?", "options": ["Sorts data", "Groups data by a column", "Merges dataframes", "Fills null values"], "answer": "Groups data by a column"},
            {"question": "What is the mean of [2, 4, 6, 8]?", "options": ["4", "5", "6", "10"], "answer": "5"},
            {"question": "What is standard deviation?", "options": ["Average value", "Measure of spread in data", "Maximum value", "Minimum value"], "answer": "Measure of spread in data"},
            {"question": "Which format is most common for datasets?", "options": ["PDF", "CSV", "DOCX", "XML"], "answer": "CSV"},
            {"question": "What does fillna() do in Pandas?", "options": ["Deletes null values", "Fills null values", "Finds null values", "Counts null values"], "answer": "Fills null values"},
            {"question": "What is data normalization?", "options": ["Adding more data", "Scaling data to a standard range", "Removing duplicates", "Sorting data"], "answer": "Scaling data to a standard range"},
            {"question": "What is a box plot used for?", "options": ["Showing trends", "Showing distribution and outliers", "Comparing categories", "Showing relationships"], "answer": "Showing distribution and outliers"},
            {"question": "What does merge() do in Pandas?", "options": ["Splits dataframes", "Combines dataframes", "Sorts dataframes", "Filters dataframes"], "answer": "Combines dataframes"},
            {"question": "What is an outlier in data?", "options": ["Average value", "Most common value", "A value far from others", "A null value"], "answer": "A value far from others"},
            {"question": "What is Seaborn used for?", "options": ["Data cleaning", "Statistical data visualization", "Machine learning", "Data storage"], "answer": "Statistical data visualization"},
            {"question": "What does value_counts() return in Pandas?", "options": ["Sum of values", "Count of unique values", "Average values", "Sorted values"], "answer": "Count of unique values"},
        ],

        "sql": [
            {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Logic", "System Query Language", "Standard Question Language"], "answer": "Structured Query Language"},
            {"question": "Which command retrieves data from a table?", "options": ["INSERT", "UPDATE", "SELECT", "DELETE"], "answer": "SELECT"},
            {"question": "Which clause filters records in SQL?", "options": ["ORDER BY", "GROUP BY", "WHERE", "HAVING"], "answer": "WHERE"},
            {"question": "What does PRIMARY KEY do?", "options": ["Allows duplicates", "Uniquely identifies each row", "Deletes rows", "Joins tables"], "answer": "Uniquely identifies each row"},
            {"question": "Which JOIN returns all rows from both tables?", "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"], "answer": "FULL OUTER JOIN"},
            {"question": "What does COUNT() do?", "options": ["Sums values", "Counts rows", "Finds maximum", "Groups rows"], "answer": "Counts rows"},
            {"question": "Which command adds new data to a table?", "options": ["UPDATE", "ALTER", "INSERT INTO", "CREATE"], "answer": "INSERT INTO"},
            {"question": "What does GROUP BY do?", "options": ["Sorts results", "Filters rows", "Groups rows with same values", "Joins tables"], "answer": "Groups rows with same values"},
            {"question": "What is a FOREIGN KEY?", "options": ["A key from another country", "A key linking two tables", "A unique key", "A primary key"], "answer": "A key linking two tables"},
            {"question": "Which command removes all rows from a table?", "options": ["DELETE", "DROP", "TRUNCATE", "REMOVE"], "answer": "TRUNCATE"},
            {"question": "What does DISTINCT do?", "options": ["Sorts values", "Returns unique values", "Counts values", "Groups values"], "answer": "Returns unique values"},
            {"question": "What does ORDER BY do?", "options": ["Filters data", "Groups data", "Sorts results", "Joins tables"], "answer": "Sorts results"},
            {"question": "Which function returns the highest value?", "options": ["COUNT()", "MIN()", "MAX()", "SUM()"], "answer": "MAX()"},
            {"question": "What is a subquery?", "options": ["A query outside main query", "A query inside another query", "A deleted query", "A saved query"], "answer": "A query inside another query"},
            {"question": "What does LIKE '%a%' do?", "options": ["Finds exact match", "Finds values containing 'a'", "Finds values starting with 'a'", "Finds values ending with 'a'"], "answer": "Finds values containing 'a'"},
            {"question": "Which command modifies existing data?", "options": ["INSERT", "ALTER", "UPDATE", "MODIFY"], "answer": "UPDATE"},
            {"question": "What is a VIEW in SQL?", "options": ["A physical table", "A virtual table based on a query", "A stored procedure", "An index"], "answer": "A virtual table based on a query"},
            {"question": "What does HAVING clause do?", "options": ["Filters rows before grouping", "Filters groups after GROUP BY", "Joins tables", "Sorts data"], "answer": "Filters groups after GROUP BY"},
            {"question": "What does NULL mean in SQL?", "options": ["Zero", "Empty string", "Missing or unknown value", "False"], "answer": "Missing or unknown value"},
            {"question": "Which command creates a new table?", "options": ["NEW TABLE", "ADD TABLE", "CREATE TABLE", "MAKE TABLE"], "answer": "CREATE TABLE"},
        ],

        "dsa": [
            {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"], "answer": "O(log n)"},
            {"question": "Which data structure uses LIFO?", "options": ["Queue", "Stack", "Array", "Tree"], "answer": "Stack"},
            {"question": "Which data structure uses FIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue"},
            {"question": "What is the worst case of bubble sort?", "options": ["O(n)", "O(log n)", "O(n²)", "O(n log n)"], "answer": "O(n²)"},
            {"question": "What is a linked list?", "options": ["Array with fixed size", "Nodes connected by pointers", "A stack", "A binary tree"], "answer": "Nodes connected by pointers"},
            {"question": "Which traversal visits root first?", "options": ["Inorder", "Postorder", "Preorder", "Level order"], "answer": "Preorder"},
            {"question": "What is the time complexity of accessing an array element?", "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"], "answer": "O(1)"},
            {"question": "What is dynamic programming?", "options": ["Writing dynamic code", "Solving problems by storing subproblem results", "Using dynamic arrays", "Runtime programming"], "answer": "Solving problems by storing subproblem results"},
            {"question": "Which algorithm is fastest for sorting on average?", "options": ["Bubble Sort", "Selection Sort", "Quick Sort", "Insertion Sort"], "answer": "Quick Sort"},
            {"question": "What is a binary search tree?", "options": ["Tree with two children max where left < root < right", "Tree with only one child", "A heap tree", "A balanced tree"], "answer": "Tree with two children max where left < root < right"},
            {"question": "What does BFS stand for?", "options": ["Binary First Search", "Breadth First Search", "Best First Search", "Backward First Search"], "answer": "Breadth First Search"},
            {"question": "What is the space complexity of an array of size n?", "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"], "answer": "O(n)"},
            {"question": "Which data structure is used for recursion?", "options": ["Queue", "Stack", "Array", "Heap"], "answer": "Stack"},
            {"question": "What is a hash table used for?", "options": ["Sorting data", "Fast key-value lookup", "Traversing trees", "Graph search"], "answer": "Fast key-value lookup"},
            {"question": "What is memoization?", "options": ["Memorizing code", "Caching results of expensive function calls", "A sorting technique", "A graph algorithm"], "answer": "Caching results of expensive function calls"},
            {"question": "What is the height of a balanced binary tree with n nodes?", "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"], "answer": "O(log n)"},
            {"question": "Which sorting algorithm is stable?", "options": ["Quick Sort", "Heap Sort", "Merge Sort", "Selection Sort"], "answer": "Merge Sort"},
            {"question": "What is a graph?", "options": ["A chart", "Nodes connected by edges", "A sorted array", "A type of tree"], "answer": "Nodes connected by edges"},
            {"question": "What does DFS stand for?", "options": ["Data File System", "Depth First Search", "Dynamic First Search", "Direct File Search"], "answer": "Depth First Search"},
            {"question": "What is the best case of insertion sort?", "options": ["O(n²)", "O(n log n)", "O(n)", "O(log n)"], "answer": "O(n)"},
        ]
    }

    skill_lower = skill.lower()
    all_questions = question_bank.get(skill_lower, [])
    questions = random.sample(all_questions, min(10, len(all_questions)))

    return render_template("skill_quiz.html", skill=skill, questions=questions)
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
@app.route('/internships')
def internships():
    return render_template('internships.html')
@app.route('/resume-tips')
def resume_tips():
    return render_template('resume_tips.html')
@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

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
    today = date.today()
    live_hackathons = [h for h in HACKATHONS if h["start"] <= today <= h["end"]]
    return render_template("ongoing_hackathons.html", live_hackathons=live_hackathons)
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
