import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()


def get_transactions(key, budget):
    print(key + " Budget:")
    done = False
    while done is False:
        buy = input("Did you buy anything? (yes/no): ")
        if buy == "no":
            break
        elif buy == "yes":
            repeat = False
            while repeat is False:
                description = input("What did you buy?: ")
                price = input("How much did it cost?: ")
                item = {'item': description, 'price': price}
                budget[key].append(item)
                print(description.title() + " was added to your " + key.lower() + " budget.")
                more = False
                while more is False:
                    add_more = input("Did you buy anything else? (yes/no): ").lower()
                    if add_more == "yes":
                        done, more, repeat = False, True, False
                    elif add_more == "no":
                        done, more, repeat = True, True, True
                        print(key + " budget completed.")
                    else:
                        print("Please enter yes or no.")
        else:
            print("Please enter yes or no.")


def send_email(table_list):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Today's Daily Budget Report"
    msg['From'] = "Daily Budget Report"
    msg['To'] = os.getenv('TO_EMAIL')

    table = ''
    for t in table_list:
        table += t

    html = """\
    <html>
      <head></head>
      <body>
        <p>Hello,<br>
           See below for your daily budget report.
            {}
        </p>
      </body>
    </html>
    """.format(table)

    msg.attach(MIMEText(html, 'html'))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(os.getenv('LOGIN_EMAIL'), os.getenv('LOGIN_PASS'))
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def create_html_table(key, items):
    html = '<table>'
    html += '<caption>{}</caption>'.format(key)
    html += '<th>Item</th>'
    html += '<th>Price</th></tr>'
    for data in items:
        item = data['item']
        price = data['price']
        html += '<tr><td>{}</td>'.format(item)
        html += '<td>{}</td></tr>'.format(price)
    html += '</table><br>'
    return html


def daily_budget():
    budget = {'Shopping': [],
              'Food': [],
              'Other': []}
    for key in budget.keys():
        get_transactions(key, budget)
    table_list = []
    for key in budget.keys():
        table = create_html_table(key, budget[key])
        table_list.append(table)
    send_email(table_list)


daily_budget()
