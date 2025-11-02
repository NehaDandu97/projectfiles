const form=document.querySelector('.form')
const input=document.querySelector('.form-input')


// const form=document.querySelector(".form")
form.addEventListener('submit',(event)=>{
validate();
event.preventDefault()
})
const validate=()=>{
    let inVal=input.value(5+6);

}