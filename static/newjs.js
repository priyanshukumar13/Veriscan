function checkPassword() {
    const password = document.getElementById("password").value;

    // Update length feedback immediately
    document.getElementById("length-feedback").innerText = password.length;

    if (password.length === 0) {
        return;
    }

    fetch('/check_password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("crack-time").innerText = data.crack_time;
        document.getElementById("length-advice").innerText = data.length_advice;
        document.getElementById("word-feedback").innerText = data.word_feedback;
        document.getElementById("word-advice").innerText = data.word_advice;
        document.getElementById("variety-feedback").innerText = data.variety_feedback;
        document.getElementById("variety-advice").innerText = data.variety_advice;
    })
    .catch(error => console.error("Error:", error));
}


document.getElementById('password').addEventListener('input', function() {
    const password = this.value;
    const crackTimeText = document.getElementById('time-to-crack');
    const lengthFeedback = document.getElementById('length-feedback');
    const wordFeedback = document.getElementById('word-feedback');
    const varietyFeedback = document.getElementById('variety-feedback');

    let crackTime = calculateCrackTime(password);
    let lengthDesc = getLengthFeedback(password);
    let wordDesc = checkDictionaryWord(password);
    let varietyDesc = checkVariety(password);

    crackTimeText.textContent = crackTime;
    lengthFeedback.innerHTML = `<strong>Length:</strong> ${lengthDesc}`;
    wordFeedback.innerHTML = `<strong>Possibly a word:</strong> ${wordDesc}`;
    varietyFeedback.innerHTML = `<strong>Character Variety:</strong> ${varietyDesc}`;
});

// Function to estimate password crack time
function calculateCrackTime(password) {
    let timeToCrack;
    if (password.length < 5) timeToCrack = "2 microseconds";
    else if (password.length < 8) timeToCrack = "a few seconds";
    else if (password.length < 12) timeToCrack = "a few minutes";
    else if (password.length < 16) timeToCrack = "several hours";
    else timeToCrack = "several years";

    return timeToCrack;
}

// Function to check password length
function getLengthFeedback(password) {
    if (password.length < 6) return "Very short<br>Your password is very short. The longer a password is, the more secure it will be.";
    if (password.length < 10) return "Short<br>Your password could be longer to increase security.";
    return "Good length<br>Your password length is decent, but adding more characters makes it even stronger.";
}

// Function to check if password looks like a dictionary word
function checkDictionaryWord(password) {
    const dictionaryWords = ["password", "hello", "admin", "welcome", "12345", "qwerty", "love"];
    if (dictionaryWords.includes(password.toLowerCase())) {
        return "Your password is a common dictionary word. It can be cracked very quickly.";
    }
    return "Your password doesn’t seem to be a common word. Good!";
}

// Function to check character variety
function checkVariety(password) {
    const hasLetters = /[a-zA-Z]/.test(password);
    const hasNumbers = /\d/.test(password);
    const hasSymbols = /[@$!%*?&]/.test(password);

    if (hasLetters && hasNumbers && hasSymbols) {
        return "Strong<br>Your password contains a good mix of letters, numbers, and symbols.";
    }
    if (hasLetters && hasNumbers) {
        return "Moderate<br>Your password includes letters and numbers. Adding symbols will make it stronger.";
    }
    if (hasLetters) {
        return "Just Letters<br>Your password only contains letters. Adding numbers and symbols can make it more secure.";
    }
    return "Weak<br>Your password lacks variety. Try using a mix of letters, numbers, and symbols.";
}
