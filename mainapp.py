from flask import Flask,request,render_template
import paralleldots
import json

paralleldots.set_api_key("2NjNqDqC7FT8PROZuQEQH0cFWouKcLay7HcNYGWbhNo")
paralleldots.get_api_key()

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if (request.method=="POST"):
        all_comments=request.form.get('test')
        all_comments=json.loads(all_comments)
        videoId=[]
        isGood=0
        for dictionary in all_comments:
            neither_count=0
            for i in dictionary["videoComments"]:
                k=paralleldots.abuse(i)
                neither_count+=k['neither']
                if(neither_count>isGood):
                    isGood=neither_count
                    if(dictionary["video-id"] not in videoId):
                        videoId.append(dictionary["video-id"])
                    print(isGood)
        return render_template('final.html',videoId=videoId)
    return render_template('newproject.html')


app.run(debug=True)
