from mail.mailer import Mailer
from mail.templates.new_ticket_temp import get_new_ticket_temp


def handle_new_order(message, logger):
    logger.info("New order ticket message, sending info mail")
    try:
        mailer = Mailer()

        html_body = get_new_ticket_temp(
            title="New Ticket Purchase was Successful!",
            message=f"Info: Ticket ID: {message['ticketId']}. User ID: {message['userId']}, Flight ID: {message['flightId']}",
            button_link="http://localhost/profile",
            button_text="View Tickets",
        )

        mailer.send_mail(
            subject="Ticket Purchase Confirmation",
            recipients=["pyfly700@gmail.com"],
            html_body=html_body,
        )
    except Exception as e:
        logger.error("Failed to send mail")
        
        
