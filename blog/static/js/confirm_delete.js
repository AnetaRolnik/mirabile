
document.addEventListener("DOMContentLoaded", function(event) {
    const deletePost = document.querySelectorAll('.post-delete');
    const modal = document.querySelector('.confirm-delete');
    const cancelModal = document.querySelector('.modal-cancel');

    function showModal() {
        const image = this.parentElement.querySelector('img').src;
        modal.querySelector('img').src = image;
        modal.style.display = 'block';
    }

    function hideModal() {
        modal.style.display = 'none';
    }

    for(let i=0; i<deletePost.length; i++) {
        deletePost[i].addEventListener('click', showModal);
    }
    cancelModal.addEventListener('click', hideModal);
});
