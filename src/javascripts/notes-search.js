import debounce from './helpers/debounce';

//const highlight = (s) => htmlEscape(s).replace(
const highlight = (s) => s.replace(
  /b4de2a49c8/g, '<b class="app-search-highlight">'
).replace(
  /8c94a2ed4b/g, '</b>'
);

const sql = `select
  snippet(notes_fts, -1, 'b4de2a49c8', '8c94a2ed4b', '...', 100) as snippet,
  notes_fts.rank, notes.title, notes.url, notes.author, notes.section, notes.updated_date
from notes
  join notes_fts on notes.rowid = notes_fts.rowid
where notes_fts match :search || "*"
  order by rank limit 5;`

const searchbox = document.getElementById("searchbox");

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
  console.log(d.length)
  let results = d.map(r => `
    <div class="app-search-result__item">
      <h3 class="cj-heading-s app-search-result__item__heading"><a href="${r.url}">${r.title}</a></h3>
      <p class="app-search-result__item__meta notes-list__item__meta">${r.author} - ${r.updated_date}</p>
      <p class="app-search-result__item__snippet">${highlight(r.snippet)}</p>
    </div>
  `).join("");
  document.getElementById("app-search-results").innerHTML = results;
});
}, 100); // debounce every 100ms
