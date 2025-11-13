# Spatial Omics Analysis with Python

**A workshop by the HMS Core for Computational Biomedicine ([CCB](https://dbmi.hms.harvard.edu/about-dbmi/core-computational-biomedicine)) in a joint venture with the [scverse](https://scverse.org) core team.**

Welcome! This repository contains the materials for the hands-on workshop on analyzing spatial omics data with Python and the [scverse](https://scverse.org) ecosystem.

In this 3-hour workshop, you will learn how to load, explore, and analyze data from different spatial technologies like MERFISH, Visium and Xenium. We will cover established workflows, from interactive visualization with [napari](https://napari.org) to cell type clustering with [Scanpy](https://scanpy.readthedocs.io) and computing spatial statistics with [Squidpy](https://squidpy.readthedocs.io).

---

## 📋 Workshop Materials

**Introduction Slides:** Before diving into the hands-on notebooks, we'll start with a brief presentation introducing the scverse ecosystem and SpatialData framework. You can access the slides here: [Introduction to SpatialData](https://docs.google.com/presentation/d/1K3SUjrZfg4pY2FAi0ydXakAPJM4Alo8ABissELLk_6o/edit?usp=sharing)

**Jupyter Notebooks:** The workshop is organized into 4 interactive Jupyter [notebooks](https://github.com/ccb-hms/Spatial-Workshop/tree/main/notebooks) that build on each other, taking you from basic concepts to advanced spatial analysis techniques.

---

## 💻 Workshop Setup - Choose Your Option

We provide **two setup options** for the workshop. Choose the one that best fits your needs:

### Option 1: Conda Environment Setup  (Recommended Setup)

- ✅ **Full interactivity**: All visualization tools work, including napari
- ❌ **Manual setup**: Requires installing dependencies and downloading data separately

### Option 2: Docker Setup 

- ✅ **Everything included**: Software, data, and notebooks pre-installed
- ❌ **Limited interactivity**: Interactive visualization tools (napari) won't work in Docker


---

## 🐍 Option 1: Conda Environment Setup

### Prerequisites

1. **Install Miniconda/Anaconda**: Download from [docs.conda.io/en/latest/miniconda.html](docs.conda.io/en/latest/miniconda.html)
2. **Install Git**: Download from [git-scm.com/downloads](git-scm.com/downloads) (if you don't have it)
Setup Steps

### Setup Steps

```
# 1. Clone the repository
git clone https://github.com/ccb-hms/Spatial-Workshop.git
cd Spatial-Workshop

# 2. Create and activate the environment
conda env create -f environment.yaml
conda activate spatial-workshop

# 3. Download and extract the workshop data (~1.5 GB)

# Install gdown (Google Drive downloader)
pip install gdown

# Download the data
gdown "1WGIxjywr3azsdGG4gSKRhlEKKhWPePG5" -O spatial-workshop-data.zip

# Extract the data
tar -xf spatial-workshop-data.zip      # Windows
unzip spatial-workshop-data.zip        # Mac/Linux

# Clean up the zip file
del spatial-workshop-data.zip          # Windows  
rm spatial-workshop-data.zip           # Mac/Linux

# 4. Start JupyterLab
jupyter lab
```

### Access JupyterLab

- JupyterLab will open automatically in your browser
- Browse the notebooks in the file browser and run them in any order

## 🐳 Option 2: Docker Setup

### Prerequisites

1. **Install Docker Desktop:** Download from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) and follow installation instructions
2. **Install Git:** Download from [git-scm.com/downloads](https://git-scm.com/downloads) (if you don't have it)

### Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/ccb-hms/Spatial-Workshop.git
cd Spatial-Workshop

# 2. Start the workshop environment (~3 GB download, ~7 GB storage)
docker compose up
```

### Access JupyterLab

- Open your browser and go to: `http://127.0.0.1:8888/lab`
- Browse the notebooks in the file browser and run them in any order


## 🚀 During the Workshop

**Important Notes:**

- **Conda users**: All interactive features will work on your system
- **Docker users**: Interactive visualization sections will be demonstrated by instructors
- Both setups provide identical analysis capabilities for the core workshop content

---

## 🆘 Need Help?

If you encounter setup issues:

1. **Conda users**: Ensure you have sufficient disk space (~11 GB total: 9 GB environment + 2 GB data)
2. **Docker users**: Try `docker-compose up` (with hyphen) if `docker compose up` fails
---

## 🧹 Cleanup (After Workshop)

**Conda users:**

```
conda env remove -n spatial-workshop
```

**Docker users:**

```
docker rmi anthonychristidis/spatial-workshop:v1.4
```

---

## 📚 Additional Resources

Continue your spatial omics journey with these comprehensive resources:

### Core Documentation

- **[SpatialData](https://spatialdata.scverse.org/en/stable/)** - Complete framework for spatial omics data management, storage, and analysis
- **[Scanpy](https://scanpy.readthedocs.io/en/stable/)** - Single-cell analysis in Python with tutorials, API reference, and best practices
- **[Squidpy](https://squidpy.readthedocs.io/en/stable/)** - Spatial molecular data analysis with advanced statistics and neighborhood analysis methods

### Interactive Visualization

- **[napari-spatialdata](https://spatialdata.scverse.org/projects/napari/en/latest/)** - Interactive visualization plugin for exploring spatial data in napari
- **[Vitessce](https://vitessce.io/docs/)** - Web-based visualization platform for integrative analysis of spatial and single-cell data

### Community

- **[scverse](https://scverse.org)** - The broader single-cell analysis ecosystem in Python
- **[scverse Discourse](https://discourse.scverse.org/)** - Community forum for questions, discussions, and announcements

These resources provide in-depth tutorials, API documentation, and community support to help you apply these tools to your own spatial omics projects.






