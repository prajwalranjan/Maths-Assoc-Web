function navLinksToggler(){
    const hamburger = document.querySelector(".nav-hamburger");
    const navlinks = document.querySelector(".nav-links");

    hamburger.addEventListener("click", () => {
        navlinks.classList.toggle("activate");
    });
}

navLinksToggler();

