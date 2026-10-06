function passScore(password) {
    let score = 0;

    if (password.length >= 8) {score++;}

    if (password.length >= 12) {score++;}

    if (/[a-z]/.test(password)) {score++;}

    if (/[A-Z]/.test(password)) {score++;}

    if (/[0-9]/.test(password)) {score++;}

    if (/[^A-Za-z0-9]/.test(password)) {score++;}

    return score;
}


function setupPasswordStrength(passwordInput, passwordStrength) {

    if (!passwordInput || !passwordStrength) {
        return;
    }

    passwordInput.addEventListener("input", function () {

        const password = passwordInput.value;

        passwordStrength.classList.remove(
            "weak",
            "medium",
            "strong"
        );

        if (password.length === 0) {
            passwordStrength.textContent = "";
            return;
        }

        const score = passScore(password);

        if (score <= 2) {

            passwordStrength.textContent = "Weak";
            passwordStrength.classList.add("weak");

        } else if (score <= 4) {

            passwordStrength.textContent = "Medium";
            passwordStrength.classList.add("medium");

        } else {

            passwordStrength.textContent = "Strong";
            passwordStrength.classList.add("strong");
        }
    });
}


function setupPasswordMatch(passwordInput, confirmPasswordInput, passwordError
) {
    if (!passwordInput || !confirmPasswordInput || !passwordError) {
        return;
    }

    function checkPasswords() {

        if (confirmPasswordInput.value === "") {
            passwordError.textContent = "";
            return true;
        }

        if (passwordInput.value === confirmPasswordInput.value) {
            passwordError.textContent = "";
            return true;
        }

        passwordError.textContent = "Passwords do not match.";

        return false;
    }

    passwordInput.addEventListener("input", checkPasswords);

    confirmPasswordInput.addEventListener("input", checkPasswords);

    return checkPasswords;
}


function setupPasswordToggles() {

    const passwordContainers = document.querySelectorAll(".password-container");

    passwordContainers.forEach(function (container) {

        const input = container.querySelector("input");

        const button = container.querySelector(".password-toggle");

        if (!input || !button) {
            return;
        }

        button.addEventListener("click", function () {

            const isPassword = input.type === "password";

            input.type = isPassword ? "text" : "password";

            button.textContent = isPassword ? "Hide" : "Show";
        });
    });
}


function setupSignupForm(passwordInput, confirmPasswordInput) {

    const signupForm = document.getElementById("signupForm");

    if (!signupForm) {
        return;
    }

    signupForm.addEventListener("submit",function (event) {

            if (
                passwordInput &&
                confirmPasswordInput &&
                passwordInput.value !==
                confirmPasswordInput.value
            ) {
                event.preventDefault();

                confirmPasswordInput.focus();
            }
        }
    );
}


export function initPassword() {

    const passwordInput = document.getElementById("password");

    const confirmPasswordInput = document.getElementById("passwordR");

    const passwordStrength = document.getElementById("passwordStrength");

    const passwordError = document.getElementById("passwordError");

    setupPasswordStrength(passwordInput, passwordStrength);

    setupPasswordMatch(passwordInput, confirmPasswordInput, passwordError);

    setupPasswordToggles();

    setupSignupForm(passwordInput, confirmPasswordInput);
}
