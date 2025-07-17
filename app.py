from flask import Flask, render_template, request
import joblib

# create the app
app = Flask(__name__) 

# load the trained model (happens only once)
pipeline = joblib.load("model/pipeline.pkl")

# define route for the main page
@app.route("/", methods = ["GET", "POST"])

def index():

    # SETTING UP VARIBALES
    PT_FULL_NAMES = {
    'a': 'Authority and Impersonation',
    'p': 'Phantom Riches',
    'f': 'Fear and Intimidation',
    'l': 'Liking',
    'u': 'Urgency and Scarcity',
    't': 'Pretext and Trust',
    'r': 'Reciprocity',
    'c': 'Consistency',
    's': 'Social Proof'
    }

    PT_DEFINITIONS = {
    'a': 'People tend to obey authorities. People trust credible individuals.',
    'p': 'Visceral triggers of desire that override rationality.',
    'f': 'Creating fear of negative consequences (e.g., arrest, data leak).',
    'l': 'Preference for saying "yes" to requests of people they know and like. People are programmed to like others who like them back and who are similar to them.',
    'u': 'Sense of urgency and scarcity assign more value to items.',
    't': 'Scammer makes up story to add source credibility and gain victim\'s trust. The scam message often includes partial personal details to seem plausible.',
    'r': 'Tendency to feel obliged to repay favors from others. "I do something for you, you do something for me."',
    'c': 'Tendency to behave in a way consistent with past decisions and behaviors.',
    's': 'Tendency to reference the behavior of others, using the majority behavior to guide their own actions.'
    }

    PT_EXAMPLES = {
    'a': 'Following the newest online screening introduced by The Bureau of Human Resources, you are required to download the Zoom app',
    'c': 'You agreed to the terms and conditions before using our service, so we ask you to stop all activities that violate them. Click here to unflag your account.',   
    'f': 'You will be arrested. Your data will be leaked.',
    'l': 'I am always available to help, and it\'s my pleasure to answer any questions you may have.',
    'p': 'Your phone Number was randomly selected from the US and Canada Numbers database and you have won $18,087.71',
    'r': 'While we work hard to keep our network secure, we\'re asking you to help us keep your account safe.',
    's': 'Your resume has been recommended by many online recruitment companies.',
    't': 'Your area code 555-XXX suggests you are eligible for this local program.',
    'u': 'We are currently in urgent need of 100 employees. Our hiring team decided that you are qualified for the position.',
    }

    prediction = " "  # start with no prediction
    prediction_labels = " "
    predict_prob = " "
    predict_prob_dict = " "
    if request.method == "POST":    # if user submits the form, this runs
        user_input = request.form["scam_text"]  # get the user input from the html form
        prediction = pipeline.predict([user_input])  # give the model the user input and get PTs as output
        predict_prob = pipeline.predict_proba([user_input])
        predict_prob_percent = [round(i*100, 2) for i in predict_prob[0]]
        predict_prob_dict = {'a':predict_prob_percent[0],
                             'p':predict_prob_percent[1],
                             'f':predict_prob_percent[2],
                             'l':predict_prob_percent[3],
                             'u':predict_prob_percent[4],
                             't':predict_prob_percent[5],
                             'r':predict_prob_percent[6],
                             'c':predict_prob_percent[7],
                             's':predict_prob_percent[8],
                             }
        prediction_labels = [label for label, val in zip(PT_FULL_NAMES, prediction[0]) if val == 1]
        
    return render_template("index.html", prediction_labels = prediction_labels, predict_prob = predict_prob, PT_FULL_NAMES = PT_FULL_NAMES, PT_DEFINITIONS = PT_DEFINITIONS, PT_EXAMPLES = PT_EXAMPLES, predict_prob_dict = predict_prob_dict )   # return the predictions to the html

if __name__ == "__main__":
    app.run(debug=True, port = 5001)