export function initVerifyCode(){

    const verifyCodeForm =
        document.getElementById("verifyCodeForm");

    if(!verifyCodeForm){
        return;
    }

    verifyCodeForm.addEventListener(
        "submit",
        async function(event){

            event.preventDefault();

            const code =
                document.getElementById(
                    "verificationCode"
                ).value;

            const verifyCodeMessage =
                document.getElementById(
                    "verifyCodeMessage"
                );

            verifyCodeMessage.textContent = "";
            verifyCodeMessage.classList.remove(
                "show",
                "success"
            );

            try{

                const response = await fetch(
                    "/api/verify-code",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            code: code
                        })
                    }
                );

                const data =
                    await response.json();

                if(!response.ok){

                    verifyCodeMessage.textContent =
                        data.message;

                    verifyCodeMessage.classList.add(
                        "show"
                    );

                    return;
                }

                verifyCodeMessage.textContent =
                    data.message;

                verifyCodeMessage.classList.add(
                    "show",
                    "success"
                );

                setTimeout(() => {
                    window.location.href =
                        "/recover-pass";
                }, 1000);

            }catch(error){

                verifyCodeMessage.textContent =
                    error.message;

                verifyCodeMessage.classList.add(
                    "show"
                );
            }
        }
    );
}