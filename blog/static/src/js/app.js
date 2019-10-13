import confirmDelete from './components/confirm_delete';
import managePost from './components/manage_post';
import postDetail from './components/post_detail';

document.addEventListener("DOMContentLoaded", function(event) {
    confirmDelete();
    managePost();
    postDetail();
});