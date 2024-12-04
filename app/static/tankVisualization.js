// tankVisualization.js

// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Fetch dimensions dynamically or use defaults
    const tankWidth = parseFloat(document.getElementById('tank-width')?.dataset.value || 1);
    const tankHeight = parseFloat(document.getElementById('tank-height')?.dataset.value || 1);
    const tankDepth = parseFloat(document.getElementById('tank-depth')?.dataset.value || 1);

    // Initialize Three.js scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 500, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, 500);
    renderer.setClearColor(0xf8f9fa); // Light background color
    document.getElementById('tank-visualization').appendChild(renderer.domElement);

    // Create tank geometry and material
    const geometry = new THREE.BoxGeometry(tankWidth, tankHeight, tankDepth);
    const material = new THREE.MeshBasicMaterial({ color: 0x007bff, wireframe: true });
    const tank = new THREE.Mesh(geometry, material);
    scene.add(tank);

    // Add labels using TextGeometry
    const loader = new THREE.FontLoader();
    loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', (font) => {
        const addLabel = (text, position) => {
            const textGeometry = new THREE.TextGeometry(text, {
                font: font,
                size: 0.2,
                height: 0.02,
            });
            const textMaterial = new THREE.MeshBasicMaterial({ color: 0xffffff });
            const textMesh = new THREE.Mesh(textGeometry, textMaterial);
            textMesh.position.set(position.x, position.y, position.z);
            scene.add(textMesh);
        };

        // Add dimension labels
        addLabel(`Width: ${tankWidth}m`, { x: tankWidth / 2, y: -tankHeight / 2 - 0.5, z: 0 });
        addLabel(`Height: ${tankHeight}m`, { x: -tankWidth / 2 - 0.5, y: tankHeight / 2, z: 0 });
        addLabel(`Depth: ${tankDepth}m`, { x: 0, y: -tankHeight / 2 - 0.5, z: -tankDepth / 2 });
    });

    // Position the camera
    camera.position.z = 5;

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        tank.rotation.y += 0.01; // Rotate for a dynamic view
        renderer.render(scene, camera);
    }
    animate();

    // Adjust canvas size on window resize
    window.addEventListener('resize', () => {
        renderer.setSize(window.innerWidth, 500);
        camera.aspect = window.innerWidth / 500;
        camera.updateProjectionMatrix();
    });
});
