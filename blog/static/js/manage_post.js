document.addEventListener("DOMContentLoaded", function(event) {
    const publishedDate = document.querySelector('#publishedDate').parentElement,
        options = document.querySelectorAll('#managePost input'),
        laterPublish = document.querySelector('#managePost_1');

    publishedDate.style.display = 'none';

    for (let i = 0; i < options.length; i++) {
        options[i].addEventListener('change', function() {
            if(laterPublish.checked === true) {
                publishedDate.style.display = 'block';
            } else {
                publishedDate.style.display = 'none';
            }
        });
    }
})