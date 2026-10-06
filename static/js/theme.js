function updateThemeButton() {
    const themeToggle = document.getElementById("themeToggle");

    if (!themeToggle) {
        return;
    }

    if (document.body.classList.contains("light")) {
        themeToggle.textContent = "Dark Mode";
    } else {
        themeToggle.textContent = "Light Mode";
    }
}


function loadTheme() {
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "light") {
        document.body.classList.add("light");
    } else {
        document.body.classList.remove("light");
    }

    updateThemeButton();
}


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


export function initTheme() {
    const themeToggle =
        document.getElementById("themeToggle");

    if (!themeToggle) {
        return;
    }

    loadTheme();

    themeToggle.addEventListener(
        "click",
        toggleTheme
    );
}
