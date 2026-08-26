document.addEventListener('DOMContentLoaded', function () {
  var nodes = document.querySelectorAll('[data-key]');
  if (!nodes.length) return;

  fetch('data/site-content.json', { cache: 'no-store' })
    .then(function (r) { return r.json(); })
    .then(function (entries) {
      var byKey = {};
      entries.forEach(function (e) { byKey[e.key] = e.text; });
      nodes.forEach(function (el) {
        var key = el.getAttribute('data-key');
        if (byKey.hasOwnProperty(key) && byKey[key] !== '') {
          el.innerHTML = byKey[key];
        }
      });
    })
    .catch(function (err) {
      console.error('content.js: nepodařilo se načíst data/site-content.json', err);
    });
});
