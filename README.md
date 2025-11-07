# Spatial Omics Analysis with Python

**A workshop by the HMS Core for Computational Biomedicine (CCB) in a joint venture with the scverse core team.**

Welcome! This repository contains all the materials for our hands-on workshop on analyzing modern spatial omics data using Python and the `scverse` ecosystem.

In this 3-hour session, you will learn how to load, explore, and analyze data from multiple spatial technologies like Visium and Xenium. We will cover a complete workflow, from interactive visualization with `napari` to cell type clustering with `scanpy` and spatial statistics with `squidpy`.

---

## 💻 Workshop Environment Setup

To ensure everyone has a smooth, identical, and error-free experience, this workshop runs inside a **Docker container**. This self-contained "Workshop in a Box" includes all the necessary software, libraries, and data, pre-installed and ready to go.

Please follow these **one-time setup instructions at least one day before the workshop.**

### Step 1: Install Docker Desktop

Docker Desktop is the application that runs our workshop container.
*   **Action:** Go to [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) and download the installer for your operating system (Windows, Mac, or Linux).
*   Follow the installation instructions. After it's installed, start the Docker Desktop application and leave it running in the background.

### Step 2: Install Git (if you don't have it)

Git is a version control tool we'll use to download the workshop files.
*   **Action:** If you don't have Git, install it from [https://git-scm.com/downloads](https://git-scm.com/downloads).

### Step 3: Clone This Repository

This command will download the workshop's configuration files and notebooks to your computer.
*   **Action:** Open your terminal (PowerShell on Windows, Terminal on Mac/Linux) and run:
    ```bash
    git clone https://github.com/ccb-hms/Spatial-Workshop.git
    ```

---

## 🚀 Running the Workshop

This is the simple process you will use to start the workshop each time.

### Step 1: Navigate to the Workshop Folder
*   In your terminal, change to the directory you just cloned:
    ```bash
    cd Spatial-Workshop
    ```

### Step 2: Launch the Container
*   This single command will download the ~8 GB workshop image (the first time only) and start the environment.
    ```bash
    docker-compose up
    ```
*   **Note:** The first time you run this, it will take a while to download the image. Please do this on a stable internet connection before the workshop begins.

### Step 3: Access JupyterLab
*   Wait for your terminal to show log messages from the Jupyter server.
*   Look for a URL that starts with `http://127.0.0.1:8888/lab?token=...`.
*   Copy this full URL and paste it into your web browser (Chrome or Firefox recommended).

You are now inside the workshop environment! You can open the notebooks from the file browser on the left and start the exercises.

---

###  Troubleshooting

#### `napari` Window Not Appearing on Windows
When you run a `napari` cell, a new window should appear on your desktop. If you are on Windows and no window appears, please follow these one-time setup steps to manually configure graphics forwarding.

**1. Install VcXsrv:**
*   Download and install the VcXsrv X Server for Windows from [this link](https://sourceforge.net/projects/vcxsrv/).

**2. Configure and Run VcXsrv:**
*   Launch "XLaunch" from your Start Menu.
*   Click through the wizard with these exact settings:
    *   Display: **Multiple windows**
    *   Client startup: **Start no client**
    *   Extra settings: **CHECK THE BOX for "Disable access control"**.
*   Click Finish. An 'X' icon will appear in your system tray. (You can also use the `.bat` script method we discussed to make this a one-click process).

**3. Modify `docker-compose.yml`:**
*   Open the `docker-compose.yml` file in this repository.
*   Add the `environment` section as shown below:
    ```yaml
    services:
      workshop:
        # ... (image and ports lines) ...
        environment:
          - DISPLAY=host.docker.internal:0.0
    ```
*   Save the file.

**4. Relaunch:**
*   Go back to your terminal, press `Ctrl+C`, then run `docker-compose up` again. The `napari` window should now appear.