from flask import Flask, request
from random import choice, sample

app = Flask(__name__)

horscopes = ["Virgo: Go see a movie today. It’s a great escape! Especially from all this pollution and dangerous UV radiation! Say, is that mole new?",
             "Libra: Your dreams will be filled with prophetic visions. Write them down. Hopefully, there are some lottery numbers or sports scores in there!", "Scorpio:  Curse you. Curse your family! Curse your children! And your children's  children! Vile, vile Scorpio.", "Sagittarius: Eat well today! You’ve earned it! And by “it,” I mean “massive food allergies”! And by “earned,” I mean “acquired”. I should proof this stuff before I read it out loud. Let’s try that again. “You’ve acquired massive food allergies!” Yes, much cleaner. Eat well!", "Capricorn: Those were not contact lenses you put in this morning. Best not think about this again…", "Aquarius: the white ball will be under the middle shell. Trust the stars. Invest all your money in this lucrative street game.", "Pisces: YOU’VE WON A BRAND NEW CAR!", "Aries: You will feel a haunting sadness about times gone by. Today’s smell is wheat grass and toast.", "Taurus: Today is your annual Crime Day. All Tauruses are exempt from laws today.", "Gemini: You will meet someone today who will have no effect on your life, and who you will immediately forget. Retain hope for a possible future.", "Cancer: “I’ve gotta pay my phone bill, and also get some more milk.” That wasn’t me talking. That is what the stars say today. Interpret it as you will.", "Leo: It’s better that I don’t read this aloud. Better that you not know. Tell your family that you love them."]


@app.route('/')
def index():
    "Show the homepage and ask the user's name."
    return """
    <form action='/horscope'>
        <p>
            What is your name?
            <input type="text" name="name"/>
        </p>
        <p>
            <input type="checkbox" name="show_horscopes"/>
            Show Compliments
        </p>
        <p>
            How many horscopes?
            <select name="num_horscopes">
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
        </p>
        <input type="submit">
    </form>
    """


@app.route('/horscope')
def get_horscope():
    """Give the user a horscope"""
    name = request.args.get('name')
    num_horscopes = int(request.args.get('num_horscopes'))
    show_horscopes = request.args.get('show_horscopes')
    your_horoscope = ', '.join(sample(horscopes, num_horscopes))

    if show_horscopes:
        return f'Hello there, {name}, your Horoscope says: {your_horoscope}!'
    else:
        return f'Hello there, {name}! Have a nice day!'
