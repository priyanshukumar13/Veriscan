from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Common dictionary words (example list)
common_words = {"password", "123456", "qwerty", "letmein", "welcome", "admin", "user", "test"}

def analyze_password(password):
    length = len(password)
    cracking_time = estimate_cracking_time(password)

    # Check if the password contains common words
    word_analysis = any(word in password.lower() for word in common_words)

    # Character variety check
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password)

    character_variety = []
    if has_upper:
        character_variety.append("Uppercase Letters")
    if has_lower:
        character_variety.append("Lowercase Letters")
    if has_digit:
        character_variety.append("Numbers")
    if has_special:
        character_variety.append("Special Characters")

    return {
        "length": length,
        "cracking_time": cracking_time,
        "word_analysis": "Contains common word" if word_analysis else "No common words found",
        "character_variety": ", ".join(character_variety) if character_variety else "None"
    }

def estimate_cracking_time(password):
    complexity = 0

    if any(c.islower() for c in password):
        complexity += 26
    if any(c.isupper() for c in password):
        complexity += 26
    if any(c.isdigit() for c in password):
        complexity += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password):
        complexity += 30

    if complexity == 0:
        return "Instantly cracked"

    possible_combinations = complexity ** len(password)
    estimated_seconds = possible_combinations / (10**9)  # Assuming a billion guesses per second

    if estimated_seconds < 60:
        return "Less than a minute"
    elif estimated_seconds < 3600:
        return f"{int(estimated_seconds // 60)} minutes"
    elif estimated_seconds < 86400:
        return f"{int(estimated_seconds // 3600)} hours"
    elif estimated_seconds < 31536000:
        return f"{int(estimated_seconds // 86400)} days"
    else:
        return f"{int(estimated_seconds // 31536000)} years"

@app.route('/')
def home():
    return render_template('newindex.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')

    if not password:
        return jsonify({"error": "No password provided"}), 400

    result = analyze_password(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# @app.route('/')  # Add this line to handle root URL
# def home():
#     return render_template('newindex.html')  # Ensure 'index.html' exists inside the 'templates' folder

# @app.route('/check_password', methods=['POST'])
# def check_password():
#     data = request.get_json()
#     password = data.get('password', '')

#     if not password:
#         return jsonify({"error": "No password provided"}), 400

#     # Password analysis logic here
#     result = {"message": "Password processed"}  # Replace with your analysis function
#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)
