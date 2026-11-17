
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
document.addEventListener('DOMContentLoaded', function () {
    const checkIn = document.getElementById('id_check_in');
    const checkOut = document.getElementById('id_check_out');

    if (!checkIn || !checkOut) return;

    const today = new Date();
    const localToday = new Date(
        today.getTime() - today.getTimezoneOffset() * 60000
    ).toISOString().split('T')[0];

    checkIn.min = localToday;
    checkOut.min = localToday;

    checkIn.addEventListener('change', function () {
        if (checkIn.value) {
            const nextDay = new Date(checkIn.value + 'T00:00:00');
            nextDay.setDate(nextDay.getDate() + 1);

            const minimumCheckout = [
                nextDay.getFullYear(),
                String(nextDay.getMonth() + 1).padStart(2, '0'),
                String(nextDay.getDate()).padStart(2, '0')
            ].join('-');

            checkOut.min = minimumCheckout;

            if (checkOut.value && checkOut.value < minimumCheckout) {
                checkOut.value = '';
            }
        }
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const calculator = document.getElementById('booking-price-calculator');
    const checkIn = document.getElementById('id_check_in');
    const checkOut = document.getElementById('id_check_out');

    if (!calculator || !checkIn || !checkOut) return;

    const pricePerNight = parseFloat(calculator.dataset.price);

    const nightsDisplay = document.getElementById('number-of-nights');
    const totalDisplay = document.getElementById('total-booking-price');

    const currency = new Intl.NumberFormat('en-NG', {
        style: 'currency',
        currency: 'NGN'
    });

    function calculateBookingPrice() {
        if (!checkIn.value || !checkOut.value) {
            nightsDisplay.textContent = '0';
            totalDisplay.textContent = 'Select your dates';
            return;
        }

        const checkInDate = new Date(checkIn.value + 'T00:00:00');
        const checkOutDate = new Date(checkOut.value + 'T00:00:00');

        const nights = Math.round(
            (checkOutDate - checkInDate) / (1000 * 60 * 60 * 24)
        );

        if (nights <= 0) {
            nightsDisplay.textContent = '0';
            totalDisplay.textContent = 'Invalid dates';
            return;
        }

        const totalPrice = nights * pricePerNight;

        nightsDisplay.textContent = nights;
        totalDisplay.textContent = currency.format(totalPrice);
    }

    checkIn.addEventListener('change', calculateBookingPrice);
    checkOut.addEventListener('change', calculateBookingPrice);

    calculateBookingPrice();
});
