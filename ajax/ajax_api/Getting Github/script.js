async function getCoderData() {
  var response = await fetch("https://api.github.com/users/Nbfern90");

  var coderData = await response.json();
  console.log(coderData);
  document.getElementById("info").innerHTML = coderData.followers;
  return coderData;
}
