let currentIndex = 0;
const cards = document.querySelectorAll(".lab-card");

function flipCard(card) {
    card.classList.toggle("flipped");
}

/* Scroll to Next Lab */
function nextLab() {
    if (currentIndex < cards.length - 1) {
        currentIndex++;
        updateCardPosition();
    }
}

/* Scroll to Previous Lab */
function prevLab() {
    if (currentIndex > 0) {
        currentIndex--;
        updateCardPosition();
    }
}

/* Adjust Card Positioning */
function updateCardPosition() {
    cards.forEach((card, index) => {
        if (index === currentIndex) {
            card.style.opacity = "1";
            card.style.zIndex = "10";
            card.style.transform = "translate(-50%, -50%) scale(1)";
        } else {
            card.style.opacity = "0.6";  // Keep previous cards slightly visible
            card.style.zIndex = index < currentIndex ? "5" : "0";
            card.style.transform = `translate(-50%, -50%) scale(${1 - (currentIndex - index) * 0.1})`;
        }
    });
}

/* Initialize first card */
updateCardPosition();

/* Smooth Scrolling on Mouse Wheel */
document.addEventListener("wheel", function (event) {
    event.preventDefault(); // Prevents default scrolling behavior

    if (event.deltaY > 0 && currentIndex < cards.length - 1) {
        nextLab();
    } else if (event.deltaY < 0 && currentIndex > 0) {
        prevLab();
    }
});
