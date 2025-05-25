const servicePrices = {
    'sound_equipment': 15000,
    'light_equipment': 10000,
    'stage_structures': 20000,
    'special_effects': 12000,
    'technical_support': 25000
};

function updateTotalAmount() {
    const checkboxes = document.querySelectorAll('.service-checkbox-input');
    let total = 0;
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            total += servicePrices[checkbox.value];
        }
    });
    document.getElementById('total-amount').textContent = total + ' ?';
    document.getElementById('total-amount-input').value = total;
}


window.addEventListener('load', () => {
    updateTotalAmount();
});


document.querySelectorAll('.service-checkbox-input').forEach(checkbox => {
    checkbox.addEventListener('change', updateTotalAmount);
});