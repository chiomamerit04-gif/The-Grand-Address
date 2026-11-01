document.addEventListener("DOMContentLoaded",()=>{
    const links=document.querySelectorAll(".dashboard-link");
    const sections=document.querySelectorAll(".dashboard-section");
    function showSection(sectionId){
        sections.forEach(section=>section.classList.toggle("active",section.id===sectionId));
        links.forEach(link=>link.classList.toggle("active",link.dataset.section===sectionId));
    }
    links.forEach(link=>{
        link.addEventListener("click",event=>{
            event.preventDefault();
            showSection(link.dataset.section);
        });
    });
    document.querySelectorAll("[data-section]").forEach(link=>{
        if(link.classList.contains("dashboard-link"))return;
        link.addEventListener("click",event=>{
            event.preventDefault();
            showSection(link.dataset.section);
            document.querySelector(".dashboard-main").scrollIntoView({behavior:"smooth"});
        });
    });
    document.querySelectorAll(".remove-saved").forEach(button=>{
        button.addEventListener("click",()=>{
            const property=button.closest(".saved-property");
            property.remove();
        });
    });
});