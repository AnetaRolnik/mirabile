document.addEventListener("DOMContentLoaded", function(event) {
    const showPost = document.querySelectorAll('.post-show');
    const closePost = document.querySelector('.detail-close');
    const postDetail = document.querySelector('.post-detail');

    function showDetail() {
        postDetail.style.display = "block";
    }

    function hidePost() {
        postDetail.style.display = 'none';
    }

    for(let i=0; i<showPost.length; i++) {
        showPost[i].addEventListener('click', showDetail);
    }
    closePost.addEventListener('click', hidePost);
});