from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)

horoscopes = ["Virgo: Go see a movie today. It’s a great escape! Especially from all this pollution and dangerous UV radiation! Say, is that mole new?",
              "Libra: Your dreams will be filled with prophetic visions. Write them down. Hopefully, there are some lottery numbers or sports scores in there!", "Scorpio:  Curse you. Curse your family! Curse your children! And your children's  children! Vile, vile Scorpio.", "Sagittarius: Eat well today! You’ve earned it! And by “it,” I mean “massive food allergies”! And by “earned,” I mean “acquired”. I should proof this stuff before I read it out loud. Let’s try that again. “You’ve acquired massive food allergies!” Yes, much cleaner. Eat well!", "Capricorn: Those were not contact lenses you put in this morning. Best not think about this again…", "Aquarius: the white ball will be under the middle shell. Trust the stars. Invest all your money in this lucrative street game.", "Pisces: YOU’VE WON A BRAND NEW CAR!", "Aries: You will feel a haunting sadness about times gone by. Today’s smell is wheat grass and toast.", "Taurus: Today is your annual Crime Day. All Tauruses are exempt from laws today.", "Gemini: You will meet someone today who will have no effect on your life, and who you will immediately forget. Retain hope for a possible future.", "Cancer: “I’ve gotta pay my phone bill, and also get some more milk.” That wasn’t me talking. That is what the stars say today. Interpret it as you will.", "Leo: It’s better that I don’t read this aloud. Better that you not know. Tell your family that you love them."]


@app.route('/')
def index():
    "Show the homepage and ask the user's name."
    return render_template('index.html')


@app.route('/horoscope')
def get_horoscope():
    """Give the user a horoscope"""
    name = request.args.get('name')
    num_horoscopes = int(request.args.get('num_horoscopes'))
    get_horoscope = request.args.get('get_horoscope')
    horoscopes_to_show = sample(horoscopes, num_horoscopes)

    return render_template(
        'horoscopes.html',
        name=name,
        get_horoscopes=get_horoscope, num_horoscopes=num_horoscopes,
        horoscopes=horoscopes_to_show)


if __name__ == '__main__':
    app.run(debug=True)
