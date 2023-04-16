# DevOps22 GitHub Contribution

A fun project counting the GitHub contributions of the DevOps22 students. Hope this will motivate you to contribute more to GitHub.

---

How it looks like:

<img src="img/top5.png" alt="Pie Chart" width=20%/>

---

## How it works

The script does't use the GitHub API. Instead it uses the GitHub website to get the contributions of the students. It uses the `requests` and `BeautifulSoup` libraries to get the HTML code of the GitHub profile page and parse it to get the contributions. The script is running every day at midnight using GitHub Actions. The result is saved in a `csv` file and the `README.md` file is updated with the new list.

---

## How to use

1. Clone the repository
2. Install the requirements
3. Run the script but first change the `username` list to your own list of GitHub usernames

---

## What I learned

- How to use the `requests` library to get the HTML code of a website
- How to use the `BeautifulSoup` library to parse HTML code
- Unfortunatly not everybody is using GitHub much... 😕

---

## TODO

- [ ] Add matplotlib to show the contributions in a bar chart
- [ ] Use the GitHub API to get the contributions, when the package gets fixed/updated.
- [x] Use GitHub Actions to run the script every day and update the README.md file
- [x] Add a pie chart with the top 5 students

---

## Webpage

See the last list updated every midnight [here](https://alexroman777.github.io/DevOps22/).

---

Back to [Python Projects](/README.md)
