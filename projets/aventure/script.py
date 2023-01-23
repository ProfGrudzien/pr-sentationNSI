from time import sleep

def demander_choix(A, B, C, D) :
    reponse = ""
    while reponse == "" :
        reponse = input("Quel est votre choix ? ")
        if reponse != A and reponse != B and reponse != C and reponse != D :
            print("Ce choix n'est pas permis.")
            reponse = ""
        else :
            return reponse

def depart(intro = True) :
    if intro :
        print("Vous venez de vous réveiller dans une pièce sombre et humide. Il fait très noir et vous avez froid.")
        print("Que voulez-vous faire ?")
    print("  A : vous lever et parcourir la pièce à tâtons.")
    print("  B : fouiller vos poches.")
    print("  C : vous frotter les bras pour vous réchauffer.")
    choix = demander_choix("A", "B", "C", None)
    if choix == "A" :
        a_taton()
    if choix == "B" :
        poches()
    if choix == "C" :
        se_frotter(depart)
    
def se_frotter(page) :
    print("La sensation de chaleur vous réconforte un peu, mais aussitôt que vous vous arrêtez, l'ambiance glaciale de la pièce vous saisie de nouveau.")
    print("Il fait toujours aussi froid et noir dans la pièce, que voulez vous faire ?")
    page(False)

def poches(intro = True) :
    if intro :
        print("En fouillant vos poches, vous trouvez un stylo, un paquet de cigarette presque vide et un briquet.")
        print("Que voulez vous faire ?")
    print("  A : vous lever et parcourir la pièce à tâtons.")
    print("  B : allumer le briquet pour scruter la pièce.")
    print("  C : fumer une cigarette.")
    print("  D : vous frotter les bras pour vous réchauffer.")
    choix = demander_choix("A", "B", "C", "D")
    if choix == "A" :
        a_taton()
    if choix == "B" :
        briquet()
    if choix == "C" :
        cigarette()
    if choix == "D" :
        se_frotter(poches)

def cigarette(intro = True) :
    if intro :
        print("Vous sortez une cigarette de ce paquet et vous tentez de l'allumer avec le briquet. Des étincelles jaillissent, mais vous n'arrivez pas à obtenir de flamme. Par habitude, vous secouez le briquet et tentez de nouveau de l'allumer. Cette fois ci c'est la bonne, la petite flamme vous permet d'allumer la cigarette.")
        print("Dès les premières bouffées, vous vous rappelez cette bonne résolution : vous avez promis d'arrêter la cigarette.")
        print("Il fait toujours aussi froid et noir dans la pièce, que voulez vous faire ?")
    print("  A : vous lever et parcourir la pièce à tâtons.")
    print("  B : allumer le briquet pour scruter la pièce.")
    print("  C : vous frotter les bras pour vous réchauffer.")
    choix = demander_choix("A", "B", "C", None)
    if choix == "A" :
        a_taton()
    if choix == "B" :
        briquet_vide()
    if choix == "C" :
        se_frotter(cigarette)

def briquet(intro = True) :
    if intro :
        print("Des étincelles jaillissent, mais vous n'arrivez pas à obtenir de flamme. Par habitude, vous secouez le briquet et tentez de nouveau de l'allumer. Cette fois ci c'est la bonne, la petite flamme vous permet de distinguer ce que vous cherchiez : une porte juste en face de vous. La flamme s’éteint, il n'y a plus de gaz dans le briquet...")
        print("Il fait toujours aussi froid et noir dans la pièce, que voulez vous faire ?")
    print("  A : vous lever et parcourir la pièce à tâtons.")
    print("  B : vous lever et avancer dans le noir en direction de la porte.")
    print("  C : vous frotter les bras pour vous réchauffer.")
    choix = demander_choix("A", "B", None, None)
    if choix == "A" :
        a_taton()
    if choix == "B" :
        porte()
    if choix == "C" :
        se_frotter(briquet)

def briquet_vide(intro = True) :
    if intro :
        print("Vous tentez de nouveau d'allumer votre briquet, mais cette fois ci, vous n'arrivez pas à allumer ne serait-ce qu'une toute petite flamme.")
        print("Il fait toujours aussi froid et noir dans la pièce, que voulez vous faire ?")
    print("  A : vous lever et parcourir la pièce à tâtons.")
    print("  B : vous frotter les bras pour vous réchauffer.")
    choix = demander_choix("A", "B", None, None)
    if choix == "A" :
        a_taton()
    if choix == "B" :
        se_frotter(briquet_vide)
    
def a_taton(intro = True) :
    print("Vous parcourez la pièce à tâtons. Alors que vous vous déplacez prudemment, vous sentez subitement le sol se dérober sous vos pieds. La chute vous paraît interminable, vous savez qu'elle vous sera fatale.")
    print("Fin de la partie, vous avez perdu !")

def porte(intro = True) :
    print("Vous avancer dans le noir en direction de la porte.")
    print("A tâtons, vous trouvez la poignée")
    print("Vous espérez que la porte n'est pas verrouillée lorsque vous exercez une pression sur cette poignée...")
    sleep(3)
    print("Hourra ! La porte s'ouvre, vous voilà délivré")
    print("Fin de la partie, vous avez gagné !")
    print("Donnez une note entre 1 et 5 à ce jeu :")
    choix = demander_choix('5', None, None, None)
    print("Merci beaucoup, à bientôt pour de nouvelles aventures !")
    
depart()
