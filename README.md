# Spatial Omics Analysis with Python

**A workshop by the HMS Core for Computational Biomedicine ([CCB](https://dbmi.hms.harvard.edu/about-dbmi/core-computational-biomedicine)) in a joint venture with the [scverse](https://scverse.org) core team.**

Welcome! This repository contains the materials for the hands-on workshop on analyzing spatial omics data with Python and the [scverse](https://scverse.org) ecosystem.

In this 3-hour workshop, you will learn how to load, explore, and analyze data from different spatial technologies like Visium and Xenium. We will cover established workflows, from interactive visualization with [napari](https://napari.org) to cell type clustering with [scanpy](https://scanpy.readthedocs.io) and computing spatial statistics with [squidpy](https://squidpy.readthedocs.io).

---

## 📋 Workshop Materials

**Introduction Slides:** Before diving into the hands-on notebooks, we'll start with a brief presentation introducing the scverse ecosystem and SpatialData framework. You can access the slides here: [Introduction to scverse](https://docs.google.com/presentation/d/1JtF5KmWrMf8-J-BDth-vwqB2Ie8qki9R/edit?usp=drive_link&ouid=106527443230334727646&rtpof=true&sd=true)

The workshop is organized into 4 interactive Jupyter notebooks that build on each other, taking you from basic concepts to advanced spatial analysis techniques.

---

## 💻 Workshop Setup - Choose Your Option

We provide **two setup options** for the workshop. Choose the one that best fits your needs:

### Option 1: Docker Setup (Recommended for Most Users)

- ✅ **Everything included**: Software, data, and notebooks pre-installed
- ✅ **Easy setup**: Just download and run
- ❌ **Limited interactivity**: Interactive visualization tools (napari) won't work in Docker

### Option 2: Conda Environment Setup  

- ✅ **Full interactivity**: All visualization tools work, including napari
- ✅ **Native performance**: Runs directly on your system
- ❌ **Manual setup**: Requires installing dependencies and downloading data separately

---

## 🐳 Option 1: Docker Setup

### Prerequisites

1. **Install Docker Desktop:** Download from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) and follow installation instructions
2. **Install Git:** Download from [git-scm.com/downloads](https://git-scm.com/downloads) (if you don't have it)

### Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/ccb-hms/Spatial-Workshop.git
cd Spatial-Workshop

# 2. Start the workshop environment (~3.2 GB download)
docker compose up
```

### Access JupyterLab

- Open your browser and go to: `http://127.0.0.1:8888/lab`
- Start with Notebook 1 in the file browser

## 🐍 Option 2: Conda Environment Setup

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

# 3. Download the workshop data (~2.5 GB)
# [INSERT_ZENODO_DOWNLOAD_COMMAND_HERE]

# 4. Start JupyterLab
jupyter lab
```

### Access JupyterLab

- JupyterLab will open automatically in your browser
- Start with Notebook 1 in the file browser

## 🚀 During the Workshop

**Important Notes:**

- **Docker users**: Interactive visualization sections will be demonstrated by instructors
- **Conda users**: All interactive features will work on your system
- Both setups provide identical analysis capabilities for the core workshop content

---

## 🆘 Need Help?

If you encounter setup issues:

1. **Docker users**: Try `docker-compose up` (with hyphen) if `docker compose up` fails
2. **Conda users**: Ensure you have sufficient disk space (~5 GB total)
3. **Everyone**: Contact us if problems persist - we have backup solutions ready

---

## 🧹 Cleanup (After Workshop)

**Docker users:**

```
docker rmi anthonychristidis/spatial-workshop:v1.4
```

**Conda users:**

```
conda env remove -n spatial-workshop
```






