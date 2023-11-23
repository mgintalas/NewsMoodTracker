import subprocess

# List of your script commands
scripts = [
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/15min.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/alfa.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/bernardinai.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/delfi.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/lrt.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/lrytas.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/respublika.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/tv3.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/ve.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/scraper/vz.py',
    'python c:/Users/ITWORK/Desktop/Code/Sentiment/nlp/sentiment.py'
]

for script in scripts:
    subprocess.run(script, shell=True)  # Use shell=True carefully; it's a security hazard if input isn't sanitized
