# iperf3_bandtest

## The .env file

You should create a <code>.env</code> file to keep a set of variables that you don't want to expose in the main codebase.

An example of this file is:

    REMOTE_HOST=172.30.118.72
    PORT=5001
    TIME=60
    TIMEWAIT=60
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    SMTP_USERNAME=sender_email@gmail.com
    SMTP_PASSWORD=sender_password
    TO_EMAIL=destination_email@gmail.com
