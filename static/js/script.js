// Укажите путь к вашему файлу .txt
fetch('/home/firestormwebapp/webapp/templates/name.txt', { method: 'get', mode: 'cors' })
    .then(response => {
        if (!response.ok) throw new Error('Ошибка загрузки');
        return response.text();
    })
    .then(text => {
        document.getElementById('content').textContent = text;
    })
    .catch(error => {
        console.error('Ошибка:', error);
        document.getElementById('content').textContent = 'Файл не загружен.';
    });