const scene = new THREE.Scene({ color: 0xfff });
const camera = new THREE.PerspectiveCamera(100, window.innerWidth / window.innerHeight, 1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);

document.body.appendChild(renderer.domElement);

const light = new THREE.PointLight(0xffffff, 1, 300);
light.position.set(-5, -1, 0.5);
camera.add(light);
scene.add(camera);

const material = new THREE.MeshPhongMaterial({
    color: 0xffffff, 
});

const points = [
    {"x": 1.3, "y": 0},
    {"x": 1.3, "y": 0.2},
    {"x": 1.2, "y": 0.3},
    {"x": 1.3, "y": 0.7},
    {"x": 1.0, "y": 0.9},
    {"x": 1.0, "y": 1.2},
    {"x": 0.9, "y": 1.2},
    {"x": 0.6, "y": 1.9},
    {"x": 0.4, "y": 3.2},
    {"x": 0.8, "y": 3.5},
    {"x": 0.65, "y": 3.6},
    {"x": 0.5, "y": 3.7},
    {"x": 0.5, "y": 3.9},
    {"x": 0.54, "y": 4.0},
    {"x": 0.5, "y": 4.1},
    {"x": 0.8, "y": 4.5},
    {"x": 0.7, "y": 5.2},
    {"x": 0.3, "y": 5.8},
    {"x": 0.3, "y": 5.9},
    {"x": 0.35, "y": 6.0},
    {"x": 0.35, "y": 6.1},
    {"x": 0.3, "y": 6.2},
];

const geometry = new THREE.LatheGeometry(points, 32);
const lathe = new THREE.Mesh(geometry, material);
lathe.position.set(0, -4, 0);
scene.add(lathe);



function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

camera.position.z = 7;

animate();