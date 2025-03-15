// Получаем элементы DOM
const modal = document.getElementById("reviewModal");
const openModalBtn = document.getElementById("openReviewModal");
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

// Обработка отправки формы
const reviewForm = document.getElementById("reviewForm");
reviewForm.addEventListener("submit", function (event) {
    event.preventDefault(); // Предотвращаем отправку формы

    const reviewText = document.getElementById("reviewText").value;

    // Здесь можно добавить логику для отправки отзыва на сервер
    console.log("Отзыв отправлен:", reviewText);

    // Закрываем модальное окно после отправки
    modal.style.display = "none";

    // Очищаем поле ввода
    document.getElementById("reviewText").value = "";
});