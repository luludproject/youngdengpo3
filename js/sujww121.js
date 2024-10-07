var jsonldData = {
  "@context": "https://schema.org",
  "@type": "Organization",
  url: "https://sd.jianhomecare.com",
  logo: "https://sd.jianhomecare.com/img/변기막힘하수구막힘.png",
};

var script = document.createElement("script");
script.type = "application/ld+json";
script.text = JSON.stringify(jsonldData);
document.head.appendChild(script);
