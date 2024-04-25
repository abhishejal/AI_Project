##.py
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np
import smtplib,ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()

#-----------------------------------Config data

class AI_Project():
    
    def __init__(self,complaint):
        self.complaint = complaint

    def load_model(self):
        """this function is used to load the model"""
        with open(r"C:\VS_code practice\NLP_Project\models\tokenizer.pickle", 'rb') as f:
           self.tokenizer = pickle.load(f)

        self.model = load_model(r"C:\VS_code practice\NLP_Project\models\finalized_model.h5")
    
    def get_receiver_email(self,prediction):
        """this function is used to assign the departments to the persons
         and to get the reciver_emails"""
        
        receiver_email = 'ailearner70@gmail.com'  # Assign a default value
    
        if prediction == 0:
            receiver_email = 'abhishejal09@gmail.com'
        elif prediction == 1:
            receiver_email = 'abhishejal09@gmail.com'
        elif prediction == 2:
            receiver_email = 'abhishejal09@gmail.com'
        elif prediction == 3:
            receiver_email = 'abhishejal09@gmail.com'
        elif prediction == 4:
            receiver_email = 'abhishejal09@gmail.com'
        elif prediction == 5:
            receiver_email = 'abhishejal09@gmail.com'
        elif prediction == 6:
            receiver_email = 'abhishejal09@gmail.com'

        return receiver_email
    

    def send_mail(self,receiver_email, message):
        """"
        This function is used to send the mail to the respective department
        """
        self.__init__(super)
        port = 465  # Gmail port
        smtp_server = 'smtp.gmail.com'
        sender_email = os.getenv('Email')  
        sender_password = os.getenv('Password')

        msg = EmailMessage()
        msg['Subject'] = 'Please resolve the complaint as soon as possible'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(message)

        with smtplib.SMTP_SSL(smtp_server, port) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, [receiver_email], msg.as_string())  # Convert msg to string

        print("mail sent")


    def forward_complaint(self, complaint):
        ''''
        This function is used to forward the complaint to the respective department
        '''
        
        self.__init__(super)
        self.load_model()

        tokenized_text = self.tokenizer.texts_to_sequences([complaint])  # Wrap complaint in a list
        padded_text = pad_sequences(tokenized_text, maxlen=500)
        predz = self.model.predict(padded_text)
        self.prediction = int(np.argmax(predz))
        print("prediction is:-", self.prediction)
        print("prediction is:-", type(self.prediction))

        receiver_email = self.get_receiver_email(self.prediction)
        print(receiver_email)
        print(type(receiver_email))

        self.send_mail(receiver_email, complaint)

        return {"message": f"complaint forwarded to the respected department"}

    
if __name__ == "__main__":
    complaint = '''collection account report mine sent 
    affidavit police report stating someone getting medical bills name please delete following account'''
    data = AI_Project(complaint)
    data.forward_complaint(complaint)

