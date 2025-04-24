// document.addEventListener('DOMContentLoaded', function () {
//     const toggles = document.querySelectorAll('.toggle-submenu');

//     toggles.forEach(toggle => {
//         toggle.addEventListener('click', function () {
//             const targetId = this.getAttribute('data-target');
//             const target = document.querySelector(targetId);

//             document.querySelectorAll('.submenu').forEach(submenu => {
//                 if (submenu !== target) {
//                     submenu.classList.remove('show');
//                 }
//             });

//             target.classList.toggle('show');
//         });
//     });

//     // Dynamic loading of content
//     // const links = document.querySelectorAll('.');
//     // links.forEach(link => {
//     //     link.addEventListener('click', e => {
//     //         e.preventDefault();
//     //         const url = link.getAttribute('href');

//     //         // Clear the #main-content div before loading new content
//     //         const mainContent = document.getElementById('main-content');
//     //         mainContent.innerHTML = ''; // Clear existing content

//     //         fetch(url)
//     //             .then(res => res.json())
//     //             .then(data => {
//     //                 mainContent.innerHTML = data.html; // Load new content
//     //                 history.pushState(null, '', url); // Update browser path
//     //             });
//     //     });
//     // }); 

//     // // Handle browser back/forward
//     // window.addEventListener('popstate', () => {
//     //     fetch(location.pathname)
//     //         .then(res => res.json())
//     //         .then(data => {
//     //             document.getElementById('main-content').innerHTML = data.html;
//     //         });
//     // }); 
// });


document.addEventListener("DOMContentLoaded", function () {
    // Get the current path
    const currentPath = window.location.pathname;

    // Find all sidebar links
    const sidebarLinks = document.querySelectorAll(".sidebar a");

    // Loop through each link
    sidebarLinks.forEach(link => {
        // Check if the link's href matches the current path
        if (link.getAttribute("href") === currentPath) {
            // Add the 'active' class to the link
            link.classList.add("active");

            // Check if the link is inside a submenu
            const submenu = link.closest(".submenu");
            if (submenu) {
                // Expand the submenu
                submenu.classList.add("show");

                // Find the parent toggle link and rotate its chevron
                const toggleLink = submenu.previousElementSibling;
                if (toggleLink && toggleLink.classList.contains("toggle-submenu")) {
                    toggleLink.querySelector(".fas.fa-chevron-right").classList.add("rotate");
                }
            }
        }
    });

    // Add click event listeners to toggle submenu visibility
    const toggleLinks = document.querySelectorAll(".toggle-submenu");
    toggleLinks.forEach(toggle => {
        toggle.addEventListener("click", function () {
            const target = document.querySelector(this.getAttribute("data-target"));
            
            // Close all other submenus
            document.querySelectorAll(".submenu").forEach(submenu => {
                if (submenu !== target) {
                    submenu.classList.remove("show");
                }
            });

            // Toggle the current submenu
            if (target) {
                target.classList.toggle("show");
                const chevron = this.querySelector(".fas.fa-chevron-right");
                if (chevron) {
                    chevron.classList.toggle("rotate");
                }
            }

            // Rotate chevrons for all toggle links
            toggleLinks.forEach(link => {
                const chevron = link.querySelector(".fas.fa-chevron-right");
                if (link === this) {
                    chevron.classList.toggle("rotate");
                } else {
                    chevron.classList.remove("rotate");
                }
            });
        });
    });
});