export default function managePost() {
    const publishedDate = document.querySelector('#publishedDate'),
        options = document.querySelectorAll('#managePost input'),
        laterPublish = document.querySelector('#managePost_1'),
        nowPublish = document.querySelector('#managePost_0');

    nowPublish.checked = true;

    publishedDate !== null ? publishedDate.parentElement.style.display = 'none' : null;

    for (let i = 0; i < options.length; i++) {
        options[i].addEventListener('change', function() {
            if(laterPublish.checked === true) {
                publishedDate.parentElement.style.display = 'block';
            } else {
                publishedDate.parentElement.style.display = 'none';
            }
        });
    }
}
