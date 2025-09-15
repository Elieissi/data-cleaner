# 🗂️ Data Cleaner

Python CLI tool to load, clean, search, preview, and export data from multiple file formats.

---

## 📂 Supported Formats
- **CSV** – Comma-separated values with headers  
- **JSON** – List of dictionaries or single-key wrapped list  
- **TXT** – Lines with comma-separated `key:value` pairs  

---

## ✨ Features
- Normalizes missing values to `"none"`
- Search any value across all keys
- Preview first 5 records
- Export cleaned data to CSV, JSON, or TXT

---

## 🚀 Quick Start (Docker)

Clone the repository and navigate into the folder:

```powershell
git clone https://github.com/Elieissi/data-cleaner.git
cd data-cleaner
```

## 🚀 Build the Docker Image
```
docker build -t data-cleaner .
```
## Run the container and mount the `data/` folder (required so the program can access your local files):

**Windows PowerShell:**
```powershell
docker run -it --rm -v ${PWD}\data:/app/data data-cleaner
```

## When prompted, just type the filename (no need to include data/):

```
employees.csv
```



