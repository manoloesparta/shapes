from bs4 import BeautifulSoup
import requests

for i in range(1, 129):
    url = f'https://trivia.fyi/page/{i}'
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'lxml')
    articles = soup.find_all('article')

    questions_list = []
    answers_list = []

    for single in articles:
        question = single.div.header.h2.a.text
        questions_list.append(question)
        
        answer = single.find('div', class_='su-spoiler-content su-clearfix').text
        answers_list.append(answer)

    data = zip(questions_list, answers_list)

    for question, answer in data:
        with open('data.txt', mode='a') as file:
            to_write = f'Question: {question}, Answer: {answer}\n'
            file.write(to_write)