from flask import Flask, request  # <-- ADD THIS
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os  # <-- ADD THIS

# Initialize Flask app
app = Flask(__name__)  # <-- ADD THIS

# Get token from environment variables (secure)
TOKEN = os.environ.get('TOKEN', "7666196084:AAH_Wn7kaZEy_-g-EnhN-eEqFf0svH_PAqU")  # <-- MODIFIED
bot = telebot.TeleBot(TOKEN)


workout_videos = {
    # Gym Arms Exercises
    "gym_arms_1": {
        "video": "BAACAgIAAxkBAAKrEmfYuLrSSen5yJxxeTjeUqXDKoy5AAL8cAAC1WfISqqalcfLqH7bNgQ",
        "text": """Curl Bar Exercise

The Curl Bar Exercise targets the biceps 💪, forearms ✋, and triceps 🏋️‍♂️, helping to build arm strength and muscle definition. It’s great for reducing wrist strain compared to straight bar curls.

How to Perform
 1. Grip the curl bar with your palms facing up and elbows close to your body.
 2. Curl the bar up, squeezing your biceps at the top .
 3. Lower the bar slowly to the starting position.

Recommended Sets & Reps
 • Strength: 3-5 sets of 3-6 reps 
 • Hypertrophy: 3-4 sets of 8-12 reps 
 • Endurance: 2-4 sets of 15-20 reps 

For both males and females, aim for 3-4 sets of 8-12 reps for muscle growth. Adjust the weight and reps based on your strength and fitness goals 🏋🏻‍♀️"""  # shortened for space
    },
    "gym_arms_2": {
        "video": "BAACAgIAAxkBAAKrFGfYuOQdUW3VEnHdzuXhIV1YmnfTAAL9cAAC1WfISrkMjgZEDvpVNgQ",
        "text": """The Intermediate Bench Press is a barbell-based exercise that primarily targets the chest 💪, shoulders 🏋️‍♂️, and triceps 💥.

Benefits
✅ Builds strength and muscle in the chest, shoulders, and triceps 💪.
✅ Enhances pushing power ⚡, benefiting performance in other lifts like the overhead press and push-ups.
✅ Can be used to progressively overload for long-term strength gains 📈.

How to Perform
1. Lie flat on a bench with your feet firmly on the ground and hands gripping the bar slightly wider than shoulder-width 🛏️.
2. Lower the bar to your chest, keeping elbows at about a 45-degree angle 🔽.
3. Push the bar back up, extending your arms fully without locking the elbows ⬆️.
4. Control the bar as it lowers back to your chest for each rep 🔄.

Incorporate the Intermediate Bench Press into your routine! 💥"""  # shortened for space
    },

    # Home Arms Exercises
    "home_arms_1": {
        "video": "BAACAgIAAxkBAAKq5GfYssEm1orJM7ko-DBSwbS2uxp0AALWcAAC1WfISvQvzaDhx3QJNgQ",
        "text": """Reverse Facing Push-Ups

Reverse Facing Push-Ups are a variation where you perform push-ups with your back facing the floor and your feet elevated. This targets the upper chest, shoulders, and triceps 💪, and adds a greater challenge to the standard push-up.

Benefits

✅ Targets the upper chest and shoulders.
✅ Adds core and stability challenge.
✅ Builds strength and muscle endurance.

How to Perform
 1. Sit on the ground with your feet elevated on a bench or platform.
 2. Place your hands behind you, fingers facing forward.
 3. Lower your body, bending your elbows, and keep your chest facing upward.
 4. Push back up, squeezing your chest at the top.

Recommended Sets & Reps
 • Strength: 3-5 sets of 5-8 reps 
 • Hypertrophy: 3-4 sets of 8-12 reps 
 • Endurance: 2-4 sets of 15-20 reps 

Challenge your upper body! Try Reverse Facing Push-Ups! 💥"""  # shortened
    },
    "home_arms_2": {
        "video": "BAACAgIAAxkBAAKrDmfYt_F1gQPN45n2HW6kwPK_TxScAAL2cAAC1WfISnQqv3zjvvVmNgQ",
        "text": """Archer Push-Ups

Archer Push-Ups are a challenging push-up variation that targets the chest, shoulders, and triceps 💪, while also improving arm strength and stability. They involve one arm doing more of the work, similar to an archer drawing a bow.

Benefits

✅ Increases chest and shoulder strength.
✅ Improves arm strength and stability.
✅ Great for muscle endurance.

How to Perform
 1. Start in a wide push-up position with one arm extended out to the side.
 2. Lower your body, keeping one arm straight and the other bent.
 3. Push back up, focusing on using the bent arm to lift your body.
 4. Alternate sides for each rep.

Recommended Sets & Reps
 • Strength: 3-5 sets of 5-8 reps
 • Hypertrophy: 3-4 sets of 8-12 reps 
 • Endurance: 2-4 sets of 15-20 reps 

Want to challenge your upper body? Add Archer Push-Ups to your routine! 💥."""  # shortened
    },
    "home_arms_3": {
        "video": "BAACAgIAAxkBAAKrEGfYuC3sDJFOBpwRGzDPuDhuUrWBAAL3cAAC1WfISunTUvpIq7tTNgQ",
        "text": """Reverse Grip Push-Ups

Reverse Grip Push-Ups target the upper chest, shoulders, triceps 💪, and forearms for improved stability. This variation shifts focus for a more complete push-up routine.

Benefits

✅ Targets the upper chest and shoulders 
✅ Engages forearms and improves stability
✅ Builds strength and muscle endurance 

How to Perform
 1. Set hands in a reverse grip (palms facing up)
 2. Lower body while keeping elbows at a 45-degree angle 
 3. Push back up, squeezing your chest at the top
 4. Control the descent 

Recommended Sets & Reps
 • Strength: 3-5 sets of 5-8 reps 
 • Hypertrophy: 3-4 sets of 10-12 reps 
 • Endurance: 2-4 sets of 15-20 reps 

Ready to boost your chest and shoulder strength? Add Reverse Grip Push-Ups! 💥"""  # shortened
    }, 
    # Gym Legs Exercises
    "gym_legs_1": {
        "video": "BAACAgIAAxkBAAKrFmfYuV9NsZMBXChrAaVZ6XaZojMYAAL_cAAC1WfISppNNditM1vzNgQ",
        "text": """Stationary Bike (Indoor Cycle)

The stationary bike targets the legs, specifically the quadriceps, hamstrings, and calves 🚴. It’s an excellent low-impact exercise for strengthening and toning your lower body while improving leg endurance.

Benefits
✅ Builds quadriceps, hamstrings, and calves 💪.
✅ Improves leg endurance without putting strain on the joints 🦵.
✅ Great for toning and shaping the lower body 🔥.

How to Perform
1. Set the bike to a comfortable resistance level 🚴‍♂️.
2. Start pedaling at a moderate pace, focusing on engaging your legs throughout the movement 🔄.
3. Maintain the pace for 20-30 minutes for optimal leg training ⏱️.

Recommended Time
• Leg Endurance: 20-30 minutes at a steady pace 🕒

Want stronger legs? Add the stationary bike to your workout routine! 💥"""
     },
    "gym_legs_2": {
        "video": "BAACAgIAAxkBAAKrGGfYuYIc8lpPdVmLOQkn5Lo80omYAAL-cAAC1WfISmk092XnAAFXZDYE",
        "text": """Walking Incline on the Treadmill

Walking on an incline treadmill targets the legs, specifically the quadriceps, hamstrings, and glutes 🍑. The incline increases the intensity, helping to tone and strengthen the lower body.

Benefits
✅ Builds stronger legs and glutes 💥.
✅ Improves leg endurance and muscle tone 🦵.
✅ Reduces joint strain compared to running 🏃‍♂️.

How to Perform
1. Set the treadmill to an incline (5-15%) and start walking at a moderate pace 🏃‍♀️.
2. Keep your posture upright and engage your legs throughout the movement 🦵.
3. Maintain the incline for 20-30 minutes for optimal leg training ⏱️.

Recommended Time
• Leg Endurance: 20-30 minutes at a moderate pace 🕒

Boost your leg strength! Incorporate Walking Incline Treadmill into your workout! 💥"""
    },
    # New Home Legs Exercises
    "home_legs_1": {
        "video": "BAACAgIAAxkBAAKrHmfYuk8HoIAQHScRI2BLNU0YqwQRAAIBcQAC1WfISt-bAAFixdBXRzYE",
        "text": """Standard Forward Lunge

The standard forward lunge targets the glutes, quadriceps, and hamstrings 🍑. This classic exercise is great for building strength, improving balance, and toning the lower body.

Benefits

✅ Strengthens glutes, quadriceps, and hamstrings 💥.
✅ Improves balance and core stability 🦵.
✅ Excellent for lower body strength and muscle toning 🔥.

How to Perform
 1. Stand with feet hip-width apart 🏋️‍♀️.
 2. Step one leg forward, lowering your body until both knees are at 90-degree angles 🔽.
 3. Push off the front foot to return to the starting position ⬆️.
 4. Alternate legs for each rep 🔄.

Recommended Sets & Reps
 • Strength: 3-5 sets of 8-10 reps per leg 🔥
 • Hypertrophy: 3-4 sets of 12-15 reps per leg 💥

Want to build stronger legs? Add the Standard Forward Lunge to your workout! 💥"""
    },
    "home_legs_2": {
        "video": "BAACAgIAAxkBAAKrHGfYui-GiIW0kiN2Xe-EO6F8uy2VAANxAALVZ8hKDM3NFyhmug42BA",
        "text": """Side Lunge

The side lunge primarily targets the glutes, quadriceps, and hamstrings, while also engaging the inner thighs 🍑. This movement focuses on lateral leg strength and flexibility, helping improve balance and stability.

Benefits

✅ Strengthens glutes, quadriceps, and hamstrings 💥.
✅ Tones the inner thighs and improves balance 🦵.
✅ Great for lower body strength and mobility 🔥.

How to Perform
 1. Stand with feet hip-width apart 🏋️‍♀️.
 2. Step one leg out to the side, lowering your body into a lunge position with the other leg straight 🔽.
 3. Push back up to the starting position, keeping your chest lifted ⬆️.
 4. Alternate sides for each rep 🔄.

Recommended Sets & Reps
 • Strength: 3-5 sets of 8-10 reps per leg 🔥
 • Hypertrophy: 3-4 sets of 12-15 reps per leg 💥

Want to target your lower body and enhance mobility? Add the Side Lunge to your workout! 💥"""
     }, 
     "home_legs_3": {
        "video": "BAACAgIAAxkBAAKrIGfYum6aFL0cYiBoPUMAAX85RB_fXAACAnEAAtVnyEpzOnfiqQnJuzYE",
        "text": """Curtsy Lunge

The curtsy lunge targets the glutes, quadriceps, and hamstrings 🍑 while also improving balance and stability. This variation of the lunge adds a lateral movement, making it great for toning the legs and shaping the lower body.

Benefits

✅ Strengthens glutes, quadriceps, and hamstrings 💥.
✅ Improves balance and stability 🦵.
✅ Great for toning and shaping the legs �.

How to Perform
 1. Stand with your feet hip-width apart 🏋️‍♀️.
 2. Step one leg diagonally behind you, lowering your body into a lunge position 🔽.
 3. Push back up to the starting position, keeping your torso upright ⬆️.
 4. Alternate legs for each rep 🔄.

Recommended Sets & Reps
 • Strength: 3-5 sets of 8-10 reps per leg 🔥
 • Hypertrophy: 3-4 sets of 12-15 reps per leg 💥

Want to shape your legs and glutes? Try the Curtsy Lunge! 💥"""
    }, 
    # Home Abs Exercises
    "home_abs_1": {
        "video": "BAACAgIAAxkBAAKrKGfYvVV1a47kEAa51J9x1GMgQJY9AAIJcQAC1WfISpaXsKNpwK0KNgQ",
        "text": """Crunch

The crunch is a classic core exercise targeting the abdominal muscles. It's great for building core strength and endurance.

How to Perform:
1. Lie on your back with knees bent
2. Place hands behind your head
3. Lift shoulder blades off the ground
4. Slowly lower back down

Sets: 3-4 sets of 15-20 reps"""
    },
    "home_abs_2": {
        "video": "BAACAgIAAxkBAAKrKmfYvXCbrobhNYEQUkT_Ge-NM8SoAAIKcQAC1WfISg-xy-HuB-hkNgQ",
        "text": """Heel Touch

Heel touches target the obliques and lower abs, improving core stability.

How to Perform:
1. Lie on back with knees bent
2. Reach hands toward heels alternately
3. Keep shoulders off the ground
4. Engage core throughout

Sets: 3 sets of 20 reps (10 per side)"""
    },
    "home_abs_3": {
        "video": "BAACAgIAAxkBAAKrJmfYvSc2_wsmvwtBdCyV_ZpZ1MxiAAIIcQAC1WfISuAFIS-rxxWjNgQ",
        "text": """Side Crunch

Targets oblique muscles for a stronger core and better waist definition.

How to Perform:
1. Lie on side with legs stacked
2. Place hand behind head
3. Lift upper body toward hips
4. Control the movement

Sets: 3 sets of 15 reps per side"""
    },

    # Gym Abs Exercises
    "gym_abs_1": {
        "video": "BAACAgIAAxkBAAKrJGfYvQ6GP22U254AAUVnRSIrsr8WPAACB3EAAtVnyEqNSpOk2XXRLjYE",
        "text": """Weighted Dead Bug

Advanced core exercise using weights for increased resistance.

How to Perform:
1. Lie on back holding weight plate
2. Raise legs to table position
3. Slowly lower opposite arm/leg
4. Keep core engaged

Sets: 3-4 sets of 10-12 reps"""
    },
    "gym_abs_2": {
        "video": "BAACAgIAAxkBAAKrImfYvOo5bCZ_SnNjWQGTtwzS2tnMAAIGcQAC1WfISrC67GWKW8pQNgQ",
        "text": """Decline Sit-Ups

Advanced sit-up variation using a decline bench for increased difficulty.

How to Perform:
1. Secure legs on decline bench
2. Perform sit-up with controlled motion
3. Add weight for intensity
4. Focus on slow eccentric

Sets: 3-4 sets of 12-15 reps"""
    },

    # Gym Chest Exercises
    "gym_chest_1": {
        "video": "BAACAgIAAxkBAAKrLGfYvYnCXNg8xnynTo-eKIa8bugRAAILcQAC1WfISpkQvahh8oW0NgQ",
        "text": """Cable Flyes

Cable flyes target the chest muscles, specifically the pectoralis major, helping to build chest strength and definition.

How to Perform:
1. Stand between two cable machines with handles at shoulder height.
2. Grab the handles with palms facing forward.
3. Bring your hands together in front of your chest, squeezing your chest muscles.
4. Slowly return to the starting position.

Sets: 3-4 sets of 10-12 reps"""
    },
    "gym_chest_2": {
        "video": "BAACAgIAAxkBAAKrLmfYvcG527w8Pg4cO9wkRkRYdIduAAIMcQAC1WfISmGqNpGiSC-sNgQ",
        "text": """Pec Deck Machine

The pec deck machine isolates the chest muscles, providing a focused workout for the pectorals.

How to Perform:
1. Sit on the machine with your back flat against the pad.
2. Grip the handles with your elbows slightly bent.
3. Bring your arms together in front of your chest, squeezing your pectorals.
4. Slowly return to the starting position.

Sets: 3-4 sets of 10-12 reps"""
    },

    # Home Chest Exercises
    "home_chest_1": {
        "video": "BAACAgIAAxkBAAKrMmfYvfJOpQABjZrQkBOmFkqncsK5VwACD3EAAtVnyEry_LPX6xJ_mjYE",
        "text": """Arm Circles

Arm circles are a simple yet effective exercise to warm up and engage the chest, shoulders, and arms.

How to Perform:
1. Stand with your arms extended out to the sides at shoulder height.
2. Make small circles with your arms, gradually increasing the size.
3. Perform circles in both clockwise and counterclockwise directions.

Sets: 3 sets of 20-30 seconds"""
    },
    "home_chest_2": {
        "video": "BAACAgIAAxkBAAKrMGfYvdhyiQMblt497iwFhEqRXJqJAAINcQAC1WfISmUkfP0SFuqdNgQ",
        "text": """Isometric Chest Squeeze

The isometric chest squeeze is a static exercise that targets the chest muscles, improving strength and endurance.

How to Perform:
1. Stand with your elbows bent at 90 degrees and palms pressed together in front of your chest.
2. Squeeze your palms together as hard as possible, engaging your chest muscles.
3. Hold for 10-15 seconds, then release.

Sets: 3-4 sets of 10-15 seconds"""
    },
}

# ========== WEBHOOK SETUP ========== #  # <-- NEW SECTION
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    return 'Invalid content type', 403

def set_webhook():
    bot.remove_webhook()
    webhook_url = f'https://github.com/khngrva/yoursweetfitness_bot.git'  # Replace with your actual URL
    bot.set_webhook(url=webhook_url)

# Handlers remain the same until select_exercise
def show_start_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("/exercise"), KeyboardButton("/help"))
    bot.send_message(message.chat.id, 
                    "Welcome to Your Fitness Assistant! What would you like to do? 💪\n"
                    "Choose an option below or use /help for guidance:",
                    reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    show_start_menu(message)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 
                    "I can help you find workouts based on your needs! 💪\n"
                    "Use /exercise to get started.")

@bot.message_handler(commands=['exercise'])
def exercise(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Gym"), KeyboardButton("Home"))
    bot.send_message(message.chat.id, "Where will you be training?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Gym", "Home"])
def workout_location(message):
    location = message.text.lower()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Arms"), KeyboardButton("Legs"), KeyboardButton("Abs"), KeyboardButton("Chest"))
    bot.send_message(message.chat.id, f"Great! What body part do you want to train at {location}?", reply_markup=markup)
    bot.register_next_step_handler(message, lambda m: select_exercise(m, location))

@bot.message_handler(func=lambda message: message.text == "Start Again")
def handle_restart(message):
    exercise(message)

@bot.message_handler(func=lambda message: True, content_types=['text'], priority=10)
def handle_unrecognized(message):
    """Show start menu for any unrecognized messages"""
    show_start_menu(message)

@bot.message_handler(func=lambda message: message.text == "Start New Session 🏋️")
def handle_new_session(message):
    exercise(message)

def select_exercise(message, location):
    body_part = message.text.lower()
    valid_body_parts = ["arms", "legs", "abs", "chest"]
    
    # Validate body part input
    if body_part not in valid_body_parts:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("Arms"), KeyboardButton("Legs"), KeyboardButton("Abs"), KeyboardButton("Chest"))
        bot.send_message(message.chat.id, "Please choose a valid body part from the buttons below 👇", reply_markup=markup)
        bot.register_next_step_handler(message, lambda m: select_exercise(m, location))
        return

    key_prefix = f"{location}_{body_part}"
    
    # Count available exercises dynamically
    exercise_count = sum(1 for key in workout_videos if key.startswith(f"{key_prefix}_"))

    if exercise_count > 0:  # <-- FIX INDENTATION FROM HERE
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [KeyboardButton(f"Exercise {i+1}") for i in range(exercise_count)]
        markup.add(*buttons)
        bot.send_message(message.chat.id, "Which exercise do you want?", reply_markup=markup)
        bot.register_next_step_handler(message, lambda m: send_workout(m, key_prefix))
    else:
        # Send error message and re-prompt for body part
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("Arms"), KeyboardButton("Legs"), KeyboardButton("Abs"), KeyboardButton("Chest"))
        bot.send_message(message.chat.id, 
                        "Sorry, I don't have that workout yet. More coming soon! 😊\n"
                        "Please choose another body part:",
                        reply_markup=markup)
        bot.register_next_step_handler(message, lambda m: select_exercise(m, location))

def send_workout(message, key_prefix):
    try:
        # Extract exercise number from message
        exercise_num = message.text.split()[-1]
        if not exercise_num.isdigit():
            raise ValueError
            
        full_key = f"{key_prefix}_{exercise_num}"
        data = workout_videos[full_key]
        
        # Send description and video
        bot.send_message(message.chat.id, data["text"])
        bot.send_video(message.chat.id, data["video"])
        
        # Continue prompt
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("Yes, Continue"), KeyboardButton("No, Finish"))
        bot.send_message(message.chat.id, "Do you want to continue working out or finish your session?", reply_markup=markup)
        bot.register_next_step_handler(message, lambda m: continue_workout(m, key_prefix.split('_')[0]))

    except (KeyError, ValueError):
        bot.send_message(message.chat.id, "Invalid choice. Please use /exercise to start again.")

def continue_workout(message, location):
    if message.text == "Yes, Continue":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("Arms"), KeyboardButton("Legs"), KeyboardButton("Abs"), KeyboardButton("Chest"))
        bot.send_message(message.chat.id, 
                        f"What body part next at {location.capitalize()}?",
                        reply_markup=markup)
        bot.register_next_step_handler(message, lambda m: select_exercise(m, location))
    elif message.text == "No, Finish":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("Start New Session 🏋️"))
        bot.send_message(message.chat.id, 
                        "Great job completing your workout! 🎉\n"
                        "Ready for another session?",
                        reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Please choose a valid option:")
        bot.register_next_step_handler(message, lambda m: continue_workout(m, location))


if __name__ == '__main__':
    set_webhook()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
