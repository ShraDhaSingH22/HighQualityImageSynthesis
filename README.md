 **README.md** file for our **High-Quality Image Synthesis and Foreground Extraction** project. It includes an overview, installation steps, dataset setup, training instructions, and usage details.

---

# **High-Quality Image Synthesis and Foreground Extraction Using GANs and Image Matting Techniques**

🚀 This project focuses on **image synthesis and foreground extraction** using **Conditional GANs, Super-Resolution GANs (SRGAN), and MODNet for image matting**. The goal is to enhance images and extract high-quality foregrounds for various applications.

---

## **📝 Features**
✅ **Foreground Extraction** using **MODNet**  
✅ **Super-Resolution Image Synthesis** using **SRGAN**  
✅ **High-Quality Background Generation** using **Conditional GAN (CGAN)**  
✅ **Real-time Processing Support** (optional)  

---

## **📂 Folder Structure**
```
HighQualityImageSynthesis/
│── checkpoints/          # Saved trained models
│── data/                 # Training datasets
│   ├── alphamatting/     # Foreground extraction dataset
│   ├── superres/         # High-resolution images for SRGAN
│   ├── backgrounds/      # Background dataset for CGAN
│── models/               # GAN and MODNet models
│── scripts/              # Training scripts
│   ├── train_modnet.py   # Train MODNet
│   ├── train_cgan.py     # Train Conditional GAN
│   ├── train_srgan.py    # Train Super-Resolution GAN
│── dataset.py            # Custom dataset loaders
│── process_image.py      # Image processing utilities
│── main.py               # End-to-end execution script
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
```

---

## **🛠 Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Anshuman22coder/HighQualityImageSynthesis.git
cd HighQualityImageSynthesis
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up Datasets**
#### **(a) Foreground Extraction Data**
Download and place `input_lowres.zip` and `trimap_lowres.zip` in `data/alphamatting/`, then extract them.

#### **(b) Super-Resolution Data**
Download **100+ high-resolution images** for SRGAN:  
```sh
python automatic_hrdwnld.py
```

#### **(c) Background Dataset for CGAN**
Download background images manually or use the **Pexels API**:
```sh
python download_backgrounds.py
```

---

## **🖥️ Training**
### **1️⃣ Train MODNet (Foreground Extraction)**
```sh
python scripts/train_modnet.py
```
🔹 The trained model is saved in: **`checkpoints/modnet.pth`**

### **2️⃣ Train Conditional GAN (Background Synthesis)**
```sh
python scripts/train_cgan.py
```
🔹 The trained model is saved in: **`checkpoints/cgan.pth`**

### **3️⃣ Train SRGAN (Super-Resolution)**
```sh
python scripts/train_srgan.py
```
🔹 The trained model is saved in: **`checkpoints/srgan.pth`**

---

## **🎮 Usage**
After training, you can **test the models** using:
```sh
python main.py
```
This will generate **high-quality images** using the trained models.

---

## **📝 Notes**
- Ensure **datasets are properly placed** before training.  
- **GPU acceleration** (CUDA) is recommended for faster training.  
- Adjust hyperparameters in `train_*.py` for better results.  

---

## **📜 License**
This project is open-source under the **MIT License**.

---

## **🚀 Contributing**
Anshuman Samanta,
Aditya Kumar,
Aman Yadav,
Vidit Mishra,
Pawan Chaudhary,
Shradha Singh
---

## **📬 Contact**
For queries, reach out via **GitHub Issues**.

---

