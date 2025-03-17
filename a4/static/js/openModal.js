// Получаем элементы DOM
const modal = document.getElementById("ModalWindow");
const openModalBtn = document.getElementById("openModalWindow");
const closeModalBtn = document.querySelector(".close");

// Открываем модальное окно
openModalBtn.addEventListener("click", function () {
    modal.style.display = "block";
});

// Закрываем модальное окно при клике на крестик
closeModalBtn.addEventListener("click", function () {
    modal.style.display = "none";
});

// Закрываем модальное окно при клике вне его области
window.addEventListener("click", function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});