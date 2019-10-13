export default function confirmDelete() {
    const deletePost = document.querySelectorAll('.post-delete'),
    modal = document.querySelector('.confirm-delete'),
    cancelModal = modal.querySelector('.modal-cancel'),
    imageModal = modal.querySelector('img'),
    formModal = modal.querySelector('form');

    function showModal() {
        modal.style.display = 'block';
        imageModal.src = this.parentElement.querySelector('img').src;
        formModal.action = this.dataset.url;
    }

    function hideModal() {
        modal.style.display = 'none';
    }

    for(let i=0; i<deletePost.length; i++) {
        deletePost[i].addEventListener('click', showModal);
    }
    cancelModal.addEventListener('click', hideModal);
}
