//Event handler for all buttons
let btns = document.querySelectorAll('button');
let text = document.getElementById("hello");
for (i of btns) {
    i.addEventListener('click', function () {
        let color = this.innerHTML;
        if(color==="Blue")
        {
            text.style.color = "Blue"
        }
        else if(color==="Grey"){
            text.style.color = "Grey"
        }
        else
        {
            text.style.color = "Red"

        }
    
});
}