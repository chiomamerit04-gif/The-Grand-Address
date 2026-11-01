
document.addEventListener("DOMContentLoaded", () => {
    const saveButton = document.getElementById("saveProperty");
    const shareButton = document.getElementById("shareProperty");
    const readMoreButton = document.getElementById("readMore");
    const bookingForm = document.getElementById("detailsBookingForm");
    const checkin = document.getElementById("detailsCheckin");
    const checkout = document.getElementById("detailsCheckout");
    const priceBreakdown = document.getElementById("priceBreakdown");
    const nightCount = document.getElementById("nightCount");
    const stayCost = document.getElementById("stayCost");
    const serviceFee = document.getElementById("serviceFee");
    const totalCost = document.getElementById("totalCost");
    const propertyPrice = 180000;
    const formatCurrency = amount => "₦" + amount.toLocaleString("en-NG");
    const today = new Date();
    const todayString = new Date(today.getTime() - today.getTimezoneOffset() * 60000).toISOString().split("T")[0];
    checkin.min = todayString;
    checkout.min = todayString;
    saveButton.addEventListener("click", () => {
        const saved = saveButton.classList.toggle("saved");
        saveButton.textContent = saved ? "♥ Saved" : "♡ Save";
    });
    shareButton.addEventListener("click", async () => {
        try {
            if (navigator.share) {
                await navigator.share({ title: document.title, url: window.location.href });
            } else if (navigator.clipboard) {
                await navigator.clipboard.writeText(window.location.href);
                shareButton.textContent = "✓ Link copied";
            } else {
                alert("Copy this page's URL from your browser to share it.");
            }
        } catch (error) {
            if (error.name !== "AbortError") alert("Unable to share this page.");
        }
    });
    readMoreButton.addEventListener("click", () => {
        const paragraphs = document.querySelectorAll(".details-section:first-of-type > p");
        paragraphs.forEach((paragraph, index) => {
            if (index > 0) paragraph.hidden = !paragraph.hidden;
        });
        readMoreButton.textContent = readMoreButton.textContent === "Read more" ? "Show less" : "Read more";
    });
    checkin.addEventListener("change", () => {
        checkout.min = checkin.value || todayString;
        if (checkout.value && checkout.value <= checkin.value) checkout.value = "";
        priceBreakdown.hidden = true;
    });
    checkout.addEventListener("change", () => {
        priceBreakdown.hidden = true;
    });
    bookingForm.addEventListener("submit", event => {
        event.preventDefault();
        if (!checkin.value || !checkout.value) {
            alert("Please select your check-in and check-out dates.");
            return;
        }
        const startDate = new Date(checkin.value + "T00:00:00");
        const endDate = new Date(checkout.value + "T00:00:00");
        const nights = Math.round((endDate - startDate) / 86400000);
        if (nights <= 0) {
            alert("Your check-out date must be after your check-in date.");
            return;
        }
        const accommodationCost = propertyPrice * nights;
        const fee = Math.round(accommodationCost * 0.10);
        nightCount.textContent = nights;
        stayCost.textContent = formatCurrency(accommodationCost);
        serviceFee.textContent = formatCurrency(fee);
        totalCost.textContent = formatCurrency(accommodationCost + fee);
        priceBreakdown.hidden = false;
    });
    document.getElementById("viewAllPhotos").addEventListener("click", () => {
        document.querySelector(".property-gallery").scrollIntoView({ behavior: "smooth", block: "center" });
    });
    document.getElementById("showAmenities").addEventListener("click", () => {
        document.querySelector(".amenities-grid").scrollIntoView({ behavior: "smooth", block: "center" });
    });
});
