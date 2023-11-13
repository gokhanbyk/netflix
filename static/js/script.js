// $('.acil').click(function (e) { 
//     if($(this).parent().children('.acilmis').hasClass('goster')){
//         $(this).parent().children('.acilmis').removeClass('goster')
    
//     }else{
     
//         $('.acilmis').removeClass('goster')
//         $(this).parent().children('.acilmis').addClass('goster')
//     }
// });

const btn = document.querySelectorAll('.acil')
const acilmis = document.querySelectorAll('.acilmis')
const icon = document.querySelectorAll('.fa-plus')

for(let i of btn){
    i.addEventListener('click',ac)
}
function ac(){
    let acılacak = this.parentElement.children[1]
    console.log()
    if(acılacak.classList.contains('goster')){
        acılacak.classList.toggle('goster')
        this.children[0].classList.toggle('dondur')
    }else{
        acilmis.forEach(e => e.classList.remove('goster'))
        icon.forEach(e => e.classList.remove('dondur'))
        acılacak.classList.toggle('goster')
        this.children[0].classList.toggle('dondur')
    }
}