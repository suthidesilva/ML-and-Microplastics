const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const loadingSpinner = document.getElementById('loadingSpinner');
const resultsSection = document.getElementById('resultsSection');
const previewImage = document.getElementById('previewImage');

const categories = {
    beads: ['bead', 'beads', 'sphere', 'spherical'],
    fibers: ['fiber', 'fibers', 'fibre', 'fibres', 'thread', 'threads'],
    films: ['film', 'films', 'sheet', 'sheets'],
    foam: ['foam', 'foams', 'polystyrene'],
    fragments: ['fragment', 'fragments', 'piece', 'pieces'],
    organic: ['organic', 'natural', 'plant', 'algae'],
    undefined: ['unknown', 'undefined', 'other']
};

dropZone.addEventListener('dragover', handleDragOver);
dropZone.addEventListener('dragleave', handleDragLeave);
dropZone.addEventListener('drop', handleDrop);
dropZone.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', handleFileSelect);

const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme') || 'dark';

document.documentElement.setAttribute('data-theme', currentTheme);
toggleSwitch.checked = currentTheme === 'dark';
updateThemeText(currentTheme);

function switchTheme(e) {
    const theme = e.target.checked ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    updateThemeText(theme);
}

function updateThemeText(theme) {
    const themeText = document.querySelector('.theme-switch-wrapper em');
    themeText.textContent = theme === 'dark' ? 'Light Mode' : 'Dark Mode';
}

toggleSwitch.addEventListener('change', switchTheme);

function handleDragOver(e) {
    e.preventDefault();
    dropZone.classList.add('dragover');
}

function handleDragLeave() {
    dropZone.classList.remove('dragover');
}

function handleDrop(e) {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
}

function handleFileSelect(e) {
    if (e.target.files.length > 0) {
        handleFile(e.target.files[0]);
    }
}

// Main file handling function
function handleFile(file) {
    if (!file.type.startsWith('image/')) {
        alert('Please upload an image file');
        return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        previewImage.style.display = 'block';
    };
    reader.readAsDataURL(file);

    // Show loading state
    loadingSpinner.style.display = 'block';
    resultsSection.style.display = 'none';

    // Process the filename
    analyzeFileName(file.name);
}

// Function to analyze filename and generate probabilities
function analyzeFileName(filename) {
    // Convert filename to lowercase for case-insensitive matching
    const lowercaseFilename = filename.toLowerCase();

    // Initialize results object
    let results = {
        beads: 5,
        fibers: 5,
        films: 5,
        foam: 5,
        fragments: 5,
        organic: 5,
        undefined: 5
    };

    // Flag to track if any category was matched
    let matchFound = false;

    for (const [category, keywords] of Object.entries(categories)) {
        for (const keyword of keywords) {
            if (lowercaseFilename.includes(keyword.toLowerCase())) {
                results[category] = 60 + Math.random() * 20;
                matchFound = true;

                for (const otherCategory in results) {
                    if (otherCategory !== category) {
                        results[otherCategory] = 5 + Math.random() * 15;
                    }
                }
                break;
            }
        }
    }

    if (!matchFound) {
        results.undefined = 40 + Math.random() * 20;
        for (const category in results) {
            if (category !== 'undefined') {
                results[category] = 5 + Math.random() * 15;
            }
        }
    }

    // Normalize results to ensure total is 100%
    const total = Object.values(results).reduce((a, b) => a + b, 0);
    for (const category in results) {
        results[category] = (results[category] / total) * 100;
    }

    // Simulate processing time
    setTimeout(() => {
        // Hide loading state
        loadingSpinner.style.display = 'none';
        resultsSection.style.display = 'block';

        updateResults(results);
    }, 1500);
}

function updateResults(results) {
    Object.keys(results).forEach((key) => {
        updateProgressBar(key, results[key]);
    });
}

function updateProgressBar(type, percentage) {
    const progressBar = document.getElementById(`${type}Progress`);
    const percentageText = document.getElementById(`${type}Percentage`);
    if (progressBar && percentageText) {
        progressBar.style.width = `${percentage}%`;
        percentageText.textContent = `${percentage.toFixed(1)}%`;
    }
}

// Sample image click handling
const sampleImages = document.querySelectorAll('.sample-image');
sampleImages.forEach((sample) => {
    sample.addEventListener('click', () => {
        const category = sample.dataset.category.toLowerCase();
        previewImage.src = sample.src;
        previewImage.style.display = 'block';
        loadingSpinner.style.display = 'block';
        resultsSection.style.display = 'none';

        // Simulate analysis for the selected sample
        setTimeout(() => {
            loadingSpinner.style.display = 'none';
            resultsSection.style.display = 'block';

            const simulatedResults = {};
            Object.keys(categories).forEach((cat) => {
                simulatedResults[cat] = cat === category ? 75 + Math.random() * 15 : 5 + Math.random() * 10;
            });
            updateResults(simulatedResults);
        }, 1000);
    });
});
