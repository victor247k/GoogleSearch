const dropDownButton = document.getElementById("appDropdown");
const dropdown = document.querySelector(".dropdown");

dropDownButton.addEventListener('click', () => {
  if (dropdown.style.display === "grid") {
    dropdown.style.display = "none";
  } else {
    dropdown.style.display = "grid";
  }
})
