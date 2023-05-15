"""Ο σκοπός της εργασίας είναι να αυτοματοποιήσουμε αυτή τη λειτουργία ανάκτησης των διαφορετικών σελίδων με δεδομένα και να δημιουργήσουμε το πρόγραμμα datagov.py το οποίο θα ζητά :

α) Το ερώτημα, έστω ότι πληκτρολογούμε περιβάλλον 

(Προσοχή, καθώς επιστρέφεται διαφορετικό σύνολο δεδομένων όταν είναι όλα τα γράμματα του όρου αναζήτησης κεφαλάια. Επίσης, αν τυχόν έχετε προβλήματα με την κωδικοποίηση τότε μια λύση είναι να χρησιμοποιήσετε τη συνάρτηση quote η οποία περιέχεται στο module urllib.parse που πρέπει να συμπεριλάβετε στα εξωτερικά modules του προγράμματος σας όπως αναλύθηκε στη διαδικτυακή μας συνεδρία (Δείτε εδώ ένα παράδειγμα λύσης: http://stackoverflow.com/questions/11818362/how-to-deal-with-unicode-string-in-url-in-python3)

β) Τη σελίδα έναρξης, έστω ότι πληκτρολογούμε 2
γ) την τελική σελίδα, έστω ότι πληκτρολογούμε 4

Το πρόγραμμα, στο συγκεκριμένο παράδειγμα, θα δημιουργεί 3 αρχεία με ονόματα

page2.html
page3.html
page4.html

όπου το καθένα θα περιέχει τα αποτελέσματα ανά σελίδα σχετικά με το ερώτημα με αρχή τη σελίδα έναρξης  (είναι η β' πληροφορία)
"""




import urllib.request 
from urllib.parse import quote
central_url="http://archive.data.gov.gr/dataset?q=%CE%A0%CE%B5%CF%81%CE%B9%CE%B2%CE%B1%CE%BB%CE%BB%CE%BF%CE%BD"
search_word=input("Εισαγωγή αναζητησης:")
temp_page=central_url+quote(search_word)
first=int(input("Εισαγωγη πρωτης σελιδας:"))
last=int(input("Εισαγωγη τελευταιας σελιδας:"))

for page in range(first,last+1):
    final_page=temp_page+"&page="+str(page)
    response=urllib.request.urlopen(final_page)
    dataentry=response.read()
    storefile=open("page"+str(page)+"html","wb")
    storefile.write(dataentry)
    storefile.close()


