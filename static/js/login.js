export function initLogin(){

    const loginForm = document.getElementById("loginForm");

    if(!loginForm){
        return;
    };
    
    loginForm.addEventListener("submit", async function (event){
        event.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        const loginMessage = document.getElementById("loginMessage");

        loginMessage.textContent = "";
        loginMessage.classList.remove("show", "success");
        
        try{

            const response = await fetch("/api/login", {
                method : "POST",
                headers : {
                    "Content-Type": "application/json"
                },
                body : JSON.stringify({
                    email : email,
                    password : password
                })
            });

            const data = await response.json();

            if(!response.ok){
                loginMessage.textContent = data.message;
                loginMessage.classList.add("show");

                return;
            }

            window.location.href = "/dashboard";

        }catch(error){
            loginMessage.textContent = error.message;
        }
    });
}