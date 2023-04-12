fetch("http://127.0.0.1:5000", { mode: 'cors' })
  .then((response) => response.json())
  .then((data) => console.log(data));