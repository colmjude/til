import debounce from './helpers/debounce';

//const highlight = (s) => htmlEscape(s).replace(
const highlight = (s) => s.replace(
  /b4de2a49c8/g, '<b class="app-search-highlight">'
).replace(
  /8c94a2ed4b/g, '</b>'
);

function createResultItem (result) {
  return `
    <div class="app-search-result__item">
      <h3 class="cj-heading-s app-search-result__item__heading"><a href="${result.url}">${result.title}</a></h3>
      <p class="app-search-result__item__meta notes-list__item__meta">${result.author} - ${result.updated_date}</p>
      <p class="app-search-result__item__snippet">${highlight(result.snippet)}</p>
    </div>
  `
}

const sql = `select
  snippet(notes_fts, -1, 'b4de2a49c8', '8c94a2ed4b', '...', 100) as snippet,
  notes_fts.rank, notes.title, notes.url, notes.author, notes.section, notes.updated_date
from notes
  join notes_fts on notes.rowid = notes_fts.rowid
where notes_fts match :search || "*"
  order by rank limit 5;`

function setupShortKey($searchbox) {
  document.addEventListener('keydown', e => {
    if (e.shiftKey && e.ctrlKey && e.key === 'S') {
      // prevent any default action happening
      e.preventDefault();
      // Place your code here
      $searchbox.focus()
    }
  });
}

const searchbox = document.getElementById("searchbox");
setupShortKey(searchbox);

// Used to avoid race-conditions:
let requestInFlight = null;

searchbox.onkeyup = debounce(() => {
const q = searchbox.value;
// Construct the API URL, using encodeURIComponent() for the parameters
const url = (
  "https://datasette-test.onrender.com/notes.json?sql=" +
  encodeURIComponent(sql) +
  `&search=${encodeURIComponent(q)}&_shape=array`
);
// Unique object used just for race-condition comparison
let currentRequest = {};
requestInFlight = currentRequest;
fetch(url).then(r => r.json()).then(d => {
  if (requestInFlight !== currentRequest) {
    // Avoid race conditions where a slow request returns
    // after a faster one.
    return;
  }

  let results = `<p class="cj-body">No notes found.</p>`
  if (d.length) {
    results = d.map(createResultItem).join("");
  }
  document.getElementById("app-search-results").innerHTML = results;
});
}, 100); // debounce every 100ms
