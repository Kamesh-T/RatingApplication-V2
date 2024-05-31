document.addEventListener('contextmenu',function(e){
    window.alert("Contextmenu Event Disabled");
    e.preventDefault();
});

document.getElementById('up-arr').addEventListener('click',function ()  {
    window.scrollTo({
        top:0,
    })
})