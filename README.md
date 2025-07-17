# 📚 Book Recommender

An interactive machine learning app that suggests similar books based on your favorite titles. Built with **Pandas**, **scikit-learn**, and **Streamlit**, this project helps users discover new reads by leveraging content-based filtering techniques.

---

## 🚀 Features

- 🔎 **Content-Based Recommendations**: Suggests books with similar themes, genres, and descriptions.
- 📊 **Clean UI with Streamlit**: Intuitive interface for selecting and recommending books.
- 💾 **Preloaded Dataset**: Includes thousands of book titles, authors, and descriptions.
- 🌐 **Deployable Web App**: Fully functional and deployable on platforms like Streamlit Cloud or Hugging Face Spaces.

---

## 🖼️ Screenshots

### 🏠 Home Interface
> The landing page of the app allows users to select any book from the dropdown and get personalized recommendations.
<img width="1919" height="805" alt="Screenshot 2025-07-17 092439" src="https://github.com/user-attachments/assets/0a0bf929-9082-403e-924b-a354736a5d0d" />


---

### 📚 Generating Recommendations
> After selecting *"Mestizos Come Home!"*, the app lists multiple similar books that the user might enjoy.
<img width="1919" height="814" alt="Screenshot 2025-07-17 090510" src="https://github.com/user-attachments/assets/4c2974c9-7c8f-4517-b512-a136e58165bc" />


---

### 🔄 Extended Book List View
> A clean, vertical layout showcasing additional recommendations along with book covers and titles.
<img width="1080" height="897" alt="Screenshot 2025-07-17 090524" src="https://github.com/user-attachments/assets/15b395fc-9844-4b35-8ad2-80ab258fbb06" />


---

### 📖 Trying Another Example
> Selecting a different title like *"Fictional Points of View"* generates new, relevant book suggestions.
<img width="1092" height="900" alt="Screenshot 2025-07-17 092907" src="https://github.com/user-attachments/assets/9a41c4ef-1ed3-4ab4-9e66-37f53fda8999" />


---

## ⚙️ Tech Stack

- **Python**
- **Pandas**
- **scikit-learn**
- **Streamlit**
- **Book dataset (custom CSV)**

---

## 🧠 How It Works

The model uses **cosine similarity** on TF-IDF vectors generated from book titles and metadata. When a user selects a book, the system finds other books with the closest feature vectors, which are then displayed as recommendations.

---

## 🛠️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/your-username/book-recommender.git
cd book-recommender
