import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import smtplib
import ssl

def send_email():
    sender_email = "your_email@gmail.com"  # Replace with your email address
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", "end-1c")

    # Basic email validation
    if not (receiver_email and subject and body):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Email sending using OAuth2 authentication with Gmail
    try:
        port = 465
        smtp_server = "smtp.gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, get_app_password())
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, receiver_email, message)

        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

def get_app_password():
    # Function to retrieve the application-specific password (OAuth2 token)
    # You should implement a secure way to retrieve this token (e.g., reading from a config file).
    return "your_application_specific_password"

# Create the main application window
app = tk.Tk()
app.title("Enhanced Mail Application")
app.geometry("500x400")  # Set the initial window size

# Color palette (you can adjust these colors to your preference)
bg_color = "#EFEFEF"         # Light gray background color
label_color = "#333333"      # Dark gray label color
button_color = "#4CAF50"     # Green button color
text_color = "#FFFFFF"       # White text color

app.configure(bg=bg_color)

# GUI design
receiver_label = tk.Label(app, text="To:", fg=text_color, bg=bg_color)
receiver_label.pack()
receiver_entry = tk.Entry(app)
receiver_entry.pack(fill=tk.X, padx=10)

subject_label = tk.Label(app, text="Subject:", fg=text_color, bg=bg_color)
subject_label.pack()
subject_entry = tk.Entry(app)
subject_entry.pack(fill=tk.X, padx=10)

body_label = tk.Label(app, text="Body:", fg=text_color, bg=bg_color)
body_label.pack()
body_text = ScrolledText(app, wrap=tk.WORD, width=40, height=10)
body_text.pack(fill=tk.BOTH, padx=10, pady=5)

send_button = tk.Button(app, text="Send Email", command=send_email, bg=button_color, fg=text_color)
send_button.pack(pady=10)

# Start the application's main event loop
app.mainloop()
