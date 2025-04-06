// navbar menu bars
let menu = document.querySelector("#menu-bars");
let nav = document.querySelector(".nav-content");

menu.onclick = () => { 
    menu.classList.toggle("fa-times");
    nav.classList.toggle("active");
}


let header = document.getElementById("nav");
let header_logo = document.getElementById("nav-logo");


const onScroll = () => {

    const scroll = document.documentElement.scrollTop

    if (scroll > 10) {
    header.classList.add('shrink');
    header_logo.classList.add('shrinklogo');
} else {
    header.classList.remove('shrink');
    header_logo.classList.remove('shrinklogo');
    }
}
window.addEventListener('scroll', onScroll);