const bar = document.getElementById("bar");
const nav = document.getElementById("navbar");
const close = document.getElementById('close');

if(bar) {
    bar.addEventListener('click', () => {
        nav.classList.add("active");
    })
} if(close) {
    close.addEventListener('click', () => {
        nav.classList.remove("active");
    })
}




// bar.addEventListener('click', () => {
//     if(nav.style.right == "-300") {
//         nav.style.right = "0px;"
//     } else {
//         nav.style.right = "-300";
//     }
// });