function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function changeImage(num) {
    document.getElementById("mypic").src=pics_src[num];
    await sleep(5000);
} 

const socket = io("http://localhost:5000");

socket.on("connect", () => {
    console.log(socket.connected); // true
});
var pics_src = new Array("static/image/1.png","static/image/2.png","static/image/3.png","static/image/4.png","static/image/5.png","static/image/6.png");
socket.on("to_browser", (data) => {
    console.log(data);
    changeImage(data)
});