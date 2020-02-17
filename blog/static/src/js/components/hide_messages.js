function hideMessages() {
    const messages = document.querySelector('.messages');

    if(messages !== null) {
        const close = messages.querySelectorAll('.icon-close');

        setTimeout(function() {
            messages.remove();
        }, 5000);
            
        for(let i=0; i<close.length; i++) {
            close[i].addEventListener('click', function() {
                this.parentElement.remove();
            })
        }
    }
}

document.addEventListener("DOMContentLoaded", hideMessages);
