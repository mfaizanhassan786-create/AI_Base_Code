
#              5 AI-Based Python Examples



# Example 1: Simple Chatbot (Rule-Based AI)

# This is a basic chatbot that responds based on keywords
# found in the user's input. This is the simplest form of AI
# where the program "understands" what you say using rules.

print("=" * 50)
print("  Example 1: Simple AI Chatbot")
print("=" * 50)

def chatbot(user_input):
    """A simple rule-based chatbot that responds to keywords."""
    user_input = user_input.lower()  # Convert to lowercase for easier matching

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today? 😊"
    elif "your name" in user_input:
        return "I am a simple AI chatbot built with Python! 🤖"
    elif "weather" in user_input:
        return "I can't check real weather, but I hope it's sunny! ☀️"
    elif "joke" in user_input:
        return "Why did the programmer quit? Because he didn't get arrays (a raise)! 😄"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day! 👋"
    else:
        return "I'm not sure I understand. Can you try asking something else?"

# Test the chatbot
test_messages = ["Hello", "What is your name?", "Tell me a joke", "Goodbye"]
for msg in test_messages:
    print(f"You:  {msg}")
    print(f"Bot:  {chatbot(msg)}")
    print()


# 
# Example 2: AI Number Guesser (Binary Search Algorithm)
# 
# The AI guesses your number using a smart strategy called
# "binary search" — it always guesses the middle number to
# eliminate half the possibilities each time!

print("\n" + "=" * 50)
print("  Example 2: AI Number Guesser")
print("=" * 50)

def ai_number_guesser(secret_number, low=1, high=100):
    """AI guesses a number between low and high using binary search."""
    attempts = 0

    print(f"🤔 AI is trying to guess the number: {secret_number}")
    print(f"   Range: {low} to {high}\n")

    while low <= high:
        guess = (low + high) // 2  # AI picks the middle number
        attempts += 1

        if guess == secret_number:
            print(f"   Attempt {attempts}: AI guesses {guess} ✅ CORRECT!")
            print(f"   🎉 AI found the number in {attempts} attempts!")
            return attempts
        elif guess < secret_number:
            print(f"   Attempt {attempts}: AI guesses {guess} ⬆️ Too low!")
            low = guess + 1
        else:
            print(f"   Attempt {attempts}: AI guesses {guess} ⬇️ Too high!")
            high = guess - 1

    return attempts

# Test: AI guesses the number 73
ai_number_guesser(73)


# 
# Example 3: Sentiment Analyzer (Text Classification AI)
# 
# This AI analyzes text to determine if it's positive,
# negative, or neutral based on keyword matching.
# Real AI uses machine learning, but this shows the concept!

print("\n" + "=" * 50)
print("  Example 3: AI Sentiment Analyzer")
print("=" * 50)

def analyze_sentiment(text):
    """Analyze the sentiment of a given text using keyword matching."""
    positive_words = [
        "good", "great", "awesome", "excellent", "happy",
        "love", "amazing", "wonderful", "fantastic", "best",
        "beautiful", "perfect", "brilliant", "superb", "enjoy"
    ]
    negative_words = [
        "bad", "terrible", "awful", "horrible", "sad",
        "hate", "worst", "ugly", "boring", "poor",
        "angry", "disappointed", "disgusting", "annoying", "fail"
    ]

    text_lower = text.lower()
    words = text_lower.split()

    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    # Calculate sentiment score
    total = positive_count + negative_count
    if total == 0:
        sentiment = "Neutral 😐"
        score = 0
    elif positive_count > negative_count:
        sentiment = "Positive 😊"
        score = positive_count / total * 100
    elif negative_count > positive_count:
        sentiment = "Negative 😞"
        score = -(negative_count / total * 100)
    else:
        sentiment = "Mixed 🤔"
        score = 0

    return sentiment, score

# Test with different sentences
sentences = [
    "This movie is amazing and wonderful!",
    "I hate this terrible and boring show.",
    "The weather is okay today.",
    "I love the great food but the service was awful.",
    "This is the best and most fantastic day ever!"
]

for sentence in sentences:
    sentiment, score = analyze_sentiment(sentence)
    print(f"   📝 \"{sentence}\"")
    print(f"      → Sentiment: {sentiment}  (Score: {score:.0f}%)")
    print()


# Example 4: AI Recommendation System
# 
# This AI recommends movies based on what genre you like.
# Real recommendation systems (like Netflix & YouTube) use
# similar logic but with much more data and machine learning!

print("\n" + "=" * 50)
print("  Example 4: AI Movie Recommendation System")
print("=" * 50)

def recommend_movies(favorite_genre):
    """Recommend movies based on the user's favorite genre."""
    movie_database = {
        "action": [
            {"title": "The Dark Knight", "rating": 9.0},
            {"title": "Mad Max: Fury Road", "rating": 8.1},
            {"title": "John Wick", "rating": 7.4},
            {"title": "Inception", "rating": 8.8},
        ],
        "comedy": [
            {"title": "The Grand Budapest Hotel", "rating": 8.1},
            {"title": "Superbad", "rating": 7.6},
            {"title": "The Hangover", "rating": 7.7},
            {"title": "Bridesmaids", "rating": 6.8},
        ],
        "sci-fi": [
            {"title": "Interstellar", "rating": 8.7},
            {"title": "The Matrix", "rating": 8.7},
            {"title": "Blade Runner 2049", "rating": 8.0},
            {"title": "Arrival", "rating": 7.9},
        ],
        "horror": [
            {"title": "Get Out", "rating": 7.7},
            {"title": "A Quiet Place", "rating": 7.5},
            {"title": "The Conjuring", "rating": 7.5},
            {"title": "Hereditary", "rating": 7.3},
        ],
    }

    genre = favorite_genre.lower()

    if genre in movie_database:
        movies = movie_database[genre]
        # Sort by rating (highest first) — AI picks the best!
        movies_sorted = sorted(movies, key=lambda m: m["rating"], reverse=True)

        print(f"\n   🎬 Top {genre.title()} Movie Recommendations:\n")
        for i, movie in enumerate(movies_sorted, 1):
            stars = "⭐" * int(movie["rating"] // 2)
            print(f"      {i}. {movie['title']} — Rating: {movie['rating']} {stars}")
    else:
        available = ", ".join(movie_database.keys())
        print(f"   ❌ Genre '{genre}' not found.")
        print(f"   Available genres: {available}")

# Test recommendations
recommend_movies("sci-fi")
print()
recommend_movies("action")


# 
# Example 5: AI Password Strength Checker
# ────────────────────────────────────────────────────────────
# This AI evaluates how strong a password is by checking
# various security criteria like length, uppercase letters,
# numbers, and special characters.

print("\n" + "=" * 50)
print("  Example 5: AI Password Strength Checker")
print("=" * 50)

def check_password_strength(password):
    """AI-based password strength checker."""
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 3
        feedback.append("✅ Great length (12+ characters)")
    elif len(password) >= 8:
        score += 2
        feedback.append("⚠️  Good length (8+ characters)")
    else:
        score += 0
        feedback.append("❌ Too short (less than 8 characters)")

    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 2
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ No uppercase letters")

    # Check for lowercase letters
    if any(c.islower() for c in password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ No lowercase letters")

    # Check for numbers
    if any(c.isdigit() for c in password):
        score += 2
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ No numbers found")

    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
    if any(c in special_chars for c in password):
        score += 2
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ No special characters")

    # Determine overall strength
    if score >= 9:
        strength = "🟢 STRONG"
    elif score >= 6:
        strength = "🟡 MEDIUM"
    else:
        strength = "🔴 WEAK"

    return strength, score, feedback

# Test with different passwords
test_passwords = [
    "abc",
    "hello123",
    "MyPassword",
    "Str0ng#Pass!2025",
    "AI@Python#99!"
]

for pwd in test_passwords:
    strength, score, feedback = check_password_strength(pwd)
    print(f"\n   🔑 Password: \"{pwd}\"")
    print(f"      Strength: {strength} (Score: {score}/10)")
    for tip in feedback:
        print(f"      {tip}")

print("\n" + "=" * 50)
print("  ✅ All 5 AI Examples Complete!")
print("=" * 50)
