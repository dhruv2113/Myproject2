from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
import smtplib

def send_email(to, subject, body):
    sender = "youremail@example.com"
    password = "your_app_password"  # Use an App Password if using Gmail

    message = f"Subject: {subject}\n\n{body}"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, to, message)

def email_tool_func(input_text):
    # You can parse the input however you want
    to = "receiver@example.com"
    subject = "Test from LangChain"
    body = input_text
    send_email(to, subject, body)
    return "Email sent."

# Wrap as a LangChain Tool
email_tool = Tool(
    name="EmailTool",
    func=email_tool_func,
    description="Use this tool to send an email. Input should be the email content."
)

# Use with a LangChain agent
llm = ChatOpenAI(model="gpt-4")
agent = initialize_agent([email_tool], llm, agent="zero-shot-react-description", verbose=True)

# Test agent
agent.run("Send an email saying 'This is a test email sent by LangChain.'")
