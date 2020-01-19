function uploadFile() {
    const inputFile = document.querySelector('#id_photo'),
        file = document.querySelector('#file');

    inputFile.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                file.setAttribute('src', e.target.result);
                file.classList.remove('photo_empty');
                file.classList.add('photo_loaded');
            }
            
            reader.readAsDataURL(this.files[0]);
        }
    });
}

document.addEventListener("DOMContentLoaded", uploadFile);
