const diagrammeCirculaire = document.querySelector(".diagrammeCirculaire")
const rayon = 100

diagrammeCirculaire.setAttribute("width", 3*rayon)
diagrammeCirculaire.setAttribute("height", 3*rayon)
diagrammeCirculaire.setAttribute("viewBox", `${-1.5*rayon} ${-1.5*rayon} ${3*rayon} ${3*rayon}`)

const data = [{nom: 'Python', valeur: 70, couleur: 'blue'},
              {nom: 'Data', valeur: 10, couleur: 'green'},
              {nom: 'Web', valeur: 10, couleur: 'red'},
              {nom: 'Archi', valeur: 10, couleur: 'orange'},]
var somme = data.reduce((acc, elt) => acc+elt.valeur, 0)

function calculerAngle(valeur) {
    return 2 * Math.PI * valeur/somme
}

function conversionPolaireCartesien(angle, rayon) {
    return {x: rayon*Math.cos(angle), y: rayon*Math.sin(angle)};
}

function tracerSecteur(element, valeurDecallage) {
    const angleDebut = calculerAngle(valeurDecallage)
    const angleFin = angleDebut + calculerAngle(element.valeur)
    const {x: xA, y: yA} = conversionPolaireCartesien(angleDebut, rayon)
    const {x: xB, y: yB} = conversionPolaireCartesien(angleFin, rayon)
    const path = document.createElementNS('http://www.w3.org/2000/svg',"path");
    path.setAttributeNS(null, 'd', `M ${xA} ${yA} A ${rayon} ${rayon} 0 ${2*element.valeur>somme?1:0} 1 ${xB} ${yB}`)
    path.style.stroke = element.couleur
    path.style.fill = "none"
    path.style.strokeWidth = 0.5*rayon
    diagrammeCirculaire.appendChild(path)
    path.addEventListener("click", event => handleClick(element, path))
}

function handleClick(element, path) {
    const div = document.getElementById(element.nom)
    for (const element of data) {
        document.getElementById(element.nom).style.display = "none"
    }
    div.style.display = "flex"
    document.getElementById("vide").style.display = "none"
    Array.from(diagrammeCirculaire.children).forEach(path => path.style.transform = 'none')
    path.style.transform = 'scale(1.1)'
}

var valeurDecallage = 0
for (const element of data) {
    tracerSecteur(element, valeurDecallage)
    valeurDecallage += element.valeur
    document.getElementById(element.nom).style.display = "none"
}
