function Couleur() 
{
  let r = Number(document.getElementById("rouge").value);
  let v = Number(document.getElementById("vert").value);
  let b = Number(document.getElementById("bleu").value);
  let rhexa = r.toString(16);
  let vhexa = v.toString(16);
  let bhexa = b.toString(16);
  let couleur = '#'+rhexa+vhexa+bhexa;
  console.log(couleur);
  document.body.style.backgroundColor = couleur;
}
