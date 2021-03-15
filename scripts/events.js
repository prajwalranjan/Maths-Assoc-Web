const slide = document.querySelector(".events-slide");
const images = document.querySelectorAll(".event");
const left = document.querySelector(".left-arrow");
const right = document.querySelector(".right-arrow");
const bubbles = document.querySelectorAll(".bubble");

let counter = 1;
const size = images[0].clientWidth;

slide.style.transform = "translateX(" + (-size*counter) + "px";

left.addEventListener("click", ()=>{
    if(counter<=0) return;
    slide.style.transition = "transform 0.4s ease-out";
    counter--;
    slide.style.transform = "translateX(" + (-size*counter) + "px";
})

right.addEventListener("click", ()=>{
    if(counter>=images.length-1) return;
    slide.style.transition = "transform 0.5s ease-out";
    counter++;
    slide.style.transform = "translateX(" + (-size*counter) + "px";
})

slide.addEventListener("transitionend", ()=>{
    if(images[counter].id === "last-clone"){
        slide.style.transition = "none";
        counter=images.length-2;
        slide.style.transform = "translateX(" + (-size*counter) + "px";
    }
    if(images[counter].id === "first-clone"){
        slide.style.transition = "none";
        counter=images.length-counter;
        slide.style.transform = "translateX(" + (-size*counter) + "px";
    }
});

slide.addEventListener("wheel", (e)=>{
    e.preventDefault();
});

bubbles.forEach((bubble, index)=>{
    bubble.addEventListener("click", ()=>{
        bubbles.forEach((bbl)=>{
            if(bbl.classList.contains("active-bubble")){
                bbl.classList.remove("active-bubble");
            }
        });
        bubble.classList.add("active-bubble");
        slide.style.transition = "transform 0.5s ease-out";
        slide.style.transform = "translateX(" + (-size*(index+1)) + "px";
    });
});