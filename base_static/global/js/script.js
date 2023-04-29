"use strict";

// function for menu mobile
(() => {
  const menuIcon = document.querySelector('.C-nav__menu_mobile');
  const menuUl = document.querySelector('.C-nav__ul');

  menuIcon.addEventListener("click", () => {
    menuUl.classList.toggle('C-nav__is_disable');
  })
})();

// function for select category
(() => {
  const selectCategory = document.querySelector('#select_cat');
  const form = document.querySelector('#form_cat');

  const button = document.querySelector('#btn_form_cat');
  button.addEventListener("click", (event) => {
    event.preventDefault();
    const action = selectCategory.value;
    form.setAttribute('action', action);
    form.submit();
  })
})();