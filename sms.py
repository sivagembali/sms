from flask import Flask, redirect, url_for, request,current_app
import urllib 
app = Flask(__name__)
#method to send messages
@app.route('/')
def route():
    return  current_app.send_static_file('sms.html')

@app.route('/messages')
def messages():
    password = request.args.get('password')
    if(password == 'gvpmca'):
        mobiles = request.args.get('mobile')
        message = request.args.get('message')
        authkey = "203564APQ8NtYrE15aacdff2" # Your authentication key.
        #mobiles = "9705707580,8978098160" # Multiple mobiles numbers separated by comma.
        #message = "Status Demo" # Your message to send.
        sender = "MSGIND" # Sender ID,While using route4 sender id should be 6 characters long.
        route = "4" # Define route
        # Prepare you post parameters
        values = {
                 'authkey' : authkey,
                 'mobiles' : mobiles,
                 'message' : message,
                 'sender' : sender,
                 'route' : route
                 }
        url = "https://control.msg91.com/api/sendhttp.php" # API URL
        postdata = urllib.parse.urlencode(values) # URL encoding the data here.
        postdata = postdata.encode('utf-8')
        req = urllib.request.Request(url,postdata)
        response = urllib.request.urlopen(req)
        output = response.read() # Get Response
        print("hai")
        return "Message Sent Successfully"
    else:
        return "Invalid Password"
#"successfully send"
if __name__ == '__main__':
   app.run(debug=True)
