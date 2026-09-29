document.addEventListener("DOMContentLoaded", function () {

    // ============================================================
    // Password elements
    // ============================================================

    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("passwordR");

    const passwordStrength =
        document.getElementById("passwordStrength");

    const passwordError =
        document.getElementById("passwordError");


    // ============================================================
    // Calculate password strength
    // ============================================================

    function passScore(password) {

        let score = 0;

        // Length
        if (password.length >= 8) {
            score++;
        }

        if (password.length >= 12) {
            score++;
        }

        // Lowercase
        if (/[a-z]/.test(password)) {
            score++;
        }

        // Uppercase
        if (/[A-Z]/.test(password)) {
            score++;
        }

        // Number
        if (/[0-9]/.test(password)) {
            score++;
        }

        // Special character
        if (/[^A-Za-z0-9]/.test(password)) {
            score++;
        }

        return score;
    }


    // ============================================================
    // Update password strength
    // ============================================================

    function updatePasswordStrength() {

        if (!passwordInput || !passwordStrength) {
            return;
        }

        const password = passwordInput.value;

        // Remove previous strength class
        passwordStrength.classList.remove(
            "weak",
            "medium",
            "strong"
        );

        // Nothing entered
        if (password.length === 0) {
            passwordStrength.textContent = "";
            return;
        }

        const score = passScore(password);


        // Weak
        if (score <= 2) {

            passwordStrength.textContent = "Weak";
            passwordStrength.classList.add("weak");

        }

        // Medium
        else if (score <= 4) {

            passwordStrength.textContent = "Medium";
            passwordStrength.classList.add("medium");

        }

        // Strong
        else {

            passwordStrength.textContent = "Strong";
            passwordStrength.classList.add("strong");
        }
    }


    // ============================================================
    // Check whether passwords match
    // ============================================================

    function checkPasswords() {

        if (
            !passwordInput ||
            !confirmPasswordInput ||
            !passwordError
        ) {
            return true;
        }


        // Don't show an error if confirmation is empty
        if (confirmPasswordInput.value === "") {

            passwordError.textContent = "";

            return true;
        }


        // Passwords match
        if (
            passwordInput.value ===
            confirmPasswordInput.value
        ) {

            passwordError.textContent = "";

            return true;
        }


        // Passwords don't match
        passwordError.textContent =
            "Passwords do not match.";

        return false;
    }


    // ============================================================
    // Show / Hide password
    // ============================================================

    function setupPasswordToggles() {

        const passwordContainers =
            document.querySelectorAll(".password-container");


        passwordContainers.forEach(function (container) {

            const input =
                container.querySelector("input");

            const button =
                container.querySelector(".password-toggle");


            // Make sure both elements exist
            if (!input || !button) {
                return;
            }


            button.addEventListener("click", function () {

                if (input.type === "password") {

                    input.type = "text";

                    button.textContent = "Hide";

                }

                else {

                    input.type = "password";

                    button.textContent = "Show";
                }

            });

        });
    }

    // ============================================================
    // Dark / Light Mode
    // ============================================================

    const themeToggle =
        document.getElementById("themeToggle");


    // ============================================================
    // Update theme toggle
    // ============================================================

    function updateThemeButton() {

        if (!themeToggle) {
            return;
        }

        const isLight =
            document.body.classList.contains("light");

        themeToggle.textContent =
            isLight ? "Dark Mode" : "Light Mode";
    }


    // ============================================================
    // Load saved theme
    // ============================================================

    function loadTheme() {

        const savedTheme =
            localStorage.getItem("theme");

        if (savedTheme === "light") {

            document.body.classList.add("light");

        }
        else {

            document.body.classList.remove("light");

        }

        updateThemeButton();
    }


    // ============================================================
    // Toggle dark / light mode
    // ============================================================

    function toggleTheme() {

        document.body.classList.toggle("light");

        const isLight =
            document.body.classList.contains("light");

        localStorage.setItem(
            "theme",
            isLight ? "light" : "dark"
        );

        updateThemeButton();
    }


    // ============================================================
    // Event listeners
    // ============================================================

    if (themeToggle) {

        themeToggle.addEventListener(
            "click",
            toggleTheme
        );
    
    }
    
    
    // ============================================================
    // Start theme
    // ============================================================
    
    loadTheme();

    if (passwordInput) {

        passwordInput.addEventListener(
            "input",
            updatePasswordStrength
        );

        passwordInput.addEventListener(
            "input",
            checkPasswords
        );
    }


    if (confirmPasswordInput) {

        confirmPasswordInput.addEventListener(
            "input",
            checkPasswords
        );
    }


    // ============================================================
    // Prevent form submission if passwords don't match
    // ============================================================

    const signupForm =
        document.getElementById("signupForm");


    if (signupForm) {

        signupForm.addEventListener(
            "submit",
            function (event) {

                if (!checkPasswords()) {

                    event.preventDefault();

                    if (confirmPasswordInput) {
                        confirmPasswordInput.focus();
                    }
                }

            }
        );
    }


    // ============================================================
    // Start password toggles
    // ============================================================

    setupPasswordToggles();

});
