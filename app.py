#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


app = Flask(__name__)


# In[3]:


dir(app)


# In[4]:


import joblib



@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print (rate)
        model = joblib.load("DBS_Prediction")
        pred = model.predict([[rate]])
        
        return(render_template("index.html", result=pred))
    else:
        return(render_template("index.html", result="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




