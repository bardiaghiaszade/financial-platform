export function initResetPassword(){

    const resetPasswordForm =
        document.getElementById(
            "resetPasswordForm"
        );

    if(!resetPasswordForm){
        return;
    }

    resetPasswordForm.addEventListener(
        "submit",
        async function(event){

            event.preventDefault();

            const password =
                document.getElementById(
                    "password"
                ).value;

            const passwordRepeat =
                document.getElementById(
                    "newPasswordR"
                ).value;

            const passwordError =
                document.getElementById(
                    "passwordError"
                );

            const resetPasswordMessage =
                document.getElementById(
                    "resetPasswordMessage"
                );

            passwordError.textContent = "";
            resetPasswordMessage.textContent = "";

            if(password !== passwordRepeat){

                passwordError.textContent =
                    "Passwords do not match.";

                return;
            }

            if(password.length < 8){

                passwordError.textContent =
                    "Password must be at least 8 characters.";

                return;
            }

            try{

                const response = await fetch(
                    "/api/reset-password",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            password: password
                        })
                    }
                );

                const data =
                    await response.json();

                if(!response.ok){

                    resetPasswordMessage.textContent =
                        data.message;

                    return;
                }

                resetPasswordMessage.textContent =
                    data.message;

                resetPasswordMessage.classList.add(
                    "show",
                    "success"
                );

                setTimeout(() => {

                    window.location.href =
                        "/login";

                }, 1500);

            }catch(error){

                resetPasswordMessage.textContent =
                    error.message;
            }
        }
    );
}