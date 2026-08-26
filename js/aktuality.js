document.addEventListener('DOMContentLoaded', function () {
  var listEl = document.getElementById('feed-list');
  var sourcesEl = document.getElementById('feed-sources');
  if (!listEl) return;

  fetch('data/aktuality.json', { cache: 'no-store' })
    .then(function (r) { return r.json(); })
    .then(function (entries) {
      renderFeed(entries);
    })
    .catch(function (err) {
      listEl.innerHTML = '<p style="text-align:center;color:rgba(247,244,236,0.6);">Kroniku se nepodařilo načíst.</p>';
      console.error(err);
    });

  function renderFeed(entries) {
    listEl.innerHTML = '';
    var lastYear = null;
    entries.forEach(function (e) {
      if (e.year !== lastYear) {
        var divider = document.createElement('div');
        divider.className = 'feed-year-divider';
        divider.textContent = e.year;
        listEl.appendChild(divider);
        lastYear = e.year;
      }

      var post = document.createElement('div');
      post.className = 'feed-post';

      var dateEl = document.createElement('span');
      dateEl.className = 'feed-date';
      dateEl.textContent = e.date;
      post.appendChild(dateEl);

      var textWrap = document.createElement('div');
      textWrap.className = 'feed-text';
      textWrap.innerHTML = e.text || '';

      if (e.photo) {
        var photoWrap = document.createElement('div');
        photoWrap.className = 'feed-photo';
        var img = document.createElement('img');
        img.src = e.photo;
        img.alt = e.photoAlt || '';
        img.loading = 'lazy';
        photoWrap.appendChild(img);
        if (e.photoSource) {
          var link = document.createElement('a');
          link.className = 'source-link';
          link.href = e.photoSource;
          link.target = '_blank';
          link.rel = 'noopener';
          link.textContent = 'originál v archivu';
          photoWrap.appendChild(link);
        }
        textWrap.appendChild(photoWrap);
      }

      post.appendChild(textWrap);
      listEl.appendChild(post);
    });

    if (sourcesEl) {
      sourcesEl.innerHTML = 'Zdroje: <a href="https://web.archive.org/web/20130205183233/http://aikidoricany.cz:80/" target="_blank" rel="noopener" style="color:#e9c9a0;">akumulovaná pre-Wix homepage (2006–2017)</a> a Wix-era snapshoty 2018–2026. Tento seznam upravujete v <a href="editor.html" style="color:#e9c9a0;">editoru</a>.';
    }
  }
});
