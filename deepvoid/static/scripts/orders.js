// Определяется объект с ценами на услуги
const servicePrices = {
    'sound_equipment': 15000,
    'light_equipment': 10000,
    'stage_structures': 20000,
    'special_effects': 12000,
    'technical_support': 25000
};

// Определяется функция для обновления общей стоимости
function updateTotalAmount() {
    // Получаются все элементы чекбоксов с классом 'service-checkbox-input'
    const checkboxes = document.querySelectorAll('.service-checkbox-input');
    // Инициализируется переменная для хранения общей суммы
    let total = 0;
    // Перебираются все чекбоксы
    checkboxes.forEach(checkbox => {
        // Проверяется, отмечен ли чекбокс
        if (checkbox.checked) {
            // Добавляется стоимость услуги к общей сумме
            total += servicePrices[checkbox.value];
        }
    });
    // Обновляется текстовое содержимое элемента с id 'total-amount'
    document.getElementById('total-amount').textContent = total + ' ?';
    // Обновляется значение скрытого поля ввода с id 'total-amount-input'
    document.getElementById('total-amount-input').value = total;
}

// Добавляется обработчик события загрузки страницы
window.addEventListener('load', () => {
    // Вызывается функция обновления общей стоимости при загрузке страницы
    updateTotalAmount();
});

// Для каждого чекбокса с классом 'service-checkbox-input' добавляется обработчик события
document.querySelectorAll('.service-checkbox-input').forEach(checkbox => {
    // При изменении состояния чекбокса вызывается функция обновления общей стоимости
    checkbox.addEventListener('change', updateTotalAmount);
});