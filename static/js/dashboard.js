const canvas = document.getElementById('clickCanvas');
const ctx = canvas.getContext('2d');

const initialLayout = { 
    xaxis: {range: [0, 1], fixedrange: true, gridcolor: 'rgba(255,255,255,0.05)', zeroline: false}, 
    yaxis: {range: [0, 1], fixedrange: true, gridcolor: 'rgba(255,255,255,0.05)', zeroline: false},
    paper_bgcolor: 'rgba(0,0,0,0)', 
    plot_bgcolor: 'rgba(0,0,0,0)',
    font: { color: '#94a3b8' }, 
    margin: {l: 50, r: 90, b: 50, t: 30}
};

const initialKdeTrace = [{
    z: [[0]], 
    type: 'contour', 
    colorscale: 'Viridis',
    colorbar: { thickness: 15, len: 0.9, x: 1.05 }
}];

const initialNnTrace = [{
    z: [[0]], 
    type: 'contour', 
    colorscale: 'Magma',
    colorbar: { thickness: 15, len: 0.9, x: 1.05 }
}];

Plotly.newPlot('kdePlot', initialKdeTrace, initialLayout);
Plotly.newPlot('nnPlot', initialNnTrace, initialLayout);

async function initDashboard() {
    try {
        const res = await fetch(`${API_URL}/points/`);
        const points = await res.json();
        points.forEach(point => {
            drawCircle(point.x * canvas.width, (1.0 - point.y) * canvas.height);
        });
        if (points.length >= 2) updateDensityPlots();
    } catch (err) { console.error("Initialization failure:", err); }
}

initDashboard();

canvas.addEventListener('click', async function(event) {
    const rect = canvas.getBoundingClientRect();
    const rawX = event.clientX - rect.left;
    const rawY = event.clientY - rect.top;
    
    drawCircle(rawX, rawY);

    try {
        await fetch(`${API_URL}/points/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ x: rawX / canvas.width, y: 1.0 - (rawY / canvas.height) })
        });
        updateDensityPlots();
    } catch (err) { console.error("Error processing coordinates point input:", err); }
});

function drawCircle(x, y) {
    ctx.beginPath(); ctx.arc(x, y, 5, 0, 2 * Math.PI);
    ctx.fillStyle = '#6366f1'; ctx.fill(); ctx.stroke();
}

async function updateDensityPlots() {
    try {
        const response = await fetch(`${API_URL}/train-and-evaluate/?grid_size=50`, { method: 'POST' });
        const data = await response.json();
        if (data.status === "success") {
            Plotly.react('kdePlot', [{ 
                x: data.axis_range, 
                y: data.axis_range, 
                z: data.kde_Z, 
                type: 'contour', 
                colorscale: 'Viridis',
                colorbar: { thickness: 15, len: 0.9, x: 1.05 }
            }], initialLayout);

            Plotly.react('nnPlot', [{ 
                x: data.axis_range, 
                y: data.axis_range, 
                z: data.nn_Z, 
                type: 'contour', 
                colorscale: 'Magma',
                colorbar: { thickness: 15, len: 0.9, x: 1.05 }
            }], initialLayout);
        }
    } catch (err) { console.error("Evaluating state failure:", err); }
}

document.getElementById('clear-btn').addEventListener('click', async function() {
    await fetch(`${API_URL}/points/clear/`, { method: 'DELETE' });
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    Plotly.react('kdePlot', initialKdeTrace, initialLayout);
    Plotly.react('nnPlot', initialNnTrace, initialLayout);
});
