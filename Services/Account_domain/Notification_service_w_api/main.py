def auto_notifiy(request):
    import os
    from python_http_client import HTTPError
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    from flask import jsonify, abort
    
    if request.method == 'POST':
        notify_msg = request.get_json(silent=True)
        message = Mail(
            to_emails=notify_msg['to'],
            from_email=notify_msg['from'],
            subject=notify_msg['subject'],
            html_content=notify_msg['message']
        )

        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        try:
            response = sg.send(message)
            return jsonify({'message': f'Email sent to {notify_msg["to"]}'}), 200

        except HTTPError as e:
            return e.reason
    else:
        return abort(405)