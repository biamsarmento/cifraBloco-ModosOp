# 🔒 AES Block Cipher & Operation Modes

## 📖 About the Project

This project explores the **AES block cipher** and its **ECB** and **GCM (Galois Counter Mode)** operation modes. It is divided into three main parts:  
1. **Implementation of the AES cipher**  
2. **Implementation of the ECB and GCM modes**  
3. **Testing the encryption process**  

🔗 **Reference:** [AES - Wikipedia](https://pt.wikipedia.org/wiki/Advanced_Encryption_Standard)  

## 🔑 AES Implementation (128-bit Block, 128-bit Key)

The **AES encryption and decryption** were implemented to allow users to specify the number of rounds to execute. The implementation includes:
- **Basic round function**
- **Initial round operations**
- **Final round operations**  

### ⚡ How to Use AES
The AES implementation is **intuitive**. Just follow the prompts, and the encryption process will guide you step by step.

## 🔄 ECB and GCM Modes Implementation

The project includes two encryption modes:  
- **ECB (Electronic Codebook)**: Encrypts each block independently.  
- **GCM (Galois Counter Mode)**: Uses a counter for encryption, ensuring better security against pattern recognition.  

To **verify correctness**, OpenSSL can be used for comparison purposes, but it was not used in the implementation itself.

### 📌 How to Use ECB Mode
- **ECB is programmed to encrypt and decrypt a JPEG image**.  
- Make sure to **provide the correct path** to the image file.  
- Other than that, the process is **intuitive**.

### 📌 How to Use GCM Mode
- In **GCM mode**, the user must provide the path to a **TXT file** containing the data to be encrypted.  
- The file **must follow the format** below:
f0 30 d6 6d 66 f5 81 5d b7 c1 09 01 1e f6 65 5e af e3 f1 a4 01 a6 e2 65 ca 34 ab 0b 00 2b 69 90 e5 64 e5 20 f0 df 82 e0 10 02 70 23 78 b0 9f 19 c6 33 ae 5e 0f 03 04 70 42 c9 4b 9e f8 85 cf 7e 29 d9 aa 14 28 ad ef ec 8d 96 77 18 6e 11 bf 71 e1 0b 6b 01 43 90 99 b1 be 0f ec 3e 94 da 09 44 23 ea 26 5f 8b 94 ba 19 6b d5 d5 9b 1c c5 a6 e1 d6 b9 f8 c0 97 d2 89 8f ae c8 9d ad 54 db c9 6a 05 2b 02 d2 e1 75 8f f4 b8 c7 c1 4e 44 8c 18 26 80 2d 12 d0 19 76 f7 1a 8e d2 cc 23 5f ac 92 e0

- The **number of lines does not matter**, as long as the **bytes are formatted correctly**.  

## 🧪 Testing

The encryption algorithm was tested using the following procedure:

1️⃣ **A selfie was taken as the input image.**  
2️⃣ **ECB Mode Tests:**  
   - The image was encrypted using **1, 5, 9, and 13 AES rounds**.  
   - Each encrypted image was rendered and hashed.  

3️⃣ **GCM Mode Tests:**  
   - The same encryption steps were applied using **GCM mode**.  

## 📂 Project Structure

- **`aes.py`** → AES implementation (encryption & decryption) with variable rounds.  
- **`ecb.py`** → ECB mode implementation for AES.  
- **`gcm.py`** → GCM mode implementation for AES.  
- **`test.py`** → Test scripts for encrypting an image and generating results.  
- **`results/`** → Contains encrypted images and corresponding hashes.  
- **`report.pdf`** → Detailed explanation of the encryption process, results, and analysis.  

## 🛠️ Technologies Used

- **Python**
- **NumPy (for matrix operations)**
- **Matplotlib (for rendering images)**
- **Custom-built AES and encryption modes (no external cryptographic libraries were used)**

## 🎯 Objective

The goal of this project was to **implement AES from scratch**, ensuring flexibility in the number of rounds, and applying it to **image encryption experiments** to analyze the effects of different modes of operation.

## 🔧 How to Run the Project

### 📦 Cloning the Repository
```bash
git clone https://github.com/biamsarmento/cifraBloco-ModosOp.git
cd cifraBloco-ModosOp


