var jsonldData = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: [
    {
      "@type": "Question",
      name: "동대문구 변기막힘 비용은 얼마인가요?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "<p>단순 변기막힘은 50,000원 입니다. 24시간 동대문구 어디든 즉시 출동합니다! 📞 010-3463-4474</p>",
      },
    },
    {
      "@type": "Question",
      name: "변기막힘 100% 뚫어주시나요?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "<p>변기막힘은 100% 뚫어드릴 자신이 있습니다. 저희 지안홈케어는 최신장비와 오랜 노하우가 축적된 현장 시공관리자들로 구성되어 있습니다. 주저말고 연락주세요</p>",
      },
    },
    {
      "@type": "Question",
      name: "동대문구하수구막힘이나 동대문구누수탐지도 가능할까요?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "<p>동대문구하수구막힘 및 동대문구누수탐지 장비를 구비한 현장관리자들이 즉시 출동해 명확한 누수이유와 해결책을 찾아 원만하게 해결해드립니다.</p>",
      },
    },
  ],
};

var script = document.createElement("script");
script.type = "application/ld+json";
script.text = JSON.stringify(jsonldData);
document.head.appendChild(script);
