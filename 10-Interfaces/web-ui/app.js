(function() {
  const API = '../preprocess_full.jsonl';
  let chunks = [];

  const $ = id => document.getElementById(id);
  const query = $('query');
  const btn = $('search-btn');
  const reloadBtn = $('reload-btn');
  const results = $('results');
  const loading = $('loading');
  const stats = $('stats');
  const chunkCount = $('chunk-count');

  async function loadIndex() {
    loading.classList.remove('hidden');
    results.innerHTML = '';
    stats.textContent = 'Baixando índice…';
    try {
      const resp = await fetch(API);
      const text = await resp.text();
      chunks = text.split('\n').filter(Boolean).map(l => JSON.parse(l));
      stats.textContent = `${chunks.length} chunks carregados. Digite uma busca.`;
      chunkCount.textContent = chunks.length;
    } catch (e) {
      stats.textContent = 'Erro ao carregar índice. Verifique se preprocess_full.jsonl existe.';
    }
    loading.classList.add('hidden');
  }

  function highlight(text, term) {
    if (!term) return text;
    const re = new RegExp(`(${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return text.replace(re, '<mark>$1</mark>');
  }

  function search(term) {
    if (!term.trim()) return;
    const t = term.toLowerCase();
    const found = chunks.filter(c => c.text && c.text.toLowerCase().includes(t));
    const elapsed = found.length;

    results.innerHTML = '';
    stats.textContent = `${elapsed} resultado(s) para "${term}"`;

    if (elapsed === 0) {
      results.innerHTML = '<div class="result-card">Nenhum resultado encontrado.</div>';
      return;
    }

    found.slice(0, 50).forEach(c => {
      const card = document.createElement('div');
      card.className = 'result-card';
      const title = c.metadata?.title || c.source || 'desconhecido';
      card.innerHTML = `
        <h3>📄 ${highlight(title, term)}</h3>
        <div class="meta">${c.metadata?.tags?.join(', ') || ''} — ${c.metadata?.nivel || ''}</div>
        <div class="text">${highlight(c.text, term)}</div>
      `;
      results.appendChild(card);
    });
  }

  btn.addEventListener('click', () => search(query.value));
  query.addEventListener('keydown', e => { if (e.key === 'Enter') search(query.value); });
  reloadBtn.addEventListener('click', loadIndex);

  loadIndex();
})();
