const signupForm = document.getElementById("signupForm");

if (signupForm) {
    signupForm.addEventListener("submit", function (event) {

        const password = document.getElementById("password").value;
        const passwordR = document.getElementById("passwordR").value;
        const passwordError = document.getElementById("passwordError");

        if (password !== passwordR) {
            event.preventDefault();

            passwordError.textContent = "Passwords do not match";
        } else {
            passwordError.textContent = "";
        }
    });
}


const passwordInput = document.getElementById("password");
const passwordStrength = document.getElementById("passwordStrength");

if(passwordInput && passwordStrength){
    passwordInput.addEventListener("input", function(){

        const passcode = passwordInput.value;

        if(passcode.length === 0){
            passwordStrength.textContent = "";
        }else if(passcode.length < 6){
            passwordStrength.textContent = "Weak";
            passwordStrength.classList.add("weak");

        }else if(passcode.length < 10){
            passwordStrength.textContent = "Medium"
            passwordStrength.classList.add("medium");

        }else{
            passwordStrength.textContent = "Strong";
            passwordStrength.classList.add("strong");
        }
    })
}
