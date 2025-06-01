// ������������ ������ � ������ �� ������
const servicePrices = {
    'sound_equipment': 15000,
    'light_equipment': 10000,
    'stage_structures': 20000,
    'special_effects': 12000,
    'technical_support': 25000
};

// ������������ ������� ��� ���������� ����� ���������
function updateTotalAmount() {
    // ���������� ��� �������� ��������� � ������� 'service-checkbox-input'
    const checkboxes = document.querySelectorAll('.service-checkbox-input');
    // ���������������� ���������� ��� �������� ����� �����
    let total = 0;
    // ������������ ��� ��������
    checkboxes.forEach(checkbox => {
        // �����������, ������� �� �������
        if (checkbox.checked) {
            // ����������� ��������� ������ � ����� �����
            total += servicePrices[checkbox.value];
        }
    });
    // ����������� ��������� ���������� �������� � id 'total-amount'
    document.getElementById('total-amount').textContent = total + ' ?';
    // ����������� �������� �������� ���� ����� � id 'total-amount-input'
    document.getElementById('total-amount-input').value = total;
}

// ����������� ���������� ������� �������� ��������
window.addEventListener('load', () => {
    // ���������� ������� ���������� ����� ��������� ��� �������� ��������
    updateTotalAmount();
});

// ��� ������� �������� � ������� 'service-checkbox-input' ����������� ���������� �������
document.querySelectorAll('.service-checkbox-input').forEach(checkbox => {
    // ��� ��������� ��������� �������� ���������� ������� ���������� ����� ���������
    checkbox.addEventListener('change', updateTotalAmount);
});