from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="theme-color" content="#16091d">
<title>Happy Birthday ❤️</title>
<style>
html{
    background:#16091d;
    overscroll-behavior:none;
    color-scheme:dark;
}
html, body{
    margin:0;
    padding:0;
    width:100%;
    min-height:100%;
}
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    -webkit-tap-highlight-color:transparent;
}
body{
    min-height:100vh;
    overflow-x:hidden;
    position:relative;
    font-family: Arial, Helvetica, sans-serif;
    color:white;
    background:#16091d;
    overscroll-behavior-y:none;
}
.bg{
    position:fixed;
    inset:0;
    width:100%;
    height:100%;
    z-index:-20;
    overflow:hidden;
    background:
        radial-gradient(circle at 15% 15%, rgba(255,74,157,.32), transparent 32%),
        radial-gradient(circle at 85% 80%, rgba(157,65,255,.30), transparent 35%),
        radial-gradient(circle at 50% 45%, rgba(255,80,180,.12), transparent 40%),
        linear-gradient(135deg, #18091f, #25102d, #120719);
}
.blob{
    position:absolute;
    width:280px;
    height:280px;
    border-radius:50%;
    pointer-events:none;
    opacity:.30;
    will-change:transform;
}
.blob1{
    left:-100px;
    top:-100px;
    background: radial-gradient(circle, #ff3d91 0%, rgba(255,61,145,.15) 55%, transparent 72%);
    animation: moveBlob1 10s ease-in-out infinite alternate;
}
.blob2{
    right:-100px;
    bottom:-90px;
    background: radial-gradient(circle, #9b4dff 0%, rgba(155,77,255,.15) 55%, transparent 72%);
    animation: moveBlob2 12s ease-in-out infinite alternate;
}
.blob3{
    width:210px;
    height:210px;
    left:55%;
    top:15%;
    background: radial-gradient(circle, #ff4eaa, transparent 70%);
    opacity:.12;
    animation: moveBlob3 14s ease-in-out infinite alternate;
}
@keyframes moveBlob1{
    from{ transform: translate3d(0,0,0) scale(1); }
    to{ transform: translate3d(80px,65px,0) scale(1.15); }
}
@keyframes moveBlob2{
    from{ transform: translate3d(0,0,0) scale(1); }
    to{ transform: translate3d(-75px,-60px,0) scale(1.12); }
}
@keyframes moveBlob3{
    from{ transform: translate3d(0,0,0) scale(.9); }
    to{ transform: translate3d(-60px,100px,0) scale(1.2); }
}
.light{
    position:fixed;
    width:170px;
    height:170px;
    border-radius:50%;
    pointer-events:none;
    z-index:-10;
    opacity:.10;
    background:#ff62aa;
    animation: lightMove 9s ease-in-out infinite alternate;
}
@keyframes lightMove{
    from{ transform: translate3d(0,0,0); }
    to{ transform: translate3d(150px, 170px, 0); }
}
.container{
    position:relative;
    z-index:5;
    min-height:100vh;
    width:100%;
    display:flex;
    align-items:center;
    justify-content:center;
    padding: 25px 10px 40px;
}
.card{
    width:min(94%,620px);
    padding: 40px 25px;
    text-align:center;
    background: linear-gradient(145deg, rgba(255,255,255,.075), rgba(255,255,255,.025));
    border: 1px solid rgba(255,160,215,.22);
    border-radius:28px;
    box-shadow: 0 20px 60px rgba(0,0,0,.30), inset 0 0 35px rgba(255,120,200,.035);
    position:relative;
    overflow:hidden;
    animation: cardIn .8s ease;
}
.card::before{
    content:"";
    position:absolute;
    width:230px;
    height:230px;
    left:-120px;
    top:-120px;
    border-radius:50%;
    background: rgba(255,80,165,.11);
    pointer-events:none;
}
.card::after{
    content:"";
    position:absolute;
    width:220px;
    height:220px;
    right:-130px;
    bottom:-120px;
    border-radius:50%;
    background: rgba(145,75,255,.10);
    pointer-events:none;
}
@keyframes cardIn{
    from{ opacity:0; transform: translateY(30px) scale(.97); }
    to{ opacity:1; transform: translateY(0) scale(1); }
}
.small{
    position:relative;
    z-index:2;
    font-size:10px;
    font-weight:600;
    letter-spacing:3px;
    color:#f2a6c9;
    text-transform:uppercase;
    margin-bottom:15px;
}
h1{
    position:relative;
    z-index:2;
    font-family: Georgia, "Times New Roman", serif;
    font-style:italic;
    font-size: clamp(43px, 11vw, 72px);
    line-height:1.12;
    background: linear-gradient(90deg, #ff70ac, #ff9bc7, #ca6cff, #ff70ac);
    background-size:220%;
    -webkit-background-clip:text;
    background-clip:text;
    color:transparent;
    animation: titleShine 5s linear infinite;
    filter: drop-shadow(0 4px 10px rgba(255,60,150,.20));
}
@keyframes titleShine{
    from{ background-position:0%; }
    to{ background-position:220%; }
}

/* গোল ছবির জন্য যোগ করা CSS */
.profile-img {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    object-fit: cover;
    margin: 18px auto 10px;
    border: 3px solid #ff70ac;
    box-shadow: 0 0 20px rgba(255, 112, 172, 0.4);
    display: block;
    position: relative;
    z-index: 2;
}

.name{
    position:relative;
    z-index:2;
    margin-top:9px;
    font-size: clamp(27px, 7vw, 42px);
    font-weight:700;
}
.name span{
    background: linear-gradient(90deg, #ff6ca9, #e58cff);
    -webkit-background-clip:text;
    background-clip:text;
    color:transparent;
}
.line{
    position:relative;
    z-index:2;
    width:80px;
    height:2px;
    margin:21px auto;
    border-radius:20px;
    background: linear-gradient(90deg, transparent, #ff5d9f, #a65cff, transparent);
    box-shadow: 0 0 10px rgba(255,80,160,.35);
}
.heart{
    position:relative;
    z-index:2;
    font-size:44px;
    margin: 13px 0 18px;
    animation: heartbeat 1.5s infinite;
    filter: drop-shadow(0 5px 12px rgba(255,20,70,.38));
}
@keyframes heartbeat{
    0%,100%{ transform:scale(1); }
    15%{ transform:scale(1.22); }
    30%{ transform:scale(1); }
    45%{ transform:scale(1.13); }
}
.message{
    position:relative;
    z-index:2;
    max-width:510px;
    margin:auto;
    color:#eee4ed;
    font-size:14px;
    line-height:1.9;
    font-weight:500;
}
.message b{
    color:#ff76b1;
    font-weight:700;
}
button{
    position:relative;
    z-index:5;
    margin-top:27px;
    padding: 14px 30px;
    border:none;
    outline:none;
    border-radius:50px;
    color:white;
    background: linear-gradient(135deg, #ff267c, #d52de6, #813eff);
    font-family: Arial, Helvetica, sans-serif;
    font-size:14px;
    font-weight:700;
    cursor:pointer;
    box-shadow: 0 9px 28px rgba(220,35,170,.35);
    animation: buttonPulse 2.5s ease-in-out infinite;
    transition: transform .18s ease;
}
button:active{
    transform: scale(.93);
}
@keyframes buttonPulse{
    0%,100%{ box-shadow: 0 9px 25px rgba(220,35,170,.28); }
    50%{ box-shadow: 0 9px 38px rgba(220,35,170,.55); }
}
button.clicked{
    animation: buttonClick .55s ease;
}
@keyframes buttonClick{
    0%{ transform:scale(1); }
    45%{ transform:scale(.91); }
    100%{ transform:scale(1); }
}
.hidden-message{
    position:relative;
    z-index:3;
    max-height:0;
    overflow:hidden;
    opacity:0;
    margin-top:0;
    transition: max-height .9s ease, opacity .6s ease, margin .6s ease;
}
.hidden-message.show{
    max-height:600px;
    opacity:1;
    margin-top:25px;
}
.secret-box{
    padding: 22px 17px;
    border-radius:20px;
    background: linear-gradient(145deg, rgba(255,255,255,.075), rgba(255,255,255,.025));
    border: 1px solid rgba(255,135,200,.20);
    box-shadow: inset 0 0 30px rgba(255,70,170,.035);
}
.secret-text{
    color:#eee5ee;
    font-size:14px;
    line-height:1.9;
    opacity:0;
    transform: translateY(15px);
}
.hidden-message.show .secret-text.one{
    animation: textReveal .7s ease forwards;
    animation-delay:.25s;
}
.hidden-message.show .secret-text.two{
    margin-top:12px;
    animation: textReveal .7s ease forwards;
    animation-delay:.7s;
}
@keyframes textReveal{
    from{ opacity:0; transform: translateY(15px); }
    to{ opacity:1; transform: translateY(0); }
}
.secret-heart{
    display:block;
    margin-top:8px;
    font-size:20px;
    opacity:0;
}
.hidden-message.show .secret-heart{
    animation: miniHeart .7s ease forwards;
    animation-delay:1.15s;
}
@keyframes miniHeart{
    0%{ opacity:0; transform:scale(.4); }
    65%{ opacity:1; transform:scale(1.25); }
    100%{ opacity:1; transform:scale(1); }
}
.script{
    margin-top:16px;
    color:#f28bb9;
    font-family: "Brush Script MT", "Segoe Script", cursive;
    font-size:20px;
    line-height:1.55;
    font-style:italic;
    opacity:0;
}
.hidden-message.show .script{
    animation: scriptReveal .9s ease forwards;
    animation-delay:1.35s;
}
@keyframes scriptReveal{
    0%{ opacity:0; transform: translateY(14px) scale(.96); }
    70%{ opacity:1; transform: translateY(-2px) scale(1.03); }
    100%{ opacity:1; transform: translateY(0) scale(1); }
}
.secret-line{
    width:55px;
    height:2px;
    margin:14px auto;
    background: linear-gradient(90deg, transparent, #ed5ca2, #a65cff, transparent);
    opacity:0;
}
.hidden-message.show .secret-line{
    animation: dividerShow .6s ease forwards;
    animation-delay:2s;
}
@keyframes dividerShow{
    from{ opacity:0; transform: scaleX(0); }
    to{ opacity:1; transform: scaleX(1); }
}
.once{
    color:#a99baa;
    font-size:11px;
    opacity:0;
}
.hidden-message.show .once{
    animation: textReveal .6s ease forwards;
    animation-delay:2.1s;
}
.final{
    margin-top:8px;
    font-size:17px;
    font-weight:700;
    background: linear-gradient(90deg, #ff65a5, #c86cff);
    -webkit-background-clip:text;
    background-clip:text;
    color:transparent;
    opacity:0;
}
.hidden-message.show .final{
    animation: finalReveal .8s ease forwards;
    animation-delay:2.3s;
}
@keyframes finalReveal{
    0%{ opacity:0; transform: translateY(10px) scale(.95); }
    70%{ opacity:1; transform: translateY(-2px) scale(1.04); }
    100%{ opacity:1; transform: translateY(0) scale(1); }
}
.footer{
    position:relative;
    z-index:2;
    margin-top:25px;
    color:#918394;
    font-size:9px;
}
.floating-heart{
    position:fixed;
    bottom:-35px;
    z-index:2;
    pointer-events:none;
    opacity:.55;
    animation: floatHeart linear forwards;
}
@keyframes floatHeart{
    0%{ transform: translate3d(0,0,0) rotate(0deg); opacity:0; }
    15%{ opacity:.65; }
    100%{ transform: translate3d(0, -110vh, 0) rotate(260deg); opacity:0; }
}
.love{
    position:fixed;
    left:50%;
    top:50%;
    z-index:100;
    pointer-events:none;
    animation: loveBurst .9s cubic-bezier(.2,.8,.3,1) forwards;
}
@keyframes loveBurst{
    0%{ opacity:1; transform: translate(-50%,-50%) scale(.3); }
    100%{ opacity:0; transform: translate(calc(-50% + var(--x)), calc(-50% + var(--y))) rotate(var(--r)) scale(1.1); }
}
.confetti{
    position:fixed;
    left:50%;
    top:50%;
    width:6px;
    height:6px;
    z-index:100;
    pointer-events:none;
    border-radius:2px;
}
@media(max-width:500px){
    .container{ padding: 18px 9px 35px; }
    .card{ width:100%; padding: 32px 17px; border-radius:24px; }
    .small{ font-size:9px; letter-spacing:2px; }
    h1{ font-size:43px; }
    .name{ font-size:29px; }
    .message{ font-size:13px; line-height:1.85; }
    .script{ font-size:19px; }
    .profile-img{ width: 110px; height: 110px; }
}
</style>
</head>
<body>
<div class="bg">
    <div class="blob blob1"></div>
    <div class="blob blob2"></div>
    <div class="blob blob3"></div>
</div>
<div class="light"></div>

<audio id="birthdaySong" loop preload="auto">
    <source src="/happy-birthday.mp3" type="audio/mpeg">
</audio>

<div class="container">
<div class="card">
<div class="small">A Special Day For Someone Special</div>
<h1>Happy Birthday</h1>

<!-- গোল ইমেজ ট্যাগ (এখানে আপনার GitHub-এর ইমেজ ফাইলের নাম বা লিংক দিন) -->
<img src="/profile.png" alt="Profile Picture" class="profile-img">

<div class="name"><span>Surovii</span> 🎂</div>
<div class="line"></div>
<div class="heart">❤️</div>
<p class="message">
    Today is not just another day...<br>
    It's the day a <b>beautiful soul</b> came into this world. ✨<br><br>
    I hope your day is filled with <b>happiness, laughter, beautiful moments</b> and everything that makes you smile. 🌸
</p>
<button id="messageButton" onclick="showMessage()">💌 One More Thing</button>
<div class="hidden-message" id="secret">
<div class="secret-box">
<div class="secret-text one">May all your little dreams slowly turn into beautiful realities. ✨</div>
<div class="secret-text two">Keep smiling, keep shining, and always stay the wonderful person you are.</div>
<span class="secret-heart">❤️</span>
<div class="script">You deserve all the beautiful moments life has to offer. 🌸✨</div>
<div class="secret-line"></div>
<div class="once">Once again...</div>
<div class="final">Happy Birthday, Surovii! 🥳✨</div>
</div>
</div>
<div class="footer">Made with ❤️ just for you</div>
</div>
</div>

<script>
const music = document.getElementById("birthdaySong");
music.volume = 0.55;

function startAudio() {
    if (music.paused) {
        music.play().catch(e => console.log("Audio play blocked:", e));
    }
}

document.addEventListener("click", startAudio, { once: true });
document.addEventListener("touchstart", startAudio, { once: true });

function showMessage(){
    startAudio();
    const box = document.getElementById("secret");
    const button = document.getElementById("messageButton");
    button.classList.remove("clicked");
    void button.offsetWidth;
    button.classList.add("clicked");
    box.classList.toggle("show");
    if(box.classList.contains("show")){
        button.innerHTML = "💖 Hide Message";
        createLoveBurst(25);
        createConfetti(35, button);
    } else {
        button.innerHTML = "💌 One More Thing";
    }
}

const heartList = ["❤️", "💗", "💕", "💖", "💓", "💞", "✨", "🌸"];
function createHeart(){
    const heart = document.createElement("div");
    heart.className = "floating-heart";
    heart.innerHTML = heartList[Math.floor(Math.random() * heartList.length)];
    heart.style.left = Math.random()*100 + "vw";
    heart.style.fontSize = (12 + Math.random()*13) + "px";
    heart.style.animationDuration = (7 + Math.random()*4) + "s";
    document.body.appendChild(heart);
    setTimeout(function(){ heart.remove(); }, 12000);
}
setInterval(createHeart, 1100);

function createLoveBurst(amount){
    const loves = ["❤️", "💗", "💕", "💖", "💓"];
    for(let i=0; i<amount; i++){
        const love = document.createElement("div");
        love.className = "love";
        love.innerHTML = loves[Math.floor(Math.random() * loves.length)];
        const angle = (Math.PI*2/amount) * i;
        const distance = 90 + Math.random()*210;
        const x = Math.cos(angle) * distance;
        const y = Math.sin(angle) * distance;
        love.style.setProperty("--x", x + "px");
        love.style.setProperty("--y", y + "px");
        love.style.setProperty("--r", (Math.random()*60-30) + "deg");
        love.style.fontSize = (15 + Math.random()*12) + "px";
        document.body.appendChild(love);
        setTimeout(function(){ love.remove(); }, 1000);
    }
}

function createConfetti(amount, target){
    const colors = ["#ff4f98", "#ff75ae", "#b35cff", "#d47cff", "#ffd166"];
    let centerX = window.innerWidth / 2;
    let centerY = window.innerHeight / 2;

    if(target){
        const rect = target.getBoundingClientRect();
        centerX = rect.left + rect.width / 2;
        centerY = rect.top + rect.height / 2;
    }

    for(let i=0; i<amount; i++){
        const c = document.createElement("div");
        c.className = "confetti";
        c.style.background = colors[Math.floor(Math.random() * colors.length)];
        const angle = Math.random() * Math.PI * 2;
        const distance = 100 + Math.random()*240;
        const x = Math.cos(angle) * distance;
        const y = Math.sin(angle) * distance;
        c.style.left = centerX + "px";
        c.style.top = centerY + "px";

        c.animate([
            { transform: "translate(-50%,-50%)", opacity:1 },
            { transform: `translate(calc(-50% + ${x}px), calc(-50% + ${y}px)) rotate(${Math.random()*500}deg)`, opacity:0 }
        ], {
            duration: 900 + Math.random()*600,
            easing: "cubic-bezier(.2,.8,.3,1)"
        });

        document.body.appendChild(c);
        setTimeout(function(){ c.remove(); }, 1700);
    }
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)
