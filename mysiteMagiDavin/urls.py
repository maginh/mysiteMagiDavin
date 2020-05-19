"""mysiteMagiDavin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

#path() argument: route
#route è una stringa che contiene un url. Quando si richiede l'elaborazione di una richiesta, 
#Django inizia dal primo url per poi scorrere con tutti i seguenti, confrontando ogni url richiesto 
#con ogni url inserito nella relativa sezione fin a trovare una corrispondenza con .urlpatterns

#argomento path(): view
#Quando Django trova una corrispondenza con gli url chiama la funzione di visualizzazione specificata con 
#Http Request come primo argomento e tutti i valori "acquisiti" dalla route come argomenti di parola chiave. 

#argomento path(): kwargs
#Gli argomenti di parola chiave vengono passati in un "dizionario" per poi essere visualizzati alla destinazione.

#argomento path(): name
#Denominare l'URL consente di farvi riferimento senza ambiguità da altre parti di Django, specialmente all'interno 
# dei modelli. Questa potente funzionalità consente di apportare modifiche globali ai modelli di URL del progetto, toccando solo un singolo file.


#$ python manage.py makemigrations polls
#Eseguendo il comando sopra riportato, si vuole apportare delle modifiche ai vari modelli e che si desidera che le modifiche vengano archiviate come migrazione.

#$ python manage.py sqlmigrate polls 0001
#Il comando sopra riportato riceve i nomi delle restituzioni e restituisce il codice SQL.

#hardcoded
#Con gli hardcoded diventa difficile apportare delle modifiche agli URL dei progetti con molti dati e modelli.
#Però dato che è stato definito l'argomento name nei path() è possibile rimuovere una dipendenza da percorsi URL 
#specifici definiti nelle configurazioni URL.

#namespacing
#Nei progetti Django reali, ci potrebbero essere cinque, dieci, venti applicazioni o più. In che modo Django 
# distingue i nomi url tra di loro? Ad esempio, l'app ha una visualizzazione, così come un'app sullo stesso 
# progetto che è per un blog.
#consiste nell'aggiungere spazi dei nomi all'URLLconf. Nel file, andare avanti e aggiungere un per impostare lo 
# spazio dei nomi dell'applicazione:In the file, go ahead and add an to set the application namespace:polls/urls.pyapp_name

#request.POST
#è un oggetto simile a un dizionario che consente di accedere ai dati inviati in base al nome della chiave. 
# In questo caso, restituisce l'ID della scelta selezionata, come stringa. richiesta. I valori POST sono sempre 
# stringhe.request.POST['choice']

#reverse()
#Questa funzione consente di evitare di dover codificare un URL nella funzione di visualizzazione. Viene assegnato
#  il nome della visualizzazione a cui si desidera passare il controllo e la parte variabile del modello di URL 
# che punta a tale visualizzazione.