document.addEventListener("DOMContentLoaded", function () {
    console.log("📷 Face Mask Detection System Loaded");

    const startBtn = document.getElementById("start-btn");
    const videoContainer = document.getElementById("video-container");
    const videoFeed = document.getElementById("video-feed");

    startBtn.addEventListener("click", function () {
        if (!videoContainer.classList.contains("active")) {
            videoContainer.classList.add("active");
            startBtn.innerText = "⛔ Stop Camera";
            startBtn.style.background = "linear-gradient(90deg, #d9534f, #c9302c)";
        } else {
            videoContainer.classList.remove("active");
            startBtn.innerText = "📷 Start Camera";
            startBtn.style.background = "linear-gradient(90deg, #ff4b2b, #ff416c)";
        }
    });

    videoFeed.onload = function () {
        videoFeed.style.opacity = "1";
    };
    videoFeed.style.opacity = "0";
});
