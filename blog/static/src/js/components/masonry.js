document.addEventListener("DOMContentLoaded", function(event) {
    const masonry = new Macy ({
        container: '.collection .container',
        columns: 3,
        margin: 5,
        breakAt: {
            768: 2,
            480: 1,
        },
    });   
});
