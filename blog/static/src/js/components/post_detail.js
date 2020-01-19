function postDetail() {
    const showPost = document.querySelectorAll('.post-show'),
        modal = document.querySelector('.post-detail'),
        cancelModal = modal.querySelector('.detail-close'),
        photoModal = modal.querySelector('.detail-photo'),
        titleModal = modal.querySelector('.detail-title'),
        dateModal = modal.querySelector('.detail-date'),
        authorModal = modal.querySelector('.detail-author');

    function showDetail() {
        modal.style.display = "block";
        console.log(this.parentElement);
        photoModal.src = this.parentElement.querySelector('.post-photo').src;
        titleModal.textContent = this.parentElement.dataset.title;
        dateModal.textContent = this.parentElement.querySelector('.post-date').textContent;
        authorModal.textContent = this.parentElement.querySelector('.post-author').textContent;
    }

    function hidePost() {
        modal.style.display = 'none';
    }

    for(let i=0; i<showPost.length; i++) {
        showPost[i].addEventListener('click', showDetail);
    }
    cancelModal.addEventListener('click', hidePost);
}

document.addEventListener("DOMContentLoaded", postDetail);