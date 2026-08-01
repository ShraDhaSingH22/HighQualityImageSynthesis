# High-Quality Image Synthesis and Foreground Extraction Using GANs and Image Matting Techniques

🚀 This project focuses on **image synthesis and foreground extraction** using **Conditional GANs (CGAN), Super-Resolution GAN (SRGAN), and MODNet**. The objective is to generate high-quality synthesized images while accurately extracting foreground objects for applications such as image editing, virtual backgrounds, content creation, and computer vision.

---

# ✨ Features

* ✅ Foreground Extraction using **MODNet**
* ✅ Super-Resolution Image Enhancement using **SRGAN**
* ✅ High-Quality Background Generation using **Conditional GAN (CGAN)**
* ✅ End-to-End Image Processing Pipeline
* ✅ Optional GPU (CUDA) Support for Faster Training

---

# 📂 Project Structure

```text
HighQualityImageSynthesis/
│── checkpoints/          # Saved trained models
│── data/                 # Training datasets
│   ├── alphamatting/     # Foreground extraction dataset
│   ├── superres/         # High-resolution dataset for SRGAN
│   ├── backgrounds/      # Background dataset for CGAN
│── models/               # MODNet, CGAN and SRGAN models
│── scripts/              # Training scripts
│   ├── train_modnet.py
│   ├── train_cgan.py
│   ├── train_srgan.py
│── dataset.py            # Dataset loaders
│── process_image.py      # Image processing utilities
│── main.py               # Main execution script
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```

---

# 🛠 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/ShraDhaSingH22/HighQualityImageSynthesis.git


---

## 2️⃣ Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📊 Dataset Setup

## 1️⃣ Foreground Extraction Dataset

Download and place the following files inside:

```text
data/alphamatting/
```

* `input_lowres.zip`
* `trimap_lowres.zip`

Extract both files before training.

---

## 2️⃣ Super-Resolution Dataset

Download high-resolution images automatically:

```bash
python automatic_hrdwnld.py
```

This downloads 100+ high-quality images for SRGAN training.

---

## 3️⃣ Background Dataset

Download background images using:

```bash
python download_backgrounds.py
```

or manually collect images and place them inside:

```text
data/backgrounds/
```

---

# 🖥️ Model Training

## Train MODNet

```bash
python scripts/train_modnet.py
```

Model saved as:

```text
checkpoints/modnet.pth
```

---

## Train Conditional GAN

```bash
python scripts/train_cgan.py
```

Model saved as:

```text
checkpoints/cgan.pth
```

---

## Train SRGAN

```bash
python scripts/train_srgan.py
```

Model saved as:

```text
checkpoints/srgan.pth
```

---

# 🚀 Run the Project

After training all models, execute:

```bash
python main.py
```

The pipeline will:

* Extract foreground using MODNet
* Generate or enhance backgrounds using CGAN
* Improve image resolution using SRGAN
* Produce high-quality synthesized output images

---

# 💻 System Requirements

### Recommended

* Python 3.10+
* Git
* pip
* CUDA-enabled NVIDIA GPU (recommended)
* 8 GB RAM minimum
* 10 GB free storage

---

# 📝 Notes

* Ensure datasets are downloaded and extracted before training.
* GPU acceleration significantly improves training speed.
* Hyperparameters can be modified inside the training scripts for better performance.
* Save trained weights inside the `checkpoints/` directory.

---

# 👥 Contributors

* Shradha Singh
* Anshuman Samanta
* Aditya Kumar
* Aman Yadav
* Vidit Mishra
* Pawan Chaudhary

---

# 📜 License

This project is released under the **MIT License**.

---

# 📬 Contact

For questions, bug reports, or feature requests, please open an issue in the project's GitHub repository.
