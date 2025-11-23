import pandas as pd
import matplotlib.pyplot as plt
import os

def contacts_chart():
    df = pd.read_json('data/contacts.json')
    counts = df['company'].value_counts()
    plt.figure(figsize=(10,6))
    counts.plot(kind='bar', color='skyblue')
    plt.title('Contacts per Company')
    plt.xlabel('Company')
    plt.ylabel('Number of Contacts')
    os.makedirs('static', exist_ok=True)
    plt.savefig('static/contacts_bar.png')
    plt.close()

def deals_chart():
    df = pd.read_json('data/contacts.json')
    counts = df['company'].value_counts()
    plt.figure(figsize=(8,8))
    counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Contacts per Company (Pie)')
    os.makedirs('static', exist_ok=True)
    plt.savefig('static/contacts_pie.png')
    plt.close()