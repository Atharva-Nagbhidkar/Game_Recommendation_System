# Game Recommendation System

This project is a content-based game recommendation system that utilizes natural language processing techniques to recommend similar games based on their attributes such as name, developer, genre, publisher, critic score, and user score.

## Introduction

This content-based recommendation system leverages a dataset containing various attributes of games to recommend similar games. It uses natural language processing techniques such as text preprocessing, stemming, and vectorization to transform the data into a suitable format for similarity computation.

## Dataset

The dataset used in this project contains the following attributes for each game:
- Name
- Developer
- Genre
- Publisher
- Critic Score
- User Score

## Data Preprocessing

The preprocessing steps involved:
1. Importing the dataset and selecting relevant parameters.
2. Handling missing values and ensuring consistency in attribute formats.

## Feature Engineering

All selected attributes were consolidated into a single column called `tags` to treat all textual data uniformly.

## Text Processing

1. Converted the text in the `tags` column to lowercase to ensure case insensitivity.
2. Applied Porter Stemmer to extract root words and normalize the text.

## Vectorization

Used `CountVectorizer` to convert the processed textual data into numerical vectors. Each unique word (or stem) became a feature in this representation.

## Similarity Calculation

Computed similarity scores between game vectors using cosine similarity, which measures the cosine of the angle between two vectors, providing a measure of similarity irrespective of their magnitude.

## Recommender Function

Developed a function that takes the name of a game as input and identifies the top 5 similar games based on their attributes.

## Usage

To use the recommendation system, follow these steps:

1. Input the name of a game.
2. The system will output a list of 5 recommended games that are most similar to the input game.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Atharva-Nagbhidkar/Game_Recommendation_System.git
2. Navigate to the project directory:
   ```sh
    cd Game_Recommendation_System
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
