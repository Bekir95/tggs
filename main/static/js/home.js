var swiper = new Swiper(".asd", {
    slidesPerView: 3,
    spaceBetween: 50,
    slidesPerGroup: 1,
    loop: 'true',
  
    fade:'true',
    gragCursor:'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets:true
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });