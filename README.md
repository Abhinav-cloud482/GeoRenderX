# GeoRenderX

A Python-based Computational Geometry &amp; ASCII Ray Tracing Engine


## GeoRenderX

### A Python Computational Geometry & ASCII Ray Tracing Engine

GeoRenderX is a compact yet powerful educational project that demonstrates core concepts of **computational geometry**, **ray tracing**, and **spatial data structures** using pure Python.

This project combines multiple advanced topics into a single executable script, making it ideal for learning, experimentation, and showcasing foundational computer graphics concepts.


## Features

### Ray Tracing Engine (ASCII-Based)

* Sphere rendering using ray-object intersection
* Diffuse + ambient lighting
* Shadow computation
* Gradient-based ASCII shading

### KD-Tree (Spatial Indexing)

* Efficient nearest neighbor search
* Demonstrates spatial partitioning
* Reduces brute-force search complexity

### Computational Geometry (2D)

* Convex Hull (Graham Scan algorithm)
* Voronoi Diagram (grid-based approximation)

## Concepts Covered

* Vector Mathematics (3D)
* Ray-Sphere Intersection
* Lighting Models (Diffuse + Ambient)
* Shadow Rays
* Spatial Data Structures (KD-Tree)
* Convex Hull Algorithms
* Voronoi Diagrams
* Precision Handling (Floating-point tolerance)

## Project Structure

```
GeoRenderX/
│
├── main.py        # Complete implementation (single-file project)
└── README.md      # Project documentation
```


## Requirements

* Python 3.8+
* No external libraries required


## How to Run

```bash
python main.py
```


## Sample Output

### Ray Tracer (ASCII)

```
      ....::::----====++++****####%%%%@
      ....::::----====++++****####%%%%@
```

### KD-Tree Output

```
KD-Tree Nearest Neighbor:
Point: (0.41, 0.52, 0.49)
Distance: 0.08
```

### Convex Hull

```
[(0,2), (5,1), (10,4), (18,12), ...]
```

### Voronoi Diagram

```
000000011111111111
000000222222111111
```


## Why This Project Matters

This project demonstrates the **core building blocks** behind real-world systems such as:

* 3D modeling software
* CAD systems
* Game engines
* Simulation tools

It highlights the trade-offs between:

* **Precision vs Performance**
* **Brute-force vs Spatial indexing**


## Limitations

* ASCII rendering (no real image output)
* Voronoi implementation is grid-based (not Fortune’s algorithm)
* No reflections/refractions in ray tracing
* KD-Tree used only for nearest neighbor (not ray acceleration)


## Future Improvements

* Real image rendering (PNG output using Pillow)
* Reflection and refraction in ray tracing
* KD-Tree / BVH acceleration for ray-object intersection
* Delaunay triangulation
* Interactive visualization (Matplotlib / GUI)



## Contributing

Contributions are welcome!

You can :-

* Improve rendering quality
* Optimize KD-tree performance
* Add new geometry algorithms
* Enhance visualization


## License

This project is open-source and available under the MIT License.



## Author

Developed as a learning project for exploring computational geometry and graphics fundamentals in Python.

Abhinav Dixit

Python Developer | Data & ML Enthusiast

