# Spatial Omics Analysis with Python

**A workshop by the HMS Core for Computational Biomedicine ([CCB](https://dbmi.hms.harvard.edu/about-dbmi/core-computational-biomedicine)) in a joint venture with the [scverse](https://scverse.org) core team.**

Welcome! This repository contains the materials for the hands-on workshop on analyzing spatial omics data with Python and the [scverse](https://scverse.org) ecosystem.

In this 3-hour workshop, you will learn how to load, explore, and analyze data from different spatial technologies like Visium and Xenium. We will cover established workflows, from interactive visualization with [napari](https://napari.org) to cell type clustering with [scanpy](https://scanpy.readthedocs.io) and computing spatial statistics with [squidpy](https://squidpy.readthedocs.io).

---

## 📋 Workshop Materials

**Introduction Slides:** Before diving into the hands-on notebooks, we'll start with a brief presentation introducing the scverse ecosystem and SpatialData framework. You can access the slides here: [Introduction to scverse](https://docs.google.com/presentation/d/1JtF5KmWrMf8-J-BDth-vwqB2Ie8qki9R/edit?usp=drive_link&ouid=106527443230334727646&rtpof=true&sd=true)

The workshop is organized into 4 interactive Jupyter notebooks that build on each other, taking you from basic concepts to advanced spatial analysis techniques.

## 💻 Workshop Environment Setup

To ensure a reproducible setup, this workshop runs inside a **[Docker](https://docker.com) container**. This self-contained "Workshop in a Box" includes the necessary software, system dependencies, and example data -- pre-installed and ready to go.

Please follow these **one-time setup instructions at least one day before the workshop.**

### Step 1: Install Docker Desktop

First, we need [Docker Desktop](https://www.docker.com/products/docker-desktop/) to run the workshop container.
*   **Action:** Go to [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) and download the installer for your operating system (Windows, Mac, or Linux).
*   Follow the installation instructions. After the installation is complete, start the Docker Desktop application and leave it running in the background.

### Step 2: Install Git (if you don't have it)

[Git](https://git-scm.com/) is a version control tool we'll use to download the workshop files.
*   **Action:** If you don't have Git, install it from [https://git-scm.com/downloads](https://git-scm.com/downloads).

### Step 3: Clone This Repository

This command will download the workshop's configuration files and analysis notebooks to your computer.
*   **Action:** Open the terminal (PowerShell on Windows, Terminal on Mac/Linux) and run:
    ```bash
    git clone https://github.com/ccb-hms/Spatial-Workshop.git
    ```

---

## 🚀 Running the Workshop

Follow these 3 steps to start the workshop:

### Step 1: Navigate to the Workshop Folder
*   In the terminal, change to the workshop directory we cloned above in Setup Step 3:
    ```bash
    cd Spatial-Workshop
    ```

### Step 2: Launch the Container
*   Download the workshop image (~3.2 GB download, expands to ~6.5 GB locally) and start the environment.
    ```bash
    docker-compose up
    ```
    ... or, if you're running Docker v2:
    ```bash
    docker compose up
    ```
*   **Note:** The first time you run this, it will take a while to download the image. Please do this on a stable internet connection **at least one day before the workshop to avoid overwhelming the Harvard network on the day of the workshop**.

### Step 3: Access JupyterLab
*   Confirm that you see log messages from the Jupyter server in the terminal,
*   Look for a URL that starts with `http://127.0.0.1:8888/lab?token=...`,
*   Copy the full URL and paste it into your web browser (Chrome or Firefox recommended).

You are now inside the workshop environment! You can open the notebooks from the file browser on the left and start the exercises.

---
