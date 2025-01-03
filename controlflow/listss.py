# list comprehensions

# capitalized_cities = [city.title() for city in cities]

# squares = [x**2 for x in range(9) if x % 2 == 0]

models = ["Logistic Regression", "Decision Tree", "Random Forest", "Support Vector Machine", "Naive Bayes"]
model_acronyms = [model[:2].upper() for model in models]
print(model_acronyms)

### Notebook grading
correct_answer = ['LR', 'DT', 'RF', 'SVM', 'NB']
if model_acronyms == correct_answer:
    print("Good job!")
else:
    print("Not quite! Did you create the acronyms correctly?")