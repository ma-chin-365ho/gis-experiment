const { io } = require("socket.io-client");

const socket = io("http://localhost:5000");

let srvMsgCount = 0;

socket.on("connect", () => {
    console.log("connect ok!!!");
    console.log(socket.id); // x8WIv7-mJelg7on_ALbx
});

socket.on("disconnect", () => {
    console.log("disconnect ok!!!");
    console.log(socket.id); // undefined
});

socket.io.on("reconnect", () => {
    console.log("reconnect ok!!!");
    console.log(socket.id); // x8WIv7-mJelg7on_ALbx
});

socket.on("srvMsg", (data) => {
    srvMsgCount++;
    console.log("srvMsg" + String(srvMsgCount));
    console.log(data);
});