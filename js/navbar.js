document.addEventListener('DOMContentLoaded', () => {
  const burger = document.querySelector('.navbar-burger');

  burger.addEventListener('click', () => {
    const menu = document.getElementById(burger.dataset.target);

    burger.classList.toggle('is-active');
    menu.classList.toggle('is-active');
  });
});
