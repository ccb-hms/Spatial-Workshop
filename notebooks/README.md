# Workshop Notebooks

This directory contains the four Jupyter notebooks for the "Spatial Omics Analysis with Python" workshop. We recommend running them in order to follow the complete analysis narrative.

---

### **Notebook 1: Introduction to the `SpatialData` Framework**

- **Goal:** Understand the fundamentals of the `SpatialData` object, the core data structure of the scverse ecosystem for spatial omics.
- **What you'll learn:**
  - How `SpatialData` organizes complex data (images, shapes, tables) into a single, unified container.
  - How to load and inspect `SpatialData` objects from different technologies.

---

### **Notebook 2: Interactive Visualization with `napari` and `Vitessce`**

- **Goal:** Learn how to visually explore complex, multi-layered spatial data.
- **What you'll learn:**
  - Use the `napari-spatialdata` plugin to interactively view images, cell segmentations, and gene expression.
  - See a demonstration of `Vitessce` for creating linked, web-based visualizations.
  - Perform interactive tasks like annotating a region of interest (ROI).

---

### **Notebook 3: Data Processing and Clustering with `Scanpy`**

- **Goal:** Go from raw gene counts to meaningful biological groups using a standard single-cell analysis workflow.
- **What you'll learn:**
  - Perform Quality Control (QC) to remove low-quality cells/spots.
  - Normalize data, find highly variable genes, and run PCA for dimensionality reduction.
  - Use the Leiden algorithm to cluster cells and visualize the results on a UMAP plot and back on the tissue image.

---

### **Notebook 4: Spatial Statistics with `Squidpy`**

- **Goal:** Take the cell clusters from the previous notebook and ask quantitative questions about their spatial organization.
- **What you'll learn:**
  - Identify spatially variable genes that define tissue regions using Moran's I.
  - Analyze the "social network" of your tissue by calculating neighborhood enrichment to see which cell types are found together.
  - Quantify cell-cell co-occurrence to understand the strength of these spatial relationships.