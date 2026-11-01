
document.addEventListener("DOMContentLoaded", () => {
    const bookingForm = document.getElementById("bookingForm");
    const bookingDate = document.getElementById("id_booking_date");
    const today = new Date();
    const todayString = new Date(today.getTime() - today.getTimezoneOffset() * 60000).toISOString().split("T")[0];

    if (bookingDate) {
        bookingDate.min = todayString;
    }

    if (bookingForm) {
        bookingForm.addEventListener("submit", () => {
            const button = bookingForm.querySelector(".confirm-button");
            button.textContent = "Submitting booking...";
            button.disabled = true;
        });
    }
});
