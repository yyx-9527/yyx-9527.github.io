(() => {
  const button = document.querySelector(".nav-toggle");
  const navigation = document.getElementById("primary-nav");
  const closeMenu = () => {
    button?.setAttribute("aria-expanded", "false");
    navigation?.removeAttribute("data-open");
  };
  if (button && navigation) {
    button.hidden = false;
    button.addEventListener("click", () => {
      const open = button.getAttribute("aria-expanded") !== "true";
      button.setAttribute("aria-expanded", String(open));
      navigation.toggleAttribute("data-open", open);
    });
    navigation.querySelectorAll("a").forEach(link => link.addEventListener("click", closeMenu));
    document.addEventListener("keydown", event => {
      if (event.key === "Escape" && button.getAttribute("aria-expanded") === "true") {
        closeMenu();
        button.focus();
      }
    });
  }

  const links = document.querySelectorAll(".site-links a");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        links.forEach(link => {
          if (link.hash === "#" + entry.target.id) link.setAttribute("aria-current", "location");
          else link.removeAttribute("aria-current");
        });
      });
    }, { rootMargin: "-15% 0px -60% 0px" });
    document.querySelectorAll(".academic-section").forEach(section => observer.observe(section));
  }

  if (navigator.clipboard && window.isSecureContext) {
    document.querySelectorAll(".copy-bibtex").forEach(copyButton => {
      copyButton.hidden = false;
      copyButton.addEventListener("click", async () => {
        const citation = document.getElementById(copyButton.dataset.copyTarget);
        const status = copyButton.parentElement.querySelector(".copy-status");
        try {
          await navigator.clipboard.writeText(citation.textContent.trim());
          status.textContent = "Citation copied.";
        } catch {
          status.textContent = "Copy failed. Please select and copy the citation above.";
        }
      });
    });
  }
})();
