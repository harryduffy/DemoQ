from Song import Song
from config import init
from flask import render_template, request

flask_app, q, sp = init()

@flask_app.route("/", methods=["POST", "GET"])
def queue():

    if request.method == "POST":

        if request.form["return"] == "Clear Queue":
            q.clear_queue()

        elif request.form["return"] == "up-vote":
            print(request.form)
            pass
        elif request.form["return"] == "down-vote":
            pass
            
        else:
            song_name = request.form["song"]

            track = sp.search(q=song_name, type="track", limit=2)
            new_song = Song(track["tracks"]["items"][0]["uri"], song_name)
            q.enqueue(new_song)

    return render_template("queue.html", queue=q)

if __name__ == "__main__":
    flask_app.run(debug=True)


