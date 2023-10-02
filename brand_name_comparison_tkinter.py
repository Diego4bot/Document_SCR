import tkinter as tk
from tkinter import messagebox
from fuzzywuzzy import fuzz

# Define a function to compare brand names and provide explanations
def compare_brand_names():
    brand_name1 = entry1.get()
    brand_name2 = entry2.get()

    # Normalize and preprocess the brand names
    brand_name1 = brand_name1.lower()
    brand_name2 = brand_name2.lower()

    # Calculate the similarity score using the fuzz.ratio method
    similarity_score = fuzz.ratio(brand_name1, brand_name2)

    # Define similarity levels and explanations
    if similarity_score >= 90:
        similarity_level = "High"
        explanation = "The brand names are very similar."
    elif similarity_score >= 70:
        similarity_level = "Moderate"
        explanation = "The brand names have moderate similarity."
    elif similarity_score >= 50:
        similarity_level = "Low"
        explanation = "The brand names have some similarity, but they are not very close."
    else:
        similarity_level = "Very Low"
        explanation = "The brand names have low similarity."

    # Display the results in a message box
    result_message = f"Similarity between '{brand_name1}' and '{brand_name2}': {similarity_score}%\n" \
                     f"Similarity Level: {similarity_level}\n" \
                     f"Explanation: {explanation}"
    messagebox.showinfo("Brand Name Similarity", result_message)

# Create a Tkinter window
root = tk.Tk()
root.title("Brand Name Similarity Checker")

# Create labels and entry fields
label1 = tk.Label(root, text="Enter Brand Name 1:")
label2 = tk.Label(root, text="Enter Brand Name 2:")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Create a button to trigger the comparison
compare_button = tk.Button(root, text="Compare", command=compare_brand_names)

# Pack the widgets
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
compare_button.pack()

# Start the Tkinter main loop
root.mainloop()

