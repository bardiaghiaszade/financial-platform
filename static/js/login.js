export function initLogin(){

    const loginForm = document.getElementById("loginForm");

    if(!loginForm){
        return;
    };
    
    loginForm.addEventListener("submit", async function (event){
        event.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

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
                throw new Error(data.message);
            }

            window.location.href = "/dashboard";

        }catch(error){
            console.error(error);

            alert(error.message);
        }
    });
}