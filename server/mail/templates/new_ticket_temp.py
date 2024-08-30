def get_new_ticket_temp (title, message, button_link,button_text ):
    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .email-container {{
                    font-family: Arial, sans-serif;
                    padding: 20px;
                    background-color: #f4f4f4;
                    text-align: center;
                }}
                .email-content {{
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                }}
                .email-title {{
                    font-size: 24px;
                    color: #333;
                    margin-bottom: 20px;
                }}
                .email-button {{
                    background-color: #28a745;
                    color: white;
                    padding: 12px 24px;
                    text-decoration: none;
                    border-radius: 5px;
                    display: inline-block;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="email-content">
                    <h1 class="email-title">{title}</h1>
                    <p>{message}</p>
                    <a href="{button_link}" class="email-button">{button_text}</a>
                </div>
            </div>
        </body>
        </html>
        """
