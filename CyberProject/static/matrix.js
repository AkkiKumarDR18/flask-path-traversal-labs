const canvas = document.getElementById("matrixCanvas");
const ctx = canvas.getContext("2d");

// Set full screen
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Matrix Code Effect
const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()*&^?/|><.,:;'{}[]_-+=%";
const fontSize = 18;
const columns = Math.floor(canvas.width / fontSize);
const drops = Array(columns).fill(1);

function drawMatrix() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0F0";
    ctx.font = fontSize + "px monospace";

    drops.forEach((y, i) => {
        const text = letters.charAt(Math.floor(Math.random() * letters.length));
        ctx.fillText(text, i * fontSize, y * fontSize);
        
        if (y * fontSize > canvas.height || Math.random() > 0.95) {
            drops[i] = 0;
        }
        drops[i]++;
    });
}

// Start Animation
setInterval(drawMatrix, 50);

// Adjust canvas on resize
window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
