"use strict";

// function for menu mobile
(() => {
  const menuIcon = document.querySelector('.C-nav__menu_mobile');
  const menuUl = document.querySelector('.C-nav__ul');

  menuIcon.addEventListener("click", () => {
    menuUl.classList.toggle('C-nav__is_disable');
  })
})();