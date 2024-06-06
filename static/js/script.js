// navbar profile
const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");

const profileBtn = document.querySelector("#user-menu-button");
const profileMenu = document.querySelector("#profile-menu");
const closeButton = document.querySelectorAll(".close");

btn.addEventListener("click", () => {
  menu.classList.toggle("hidden");
});

profileBtn.addEventListener("click", () => {
    profileMenu.classList.toggle("hidden");
});

// alert
window.onload = () => {
    const messages = document.querySelectorAll(".alert");
    for (const message of messages) {
        setTimeout(() => message.classList.add("hidden"), 3000);
    }
}

// datetime picker
let dateTimeInput1 = new tempusDominus.TempusDominus(
    document.getElementById("datetimepicker1"),
    {
        display: {
            theme: "light"
        }
    }
  );

let dateTimeInput2 = new tempusDominus.TempusDominus(
    document.getElementById("datetimepicker2"),
    {
        display: {
            theme: "light"
        }
    }
);

document.addEventListener("DOMContentLoaded", function() {
    const pricePerDay = document.querySelector("#priceperday");
    const rentalPriceInput = document.querySelector("#rentalprice");
    const rentalDateInput = document.querySelector("#datetimepicker1Input");
    const returnDateInput = document.querySelector("#datetimepicker2Input");

    function calculateRentalPrice() {
        const rentalDateStr = rentalDateInput.value;
        const returnDateStr = returnDateInput.value;

        if (rentalDateStr && returnDateStr) {
            const rentalDate = new Date(Date.parse(rentalDateStr));
            const returnDate = new Date(Date.parse(returnDateStr));

            const oneDay = 1000 * 60 * 60 * 24;

            const timeDiff = returnDate.getTime() - rentalDate.getTime();

            const totalDays = Math.ceil(timeDiff / oneDay);

            const rentalPrice = totalDays * Number(pricePerDay.value);

            rentalPriceInput.value = rentalPrice;

        }

        console.log(rentalPriceInput);
        console.log(rentalPriceInput.value);
    }

    rentalDateInput.addEventListener("change", calculateRentalPrice);
    returnDateInput.addEventListener("change", calculateRentalPrice);
});

// generate bill