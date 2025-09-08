import { useEffect, useState } from "react";
import "../style/Scroll.css";
import { ArrowUp } from "lucide-react"; // أيقونة سهم طالعة فوق

export default function ScrollToTop() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const toggleVisibility = () => {
      if (window.scrollY > 300) {
        setVisible(true);
      } else {
        setVisible(false);
      }
    };

    window.addEventListener("scroll", toggleVisibility);
    return () => window.removeEventListener("scroll", toggleVisibility);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  if (!visible) return null;

  return (
    <button className="scroll-btn" onClick={scrollToTop}>
      <ArrowUp size={22} color="white" />
    </button>
  );
}
