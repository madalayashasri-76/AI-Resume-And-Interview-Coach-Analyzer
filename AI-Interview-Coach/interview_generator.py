def generate_questions(role):

    questions = {

        "Data Analyst": [
            {
                "question": "Explain your experience with data analysis.",
                "answer": "I analyze data using Python, SQL, Excel, and visualization tools to extract meaningful insights."
            },
            {
                "question": "What is the difference between SQL WHERE and HAVING?",
                "answer": "WHERE filters rows before grouping, while HAVING filters grouped data after aggregation."
            },
            {
                "question": "Explain data visualization.",
                "answer": "Data visualization represents information using charts, graphs, and dashboards for better decision-making."
            },
            {
                "question": "What is normalization?",
                "answer": "Normalization organizes data in a database to reduce redundancy and improve consistency."
            },
            {
                "question": "Which tools have you used for data analysis?",
                "answer": "I have worked with Python, Pandas, SQL, Excel, Power BI, and Tableau."
            }
        ],

        "Python Developer": [
            {
                "question": "What are Python data structures?",
                "answer": "Python provides lists, tuples, dictionaries, and sets for storing data."
            },
            {
                "question": "Explain OOP concepts in Python.",
                "answer": "OOP concepts include classes, objects, inheritance, encapsulation, abstraction, and polymorphism."
            },
            {
                "question": "What are Python libraries?",
                "answer": "Libraries are reusable collections of code such as NumPy, Pandas, Streamlit, and Requests."
            },
            {
                "question": "What is exception handling?",
                "answer": "Exception handling uses try, except, else, and finally blocks to handle runtime errors."
            },
            {
                "question": "What is a Python decorator?",
                "answer": "A decorator modifies the behavior of a function without changing its original code."
            }
        ],

        "Full Stack Developer": [
            {
                "question": "Explain frontend and backend development.",
                "answer": "Frontend manages the user interface while backend handles business logic, databases, and APIs."
            },
            {
                "question": "What is an API?",
                "answer": "An API allows communication between different software applications."
            },
            {
                "question": "Explain database management.",
                "answer": "Database management involves storing, organizing, and retrieving application data efficiently."
            },
            {
                "question": "What is REST API?",
                "answer": "REST API is a web service architecture that uses HTTP methods like GET, POST, PUT, and DELETE."
            },
            {
                "question": "What is Git?",
                "answer": "Git is a version control system used to track code changes and collaborate with developers."
            }
        ],

        "Machine Learning Engineer": [
            {
                "question": "What is Machine Learning?",
                "answer": "Machine Learning enables systems to learn patterns from data and make predictions without explicit programming."
            },
            {
                "question": "Difference between supervised and unsupervised learning?",
                "answer": "Supervised learning uses labeled data, while unsupervised learning identifies patterns in unlabeled data."
            },
            {
                "question": "What is model evaluation?",
                "answer": "Model evaluation measures model performance using metrics such as Accuracy, Precision, Recall, F1-score, MAE, RMSE, and R²."
            },
            {
                "question": "What is overfitting?",
                "answer": "Overfitting occurs when a model learns the training data too well and performs poorly on unseen data."
            },
            {
                "question": "What is feature engineering?",
                "answer": "Feature engineering involves selecting, creating, and transforming variables to improve model performance."
            }
        ],

        "Software Engineer": [
            {
                "question": "Explain the Software Development Life Cycle (SDLC).",
                "answer": "SDLC includes planning, designing, development, testing, deployment, and maintenance."
            },
            {
                "question": "What is version control?",
                "answer": "Version control systems like Git help manage source code changes and team collaboration."
            },
            {
                "question": "Explain debugging.",
                "answer": "Debugging is the process of identifying and fixing errors in software."
            },
            {
                "question": "What is Agile methodology?",
                "answer": "Agile is a software development methodology that focuses on iterative development and customer feedback."
            },
            {
                "question": "What is object-oriented programming?",
                "answer": "Object-oriented programming organizes software into classes and objects for better code reuse and maintenance."
            }
        ]

    }

    return questions.get(role, [])