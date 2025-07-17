# Streamlit UI
def infofetcher():
    st.markdown(
        """
        <div style='text-align: center; padding: 1rem; background-color: #F63366; color: white; border-radius: 10px;'>
            <h1>📚 Book Recommender</h1>
            <p>Discover new reads based on your favorites!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    selected_book = st.selectbox("🔍 Choose a book to get similar recommendations:", newdf["title"].values)

    if st.button("✨ Recommend"):
        results = recommender(selected_book)
        if results:
            st.subheader("📖 You might enjoy these:")
            for book in results:
                col1, col2 = st.columns([1, 4])
                with col1:
                    if book["thumbnail"]:
                        st.image(book["thumbnail"], width=100)
                    else:
                        st.image("https://via.placeholder.com/100x150?text=No+Image", width=100)
                with col2:
                    st.markdown(f"**{book['title']}**")
        else:
            st.warning("No recommendations found!")

# Run the app
if __name__ == "__main__":
    infofetcher()
