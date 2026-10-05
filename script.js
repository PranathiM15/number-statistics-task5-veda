const numbers = document.getElementById("numbers");
const analyzeBtn = document.getElementById("analyzeBtn");
const clearBtn = document.getElementById("clearBtn");
const message = document.getElementById("message");

const smallest = document.getElementById("smallest");
const largest = document.getElementById("largest");
const count = document.getElementById("count");
const sum = document.getElementById("sum");
const average = document.getElementById("average");
const evenList = document.getElementById("evenList");
const oddList = document.getElementById("oddList");

function renderList(element, values) {
  if (!values.length) {
    element.innerHTML = '<span class="empty">No values in this group</span>';
    return;
  }
  element.innerHTML = values.map(value => `<span class="number">${value}</span>`).join("");
}

async function analyze() {
  message.textContent = "";
  const raw = numbers.value.trim();

  if (!raw) {
    message.textContent = "Please enter at least one whole number.";
    return;
  }

  analyzeBtn.disabled = true;
  analyzeBtn.textContent = "Analyzing…";

  try {
    const response = await fetch("/api/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ numbers: raw })
    });

    const data = await response.json();

    if (!response.ok) throw new Error(data.error || "Analysis failed.");

    smallest.textContent = data.smallest;
    largest.textContent = data.largest;
    count.textContent = data.count;
    sum.textContent = data.sum;
    average.textContent = data.average;

    renderList(evenList, data.even);
    renderList(oddList, data.odd);
  } catch (error) {
    message.textContent = error.message;
  } finally {
    analyzeBtn.disabled = false;
    analyzeBtn.innerHTML = 'Analyze Dataset <span>→</span>';
  }
}

analyzeBtn.addEventListener("click", analyze);

clearBtn.addEventListener("click", () => {
  numbers.value = "";
  message.textContent = "";
  smallest.textContent = "—";
  largest.textContent = "—";
  count.textContent = "—";
  sum.textContent = "—";
  average.textContent = "—";
  evenList.innerHTML = '<span class="empty">Awaiting analysis</span>';
  oddList.innerHTML = '<span class="empty">Awaiting analysis</span>';
});

document.querySelectorAll("[data-set]").forEach(button => {
  button.addEventListener("click", () => {
    numbers.value = button.dataset.set;
    analyze();
  });
});

numbers.addEventListener("keydown", event => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") analyze();
});
