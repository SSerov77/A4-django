document.getElementById('file-upload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const btn = document.getElementById('upload-label')
            const preview = document.getElementById('preview');
            preview.src = e.target.result;
            btn.style.display = 'none';
            preview.style.display = 'block';
        
        }
        reader.readAsDataURL(file);
    }
});