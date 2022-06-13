//This is for change image on landing page

// let landing = document.querySelector('.landing');
// DJANGO_STATIC_URL = '{{ STATIC_URL }}';
// let images = [{ 'Home/Image/landing1.jpg', 'Image/landing2.jpg', 'Image/landing3.jpg', 'Image/landing4.jpg'];
// landing.style.backgroundImage = `url("{% static 'Home/Image/landing1.jpg' %}")`

// let backgroundOption = true,
//     backgroundInterval;
// function randomizImgs() {
//     if (backgroundOption) {

//         backgroundInterval = setInterval(() => {
//             let random = Math.floor(Math.random() * images.length);

//             landing.style.backgroundImage = `url('${images[random]}')`
//         }, 5000);
//     } else {
//         clearInterval(backgroundInterval)
//     }
// }

// randomizImgs()

//This is for change image on landing page
let gear = document.querySelector('.fa-gear')
gear.addEventListener('click', () => {
    gear.classList.toggle('rotate');
    document.querySelector('.setting-box').classList.toggle('open');
});

//Local Store
const localStore = localStorage.getItem('options');
if (localStore !== null) {
    document.documentElement.style.setProperty('--main-color', localStore);

    document.querySelectorAll('color-list li').forEach(elem => {
        elem.classList.remove('active');
        if (elem.dataset.color === localStore) {
            elem.classList.add('active');
        }
    })
    // localStore.classList.add('active');
}

//Switch Colors
const colorLi = document.querySelectorAll('.color-list li');

colorLi.forEach(li => {
    li.addEventListener('click', (e) => {
        const root = e.target.dataset.color;
        //Set value of li on root
        document.documentElement.style.setProperty('--main-color', root);
        localStorage.setItem('options', root);

        //Remove active class
        e.target.parentElement.querySelectorAll('.color-list li').forEach(elem => {
            elem.classList.remove('active');
        })
        e.target.classList.add('active');
    })
})

//Switch Backgorund-image 
document.querySelectorAll('.randomBG button').forEach(elem => {
    elem.addEventListener('click', (e) => {
        e.target.parentElement.querySelectorAll('.active').forEach(element => {
            element.classList.remove('active');

        })
        elem.classList.add('active');
        if (e.target.dataset.background === "true") {
            backgroundOption = true;
            randomizImgs();
        } else {
            backgroundOption = false;
            clearInterval(backgroundInterval);
        }
    })
})

document.querySelectorAll('.bulletsOption button').forEach(elem => {
    elem.addEventListener('click', (e) => {
        e.target.parentElement.querySelectorAll('.active').forEach(elemnt => {
            elemnt.classList.remove('active');
        })
        elem.classList.add('active');

        if (e.target.dataset.bullet === 'false') {
            document.querySelector('.nav-bullet').style.display = 'none';
        } else {
            document.querySelector('.nav-bullet').style.display = 'block';

        }
    })
})

localStorage.getItem('lang');
document.querySelectorAll('.language a').forEach(elem => {
    elem.addEventListener('click', (e) => {
        e.target.parentElement.querySelectorAll('.active').forEach(elemnt => {
            elemnt.classList.remove('active');
        })
        elem.classList.add('active');
        localStorage.setItem('lang', e)
    })
})
//Progress Animation

// let ourSkills = document.querySelector('.skills');

// window.onscroll = function () {
//     //Skill offset top 
//     let skillOfsetTop = ourSkills.offsetTop;
//     //Skills outer Height
//     let skillOuterHeight = ourSkills.offsetHeight;
//     //Window height
//     let windowHeight = this.innerHeight;
//     //Window Scroll top
//     let windowScrollTop = this.pageYOffset;

//     //ده يعرفك انك وصلت للسكشن 
//     if (windowScrollTop > skillOfsetTop + skillOuterHeight - windowHeight) {

//         document.querySelectorAll('.skill-box .skill-progress span').forEach(span => {
//             span.style.width = span.dataset.progress;
//         })
//     }
// }


//Images 
let Gallery = document.querySelectorAll('.gallery img').forEach(img => {
    img.addEventListener('click', (e) => {
        //Create overlay 
        let overlay = document.createElement('div');
        overlay.classList.toggle('popup-overlay');
        //Append overlay div 
        document.body.appendChild(overlay);

        //Create popup box
        let popupBox = document.createElement('div');
        popupBox.className = 'popupBox';

        //Create Text from alt

        let heading = document.createElement('h3');
        heading.className = "heading-gallery";
        if (img.getAttribute('alt') !== null) {
            heading.append(document.createTextNode(img.getAttribute('alt')));
            popupBox.appendChild(heading);
        }

        //Create close button 
        let closeBtn = document.createElement('i');
        closeBtn.className = "fa-solid fa-xmark";
        closeBtn.addEventListener('click', () => {
            // overlay.style.display = 'none';
            // popupBox.style.display = 'none';
            overlay.remove();
            popupBox.remove();
        })
        popupBox.appendChild(closeBtn);
        //Create image in popup box
        let popupImg = document.createElement('img');
        popupImg.src = img.src;
        // console.log(img.src)
        // console.log(popupImg.src)

        //append image on popupbox
        popupBox.appendChild(popupImg);
        document.body.appendChild(popupBox);

    })
})



//Nav Bullets

const Bullets = document.querySelectorAll('.nav-bullet .bullets');
Bullets.forEach(bullet => {
    bullet.addEventListener('click', (e) => {
        document.querySelector(e.target.dataset.section).scrollIntoView({
            behavior: 'smooth'
        })
    })
})

//Reset options 
document.querySelector('.reset').onclick = function () {
    localStorage.clear();
    window.location.reload();
}

// document.querySelector('.refresh').addEventListener('click', () => {
//     window.location.reload();
//     console.log('we')
// })

//Create overlay
let closeBtn = document.querySelector('.fedback .close');
let feedBack = document.querySelector('.feed-back .feed-back-btn').addEventListener('click', () => {
    let overlay = document.createElement('div');
    overlay.classList.toggle('popup-overlay');
    //Append overlay div 
    document.body.appendChild(overlay);
    document.querySelector('.fedback').style.display = 'block';

    //For close feedback page
    closeBtn.addEventListener('click', () => {
        document.querySelector('.popup-overlay').remove();
        document.querySelector('.fedback').style.display = 'none'
    })


    document.querySelector('.send').addEventListener('click', () => {
        if (document.querySelector('.feedbackInput').value == '') {
            let alerterror = document.createElement('div');
            alerterror.className = 'alert alert-danger w-75';
            alerterror.append('Please, Enter your Feed Back')
            document.querySelector('.error').style.color = 'red';
            document.querySelector('.fedback').appendChild(alerterror);
            alerterror.style.color = 'red';
            alerterror.style.textAlign = 'center';
            setTimeout(() => {
                alerterror.remove();
                document.querySelector('.error').style.color = 'white';
            }, 2000);
        }

        else {
            let alertsuccess = document.createElement('div');
            alertsuccess.className = 'alert alert-success w-75';
            alertsuccess.append('Thank You for Feed Back')

            document.querySelector('.fedback').appendChild(alertsuccess);
            alertsuccess.style.color = 'green';
            alertsuccess.style.textAlign = 'center';

            setTimeout(() => {
                document.querySelector('.popup-overlay').remove();
                document.querySelector('.fedback').style.display = 'none';
                document.querySelector('.feedbackInput').value = "";
                alertsuccess.remove();
            }, 2000);

        }
    })
    let popupBox = document.querySelector('.fedback')
    popupBox.classList.add('popupBox');
})

const faces = document.querySelectorAll('.faces i');

faces.forEach(i => {
    i.addEventListener('click', (e) => {
        // const root = e.target.dataset.color;
        //Set value of li on root

        //Remove active class
        e.target.parentElement.querySelectorAll('.faces i').forEach(elem => {
            elem.classList.remove('active');
        })
        e.target.classList.add('active');
    })
})


window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.querySelector(".navbar").style.top = "0px";
        document.querySelector(".navbar").style.backgroundColor = "rgb(79, 79, 79)";
        document.querySelector(".navbar").style.zIndex = "100";


    } else {
        document.querySelector(".navbar").style.top = "48px";
        document.querySelector(".navbar").style.backgroundColor = "transparent";

    }
}

//--------------------------------------------------------------------------
//Search bar

const clinicName = document.querySelectorAll('.serv-content');

const searchInput = document.querySelector('[data-search]');


searchInput.addEventListener('input', (e) => {
    console.log(searchInput.value);
    const text = e.target.value.toLowerCase();
    clinicName.forEach(function (task) {

        const item = task.textContent;
        if (item.toLowerCase().indexOf(text) != -1) {
            task.style.display = 'block';

        } else {
            task.style.display = 'none';

        }
    });

})
//--------------------------------------------------------------------------