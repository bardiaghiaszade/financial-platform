export function initForgotPass(){

    const forgotPassForm = document.getElementById("forgotPassForm");

    if(!forgotPassForm){
        return;
    }

    forgotPassForm.addEventListener("submit", async function (event){
        event.preventDefault();

        const email = document.getElementById("email").value;

        const forgotPassMessage = document.getElementById("forgotPassMessage");

        forgotPassMessage.textContent = "";
        forgotPassMessage.classList.remove("success", "show");

        try{
           
            const response = await fetch("/api/forgotPass", {
                method : "POST",
                headers : {"Content-Type" : "application/json"},
                body : JSON.stringify({email : email})
            });

            const data = await response.json();


            if(!response.ok){
                forgotPassMessage.textContent = data.message;
                forgotPassMessage.classList.add("show");

                return;
            }

            forgotPassMessage.textContent = data.message;
            forgotPassMessage.classList.add("show", "success");

            setTimeout(()=>{
                window.location.href = "/login";
            }, 1000);
        }catch{
            forgotPassMessage.textContent = data.message;
        }
    });
}