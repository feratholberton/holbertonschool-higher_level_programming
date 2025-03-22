#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
	url = 'https://jsonplaceholder.typicode.com/posts'
	response = requests.get(url)
	
	print(response.status_code)

	if response.status_code == 200:
		posts = response.json()

		for post in posts:
			print(post['title'])
		else:
			print('Failed to get posts.')



def fetch_and_save_posts():
	url = 'https://jsonplaceholder.typicode.com/posts'
	response = requests.get(url)

	if response.status_code == 200:
		posts = response.json()

		saved_data = [{
			'id': post['id'],
			'title': post['title'],
			'body': post['body'],}
			for post in posts
		]

		with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
			writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
			writer.writeheader()
			writer.writerows(saved_data)

		print('Post saved successfully to file')
	else:
		print('Failed to get posts.')