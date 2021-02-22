document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("button").forEach((button) => {
    button.onclick = () => {
      const name = document.querySelector("#name").value;
      const heading = document.querySelector("#hello");
      if (heading) {
        heading.innerHTML = `Hello, ${name}!`;
      }

      document.querySelector("#hello").style.color = button.dataset.color;
    };
  });

  document.querySelector("#selection").onchange = function () {
    document.querySelector("#wish").style.color = this.value;
  };

  document.querySelector("#wishes").onchange = function () {
    document.querySelector("#wish").innerHTML = this.value;
  };
});
