const project_link = document.querySelector(".overview-link-projects")
const project_box = document.querySelector(".overview-item-projects")
const about_link = document.querySelector(".overview-link-about")
const about_box = document.querySelector(".overview-item-about")
const contact_link = document.querySelector(".overview-link-contact")
const contact_box = document.querySelector(".overview-item-contact")
const experience_link = document.querySelector(".overview-link-experience")
const experience_box = document.querySelector(".overview-item-experience")

const sections = document.querySelectorAll('.section');
const navLinks = {
    'about-content': { box: about_box, link: about_link },
    'experience-content': { box: experience_box, link: experience_link },
    'project-content': { box: project_box, link: project_link },
    'contact-content': { box: contact_box, link: contact_link }
};

const setActiveSection = (entries) => {
    let maxIntersectRatio = 0;
    let activeSectionId = null;

    entries.forEach((entry) => {
        const { target, intersectionRatio } = entry;

        if (intersectionRatio > maxIntersectRatio) {
            maxIntersectRatio = intersectionRatio;
            activeSectionId = target.id;
        }
    });

    if (activeSectionId) {
        setStylesForSection(activeSectionId);
    }
};

const setStylesForSection = (sectionId) => {
    Object.keys(navLinks).forEach((key) => {
        const { box, link } = navLinks[key];
        box.style.width = "";
        link.style.marginLeft = "";
    });

    const { box, link } = navLinks[sectionId];
    box.style.width = "40px";
    link.style.marginLeft = "50px";
};

const section_observer = new IntersectionObserver(setActiveSection, {
    threshold: 0.5, // Adjust the threshold as needed
});

sections.forEach((section) => section_observer.observe(section));

