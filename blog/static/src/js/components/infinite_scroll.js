// function infiniteScroll() {
//     const collection = document.querySelector('.collection');

//     collection.addEventListener('scroll', function() {
//         if (collection.scrollTop + collection.clientHeight >= collection.scrollHeight) {
//             for (let i = 0; i < 20; i++) {
//                 const post = document.createElement('div');
//                 post.className = 'collection-post';
//                 post.innerHTML = `
//                     <a class='post-show'>
//                         <div class="post-metadata">
//                             <span class='post-author'></span>
//                             <span class='post-date'></span>
//                         </div>
//                         <img class='post-photo' src=''>
//                     </a>`;
//                 collection.appendChild(post);
//             }
//         }
//     });
// }

// document.addEventListener("DOMContentLoaded", infiniteScroll);