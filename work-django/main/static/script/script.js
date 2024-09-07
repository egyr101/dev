let currentIndex = 0;
const imageSlides = document.getElementsByClassName('image-slide');
const BackButton = document.getElementsByClassName('slide-back');
const NextButton = document.getElementsByClassName('slide-next');
let QuatityImage = 0;
window.addEventListener('load',function (){
          for (let i= 0, max= imageSlides.length;i < max;i++){
               console.log(QuatityImage)
               if (imageSlides[i].getAttribute("src") != '/media/default.jpg'){
                    QuatityImage = QuatityImage+1;
               }
     }
})

function NextSlide (){
     imageSlides[currentIndex].style.display = 'none';
     currentIndex = (currentIndex + 1) % QuatityImage;
     imageSlides[currentIndex].style.display = 'block';
}
function BackSlide (){
     imageSlides[currentIndex].style.display = 'none';
     if (currentIndex===1){
          currentIndex = 0;
          imageSlides[currentIndex].style.display = 'block';
     }
     else if(currentIndex===0){
          currentIndex = QuatityImage - 1;
          imageSlides[currentIndex].style.display = 'block';
     }
     else{
        currentIndex = (currentIndex-1) % QuatityImage;
        imageSlides[currentIndex].style.display = 'block';
     }
}
BackButton.onclick = () =>{
     BackSlide();
}
NextButton.onclick = () =>{
     NextSlide();
}