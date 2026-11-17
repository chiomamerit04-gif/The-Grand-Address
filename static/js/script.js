const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');
const navActions = document.querySelector('.nav-actions');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        navActions.classList.toggle('active');
    });
}

// Homepage date restrictions
document.addEventListener('DOMContentLoaded', () => {
    const checkIn = document.getElementById('checkin');
    const checkOut = document.getElementById('checkout');

    if (!checkIn || !checkOut) return;

    const today = new Date();
    const localToday = new Date(
        today.getTime() - today.getTimezoneOffset() * 60000
    ).toISOString().split('T')[0];

    checkIn.min = localToday;
    checkOut.min = localToday;

    checkIn.addEventListener('change', () => {
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
