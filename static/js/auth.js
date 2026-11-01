document.addEventListener("DOMContentLoaded",()=>{
    document.querySelectorAll(".toggle-password").forEach(button=>{
        button.addEventListener("click",()=>{
            const input=document.getElementById(button.dataset.target);
            const icon=button.querySelector("i");
            const isPassword=input.type==="password";
            input.type=isPassword?"text":"password";
            icon.classList.toggle("fa-eye",!isPassword);
            icon.classList.toggle("fa-eye-slash",isPassword);
            button.setAttribute("aria-label",isPassword?"Hide password":"Show password");
        });
    });
});
