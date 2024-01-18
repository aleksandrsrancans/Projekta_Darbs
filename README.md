# **Projekta Darbs**

## Projekta uzdevums
Šī projekta uzdevums ir atvieglot un automatizēt automašīnas meklēšanu izmantojot ss.lv izveidoto meklēšanas sistēmu. Programma darbojas sekojoši: litotājs ievada dažādus parametrus (mašīnas marku, dzinēja tipu un tilpumu, cenu, gadu un ātrumkārbas veidu), tālāk šie parametri tiek izmantoti datu filtrēšanai sākot ar markas izvēli un tālāk tiek izmantoti pārējie parametri, tālāk programma iegūst informāciju par atrastajiem sludinājumiem (sludinājuma tekstu, mašīnas modeli, dzinēja tilpumu, gadu, nobraukumu, cenu un saiti uz pašu sludinājumu), tad šie dati tiek apstrādāti un sakārtoti pārkatāmā tabulā, no kuras lietotājs var apskatīt sludinājumu, kas interesē, un apmeklēt pašu sludinājumu mājaslapā. 

## Izmantošanas pamācība
Programma darbojas izmantojot termināli, tādēļ, lai to izmantotu ir nepieceišams lejupielādēt _main.py_ failu un izmantot kādu programmēšanas aplikāciju kurā to var atvērt (piem. Visual Studio Code). kad fails ir atvērt aplikācijā ir nepieciešams ielādēt kodā izmantotās bibliotēkas, terminālie ievadot sekojošās rindiņas:  
 _pip install selenium_  
 _pip install prettytable_  
 
Vēl arī ir nepieciešama _Chrome_ pārlūkprogramma, ko programma izmanto, lai piekļūtu mājaslapai.  
Kā programma darbojas var apskatīt ***Koda_Darbības_Video.mp4*** 

## Izmantotās bibliotēkas
Galvenā bibliotēka kas tiek izmantota šī projekta kodā ir _**selenium**_. Šajā kodā šī bibliotēka tiek izmantota, lai automatizētu informācijas iegūšanu no mājaslapas (ss.lv). Tā tiek izmantota lai mājaslapā atrastu konkrētus elementus, ievadītu nepieciešamās vērtības, izvālētos nepieciešamās vērtības, kā arī, lai iegūtu datus. No šīs bibliotēkas tiek importēti vairāki moduļi, kas nepieciešami dažādām darbībām mājaslapā. Piemēram, _**webdriver**_, kas tiek izmantots, lai varētu piekļūt pārlūkprogrammai (šajā gadījumā Chrome), tiek izmantos arī _**By**_ modulis, lai mājaslapā atrastu konkrētus elementus izmantojot to ID, klasi vai citus parametrus, kā arī tiek izmantots _**NoSuchElementException**_, kas tiek izmantots, lai apstrādātu kļūdas, kad netiek atrasts nepieciešamais mājaslapas elements.

Otra bibliotēka, kas tiek izmantota ir _**time**_. Šī bibliotēka tiek izmantota, lai ieveistu pauzi un ļautu mājaslapai ieladēties, pirms tajā tiek kaut kas darīts.

Trešā bibliotēka ir _**PrettyTable**_. Šī biblotēka tiek izmantota lai no mājaslapas iegūtos datus apkopotu tabulā un izvadītu terminālī.

## Iespējamie uzlabojumi
Šajā kodā vēl ir daudz iespēju kaut ko mainīt un uzlabot. Daži no iespējamajiem uzlabojumiem būtu:
* Ieviest labāku ievades un meklēšanas kļūdu apstrādi, jo esošā kļūdu apstrāde ignorē daudzas lietotāja ievades kļūdas.
* Izveidot atsevišķu UI programmai, lai tās lietošana būtu ērtāka un arī izskatītos labāk.
* Optimizēt koda darbību. Kods vispār nav optimizēts, kā arī tā pārskatīšana ir sarežģīta.
