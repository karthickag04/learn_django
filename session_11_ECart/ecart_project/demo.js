 const serviceLink = document.getElementById('service');
        serviceLink.addEventListener('mouseover', function() {
            this.style.color = 'yellow';
        });

        serviceLink.addEventListener('mouseout', function() {
            this.style.color = '';
        });

        serviceLink.addEventListener('mousedown', function() {
            this.style.color = 'gray';
        });

        serviceLink.addEventListener('mouseup', function() {
            this.style.color = 'blue';
        });
