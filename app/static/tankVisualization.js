// tankVisualization.js

// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Dimensions - Replace these with actual results from your Flask app
    const tankWidth = {{ results['Tank Width'] || 1 }}; // Example value
    const tankHeight = {{ results['Tank Height'] || 1 }}; // Example value
    const tankDepth = {{ results['Tank Depth'] || 1 }}; // Example value

    // Initialize Three.js scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 500, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, 500); // Width of container
    document.getElementById('tank-visualization').appendChild(renderer.domElement);

    // Create tank geometry and material
    const geometry = new THREE.BoxGeometry(tankWidth, tankHeight, tankDepth);
    const material = new THREE.MeshBasicMaterial({ color: 0x007bff, wireframe: true });
    const tank = new THREE.Mesh(geometry, material);
    scene.add(tank);

    // Position camera
    camera.position.z = 5;

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        tank.rotation.y += 0.01; // Rotate for a 3D view effect
        renderer.render(scene, camera);
    }
    animate();

    // Adjust the canvas size when the window is resized
    window.addEventListener('resize', () => {
        renderer.setSize(window.innerWidth, 500);
        camera.aspect = window.innerWidth / 500;
        camera.updateProjectionMatrix();
    });
});
