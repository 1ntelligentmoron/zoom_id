// Communication with Python backend via Eel
async function hello() { document.getElementById("hi").innerHTML = await eel.username_to_js()(); }


// Frontend
function onLoad() {

    hello();

    // Disable right click
    // document.oncontextmenu = RightMouseDown;
    // document.onmousedown = mouseDown; 
    // function RightMouseDown() { return false; }
    
}

function url(href) { window.open(href, '_self'); }
function urlNewPage(href) { window.open(href); }
