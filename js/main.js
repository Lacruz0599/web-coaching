document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener('click', function (e) {

        const targetSelector = this.getAttribute('href');

        if (!targetSelector || targetSelector === '#') {
            return;
        }

        let target;

        try {
            target = document.querySelector(targetSelector);
        } catch (error) {
            return;
        }

        if (!target) {
            return;
        }

        e.preventDefault();

        target.scrollIntoView({
            behavior: 'smooth'
        });

    });

});
