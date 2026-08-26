document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      toggle.classList.toggle('open', isOpen);
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Submenu expand on mobile (tap the parent link's caret area) / hover on desktop
    document.querySelectorAll('.main-nav .has-submenu > a').forEach(function (link) {
      link.addEventListener('click', function (e) {
        if (window.innerWidth <= 900) {
          e.preventDefault();
          link.parentElement.classList.toggle('submenu-open');
        }
      });
    });
  }

  // Lightbox for gallery grids
  var lightbox = document.querySelector('.lightbox');
  if (lightbox) {
    var lightboxImg = lightbox.querySelector('img');
    var closeBtn = lightbox.querySelector('.lightbox-close');
    var prevBtn = lightbox.querySelector('.lightbox-prev');
    var nextBtn = lightbox.querySelector('.lightbox-next');
    var items = Array.prototype.slice.call(document.querySelectorAll('.gallery-grid button'));
    var current = 0;

    function show(index) {
      current = (index + items.length) % items.length;
      var img = items[current].querySelector('img');
      lightboxImg.src = img.getAttribute('src');
      lightboxImg.alt = img.getAttribute('alt') || '';
    }

    items.forEach(function (btn, index) {
      btn.addEventListener('click', function () {
        show(index);
        lightbox.classList.add('open');
      });
    });

    function close() { lightbox.classList.remove('open'); }

    if (closeBtn) closeBtn.addEventListener('click', close);
    if (prevBtn) prevBtn.addEventListener('click', function () { show(current - 1); });
    if (nextBtn) nextBtn.addEventListener('click', function () { show(current + 1); });

    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox) close();
    });

    document.addEventListener('keydown', function (e) {
      if (!lightbox.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
  }
});
