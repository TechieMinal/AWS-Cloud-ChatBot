#  Cloud-Based Intelligent Chatbot  

This project is a **cloud-enabled intelligent chatbot** developed in Python to handle user queries efficiently using scalable cloud infrastructure. The system leverages AWS services, including **AWS Lambda and Amazon DynamoDB**, to provide high availability, low latency, and reliable performance in a serverless environment.  

The chatbot follows a modular architecture, enabling easy maintenance, extensibility, and seamless cloud integration while ensuring secure data processing and real-time responsiveness.

---

##  Project Structure  

| File | Description |
|------|-------------|
| `main.py` | Core application logic and execution flow |
| `create_bot.py` | Initializes and configures the chatbot |
| `lambda_function.py` | AWS Lambda handler for serverless execution |
| `setup_table.py` | Creates and manages DynamoDB tables |
| `upload_log.py` | Stores chatbot interaction logs in cloud storage |
| `requirement` | Lists all required Python dependencies |

---

##  Key Features  

- Serverless cloud deployment using AWS  
- Scalable and cost-efficient architecture  
- Secure data storage with DynamoDB  
- Real-time conversational interaction  
- Modular and maintainable code structure  

---

##  Technology Stack  

- **Programming Language:** Python  
- **Cloud Platform:** Amazon Web Services (AWS)  
- **AWS Services Used:**  
  - AWS Lambda  
  - Amazon DynamoDB  
  - AWS S3 (for logging and storage)  

---
 ## Install dependencies
 
 pip install -r requirement

 ---

 ## Run the chatbot

 python main.py

