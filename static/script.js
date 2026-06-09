/* =========================================
   PARTICLES BACKGROUND
========================================= */

tsParticles.load("particles-js", {

    fullScreen: {
        enable: false
    },

    particles: {

        number: {
            value: 80
        },

        color: {
            value: "#00E5FF"
        },

        links: {

            enable: true,

            distance: 150,

            color: "#00E5FF",

            opacity: 0.3,

            width: 1
        },

        move: {

            enable: true,

            speed: 1
        },

        opacity: {
            value: 0.5
        },

        size: {
            value: 2
        }

    },

    interactivity: {

        events: {

            onHover: {

                enable: true,

                mode: "grab"

            }

        }

    }

});


/* =========================================
   COUNTER ANIMATION
========================================= */

const counters =
document.querySelectorAll('.counter');

const animateCounter = (counter) => {

    const target =
    +counter.getAttribute(
    'data-target');

    const increment =
    target / 100;

    let count = 0;

    const updateCounter = () => {

        if(count < target){

            count += increment;

            counter.innerText =
            Math.floor(count);

            requestAnimationFrame(
            updateCounter);

        }

        else{

            counter.innerText =
            target;

        }

    };

    updateCounter();

};

const counterObserver =
new IntersectionObserver(

(entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

animateCounter(
entry.target);

counterObserver.unobserve(
entry.target);

}

});

},

{
    threshold:0.5
}

);

counters.forEach(counter=>{

counterObserver.observe(
counter);

});


/* =========================================
   SCROLL REVEAL
========================================= */

const revealElements =
document.querySelectorAll(

'.glass-card,.section-title,.hero'

);

const revealObserver =
new IntersectionObserver(

(entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.classList.add(
'show-element');

}

});

},

{
    threshold:0.15
}

);

revealElements.forEach(el=>{

el.classList.add(
'hidden-element');

revealObserver.observe(el);

});


/* =========================================
   CARD HOVER EFFECT
========================================= */

document.querySelectorAll(

'.glass-card'

).forEach(card=>{

card.addEventListener(

'mousemove',

(e)=>{

const rect =
card.getBoundingClientRect();

const x =
e.clientX - rect.left;

const y =
e.clientY - rect.top;

card.style.setProperty(
'--mouse-x',
`${x}px`
);

card.style.setProperty(
'--mouse-y',
`${y}px`
);

}

);

});


/* =========================================
   NAVBAR SHADOW
========================================= */

window.addEventListener(

'scroll',

()=>{

const nav =
document.querySelector(
'.navbar'
);

if(window.scrollY > 50){

nav.style.boxShadow =
'0 10px 40px rgba(0,0,0,.4)';

}
else{

nav.style.boxShadow =
'none';

}

});

function updateDashboard(score,label){

    score = parseFloat(score);

    let manipulationScore;
    let authenticityScore;

    if(label.toUpperCase() === "FAKE"){

        manipulationScore = score;
        authenticityScore = 100 - score;

    }
    else{

        authenticityScore = score;
        manipulationScore = 100 - score;

    }

    document.getElementById(
"confidence-fill"
).style.width =
score + "%";

const level =
document.getElementById(
"confidence-level"
);

if(score >= 95){

    level.innerHTML =
    "Very High Confidence";

}
else if(score >= 80){

    level.innerHTML =
    "High Confidence";

}
else if(score >= 60){

    level.innerHTML =
    "Moderate Confidence";

}
else{

    level.innerHTML =
    "Low Confidence";

}

    animateValue(
        "gauge-value",
        Math.round(score)
    );

    document.getElementById(
        "risk-percent"
    ).innerHTML =
    manipulationScore.toFixed(2) + "%";

    document.getElementById(
        "risk-bar"
    ).style.width =
    manipulationScore + "%";

    document.getElementById(
        "fake-score"
    ).innerHTML =
    manipulationScore.toFixed(2) + "%";

    document.getElementById(
        "auth-score"
    ).innerHTML =
    authenticityScore.toFixed(2) + "%";

    document.getElementById(
        "result-label"
    ).innerHTML =
    label;

    const badge =
    document.getElementById(
        "threat-badge"
    );

    badge.className =
    "threat-badge";

    if(manipulationScore >= 90){

        badge.innerHTML =
        "CRITICAL RISK";

        badge.classList.add(
        "badge-danger"
        );

    }
    else if(manipulationScore >= 70){

        badge.innerHTML =
        "HIGH RISK";

        badge.classList.add(
        "badge-danger"
        );

    }
    else if(manipulationScore >= 40){

        badge.innerHTML =
        "MEDIUM RISK";

        badge.classList.add(
        "badge-warning"
        );

    }
    else{

        badge.innerHTML =
        "LOW RISK";

        badge.classList.add(
        "badge-safe"
        );

    }

}
function animateValue(id,target){

    const element =
    document.getElementById(id);

    let start = 0;

    clearInterval(
        element.animationTimer
    );

    element.animationTimer =
    setInterval(()=>{

        if(start >= target){

            clearInterval(
                element.animationTimer
            );

            element.innerHTML =
            target.toFixed(0) + "%";

            return;
        }

        start += Math.max(
            1,
            Math.ceil(target/50)
        );

        if(start > target){

            start = target;
        }

        element.innerHTML =
        start.toFixed(0) + "%";

    },20);

}
