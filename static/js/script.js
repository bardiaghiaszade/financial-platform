import { initPassword } from "./password.js";
import { initTheme } from "./theme.js";
import { initLogin } from "./login.js";
import { initSignup } from "./signup.js";


document.addEventListener("DOMContentLoaded", function () {

    initPassword();
    initTheme();
    initLogin();
    initSignup();

});
