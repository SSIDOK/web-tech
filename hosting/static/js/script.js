const questions = document.querySelectorAll(".question");

questions.forEach(function (question) {
  question.addEventListener("click", function () {
    question.classList.toggle("open");
  });
});
$('.icon').click(function(){
    $('span').toggleClass("cancel");
  });
  window.addEventListener('scroll', function() {
  var nav = document.querySelector('nav');
  var screenWidth = window.innerWidth;

  if (screenWidth > 1040) {
     nav.classList.toggle('scrolled', window.scrollY > 90);
  }
  });
  $(document).ready(function(){
 $('.customer-logos').slick({
     slidesToShow: 5,
     slidesToScroll: 1,
     autoplay: true,
     autoplaySpeed: 1500,
     arrows: false,
     dots: false,
     pauseOnHover:false,
     responsive: [{
         breakpoint: 1040,
         settings: {
             slidesToShow:3
         }
     }, {
         breakpoint: 520,
         settings: {
             slidesToShow: 2
         }
     }]
 });
});

const createOdometer = (el, value) => {
    const odometer = new Odometer({
      el: el,
      value: 0,
    });

    let hasRun = false;

    const options = {
      threshold: [0, 0.9],
    };

    const callback = (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          if (!hasRun) {
            odometer.update(value);
            hasRun = true;
          }
        }
      });
    };

    const observer = new IntersectionObserver(callback, options);
    observer.observe(el);
  };

  const subscribersOdometer = document.querySelector(".subscribers-odometer");
  createOdometer(subscribersOdometer, 850);

  const videosOdometer = document.querySelector(".videos-odometer");
  createOdometer(videosOdometer, 790);

  const projectsOdometer = document.querySelector(".projects-odometer");
  createOdometer(projectsOdometer, 89);

  function checkDomain() {
    var inputVal = document.getElementById("domainInput").value.trim();
    var zoneVal = document.getElementById("zoneSelect").value;
    var messageContainer = document.getElementById("messageContainer");
    messageContainer.innerHTML = ""; // Clear previous messages

    // Перевірка правильності введення домену
    var domainRegex = /^[a-zA-Z0-9.-]+$/; // Регулярний вираз для перевірки формату домену
    if (!domainRegex.test(inputVal)) {
      showMessage("Please enter a valid domain name.", "error");
      return;
    }

    var button = document.querySelector(".input-container button");
    button.disabled = true;
    button.innerText = "Checking...";

    var apiKey = "at_kXQfh4WtAm7zvRGYDJ1FlMRTU0unL";
    var domain = inputVal.toLowerCase() + zoneVal; // Додати обрану зону до домену

    fetch(
      `https://domain-availability.whoisxmlapi.com/api/v1?apiKey=${apiKey}&domainName=${domain}`
    )
      .then((response) => response.json())
      .then((data) => {
        button.disabled = false;
        button.innerText = "Check Domain";

        if (data.DomainInfo.domainAvailability === "UNAVAILABLE") {
          showMessage(
            `The domain "${data.DomainInfo.domainName}" is not available.`,
            "error"
          );
        } else {
          showMessage(
            `The domain "${data.DomainInfo.domainName}" is available.`,
            "success"
          );
        }
      })
      .catch((error) => {
        button.disabled = false;
        button.innerText = "Check Domain";
        showMessage(
          "An error occurred while checking the domain availability.",
          "error"
        );
        console.error("Error:", error);
      });
  }

  function isValidDomain(domain) {
    // Перевірка за допомогою регулярного виразу
    var domainRegex = /^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return domainRegex.test(domain);
  }

  function showMessage(message, type) {
    var messageContainer = document.getElementById("messageContainer");
    var messageElement = document.createElement("div");
    messageElement.textContent = message;
    messageElement.classList.add("message", type);
    messageContainer.appendChild(messageElement);
  }