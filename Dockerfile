FROM mambaorg/micromamba:latest
WORKDIR /workspace
COPY environment.yaml .
RUN micromamba create -p /opt/conda/env -f environment.yaml -y && micromamba clean -a -y
COPY . .
EXPOSE 8888
CMD ["micromamba", "run", "-p", "/opt/conda/env", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]