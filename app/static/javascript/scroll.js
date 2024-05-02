const handleScroll = (event) => {
    event.preventDefault();
  
    const articlesSection = document.getElementById("articles");
    if (articlesSection) {
      articlesSection.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  };
  