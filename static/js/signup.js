export function initSignup(){

    const signupForm = document.getElementById("signupForm");

    if(!signupForm){
        return;
    };
    
    signupForm.addEventListener("submit", async function (event){
        event.preventDefault();

        const firstName = document.getElementById("firstName").value;
        const lastName = document.getElementById("lastName").value;
        const phone = document.getElementById("phone").value
        const email = document.getElementById("email").value;
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        try{

            const response = await fetch("/api/signup", {
                method : "POST",
                headers : {
                    "Content-Type": "application/json"
                },
                body : JSON.stringify({
                    firstName : firstName,
                    lastName : lastName,
                    phone : phone,
                    email : email,
                    username : username,
                    password : password
                })
            });

            const data = await response.json();

            if(!response.ok){
                throw new Error(data.message);
            }

            window.location.href = "/login";

        }catch(error){
            console.error(error);

            alert(error.message);
        }
    });
}