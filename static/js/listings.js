
document.addEventListener("DOMContentLoaded", () => {
    const propertyGrid = document.getElementById("listingPropertyGrid");
    if (!propertyGrid) return;
    const cards = Array.from(propertyGrid.querySelectorAll(".listing-card"));
    const priceRange = document.getElementById("priceRange");
    const priceValue = document.getElementById("priceValue");
    const resultsCount = document.getElementById("resultsCount");
    const noResults = document.getElementById("noResults");
    const sortSelect = document.getElementById("sortProperties");
    const searchForm = document.getElementById("listingSearchForm");
    const destinationInput = document.getElementById("destination");
    const checkinInput = document.getElementById("checkin");
    const checkoutInput = document.getElementById("checkout");
    const clearButton = document.getElementById("clearFilters");
    const resetButton = document.getElementById("resetSearch");
    const getCheckedValues = name => Array.from(document.querySelectorAll(`input[name="${name}"]:checked`)).map(input => input.value);
    function filterProperties() {
        const maxPrice = Number(priceRange.value);
        const locations = getCheckedValues("location");
        const types = getCheckedValues("type");
        const bedrooms = document.querySelector('input[name="bedrooms"]:checked')?.value || "";
        const amenities = getCheckedValues("amenity");
        const destination = destinationInput.value.trim().toLowerCase();
        let visibleCards = [];
        cards.forEach(card => {
            const location = card.dataset.location;
            const type = card.dataset.type;
            const price = Number(card.dataset.price);
            const bedroomCount = Number(card.dataset.bedrooms);
            const cardAmenities = card.dataset.amenities.split(",");
            const cardText = card.textContent.toLowerCase();
            const locationMatch = locations.length === 0 || locations.includes(location);
            const typeMatch = types.length === 0 || types.includes(type);
            const priceMatch = price <= maxPrice;
            const bedroomMatch = !bedrooms || (bedrooms === "4" ? bedroomCount >= 4 : bedroomCount === Number(bedrooms));
            const amenitiesMatch = amenities.every(amenity => cardAmenities.includes(amenity));
            const destinationMatch = !destination || cardText.includes(destination);
            const isVisible = locationMatch && typeMatch && priceMatch && bedroomMatch && amenitiesMatch && destinationMatch;
            card.hidden = !isVisible;
            if (isVisible) visibleCards.push(card);
        });
        resultsCount.textContent = visibleCards.length;
        noResults.hidden = visibleCards.length !== 0;
        sortProperties(visibleCards);
    }
    function sortProperties(visibleCards = cards.filter(card => !card.hidden)) {
        const sortValue = sortSelect.value;
        visibleCards.sort((a, b) => {
            const priceA = Number(a.dataset.price);
            const priceB = Number(b.dataset.price);
            const ratingA = Number(a.dataset.rating);
            const ratingB = Number(b.dataset.rating);
            if (sortValue === "price-low") return priceA - priceB;
            if (sortValue === "price-high") return priceB - priceA;
            if (sortValue === "rating") return ratingB - ratingA;
            return cards.indexOf(a) - cards.indexOf(b);
        });
        visibleCards.forEach(card => propertyGrid.appendChild(card));
    }
    function clearFilters() {
        document.querySelectorAll('input[name="location"], input[name="type"], input[name="amenity"], input[name="bedrooms"]').forEach(input => {
            input.checked = false;
        });
        priceRange.value = 500000;
        priceValue.textContent = "500,000";
        destinationInput.value = "";
        checkinInput.value = "";
        checkoutInput.value = "";
        sortSelect.value = "recommended";
        filterProperties();
    }
    priceRange.addEventListener("input", () => {
        priceValue.textContent = Number(priceRange.value).toLocaleString("en-NG");
        filterProperties();
    });
    document.querySelectorAll('.filters-sidebar input[type="checkbox"], .filters-sidebar input[type="radio"]').forEach(input => {
        input.addEventListener("change", filterProperties);
    });
    destinationInput.addEventListener("input", filterProperties);
    sortSelect.addEventListener("change", filterProperties);
    searchForm.addEventListener("submit", event => {
        event.preventDefault();
        if (checkinInput.value && checkoutInput.value && checkoutInput.value <= checkinInput.value) {
            alert("Check-out date must be after check-in date.");
            return;
        }
        filterProperties();
        document.querySelector(".listings-section").scrollIntoView({ behavior: "smooth" });
    });
    clearButton.addEventListener("click", clearFilters);
    resetButton.addEventListener("click", clearFilters);
    document.querySelectorAll(".favourite-btn").forEach(button => {
        button.addEventListener("click", () => {
            const isFavourite = button.classList.toggle("is-favourite");
            button.textContent = isFavourite ? "♥" : "♡";
            button.setAttribute("aria-label", isFavourite ? "Remove from favourites" : "Add to favourites");
        });
    });
    filterProperties();
});
