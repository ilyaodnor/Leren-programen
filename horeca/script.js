// Prijzen van drankjes en snacks
const prijzen = {
    fris: 2.50,
    bier: 3.00,
    wijn: 4.00,
    bitterballen8: 5.00,
    bitterballen16: 9.00,
    frikandel: 2.50,
};

// Variabelen om bestellingen op te slaan
let bestellingen = [];

// Functie om bestellingen toe te voegen
function voegBestellingToe(drank, aantal) {
    bestellingen.push({ drank, aantal });
}

// Functie om de rekening te tonen
function toonRekening() {
    let totaalPrijs = 0;
    let rekeningTekst = "<h2>Uw rekening:</h2>";

    bestellingen.forEach(bestelling => {
        const { drank, aantal } = bestelling;
        const prijs = prijzen[drank] ? prijzen[drank] : 0;
        rekeningTekst += `<p>${aantal} x ${drank.charAt(0).toUpperCase() + drank.slice(1)}: €${(prijs * aantal).toFixed(2)}</p>`;
        totaalPrijs += prijs * aantal;
    });

    rekeningTekst += `<h3>Totaal: €${totaalPrijs.toFixed(2)}</h3>`;
    document.getElementById('rekening').innerHTML = rekeningTekst;
}

// Functie om drankjes te bestellen
function bestelDrankjes() {
    const drankjes = ['fris', 'bier', 'wijn'];

    let bestelling = prompt("Welke bestelling wilt u toevoegen? (fris, bier, wijn of stop om te stoppen)");

    while (bestelling.toLowerCase() !== 'stop') {
        if (drankjes.includes(bestelling.toLowerCase())) {
            let aantal = parseInt(prompt(`Hoeveel ${bestelling} wilt u toevoegen aan uw bestelling?`));
            voegBestellingToe(bestelling.toLowerCase(), aantal);
        } else {
            alert("U heeft een ongeldige invoer gedaan. Uw bestelling kan niet worden toegevoegd.");
        }
        bestelling = prompt("Welke bestelling wilt u toevoegen? (fris, bier, wijn of stop om te stoppen)");
    }

    toonRekening();
}

// Start de bestellingsmodule
document.getElementById('startButton').addEventListener('click', bestelDrankjes);

// Functie om snacks te bestellen
function bestelSnacks() {
    const snacks = ['bitterballen', 'frikandel', 'pizza'];

    let bestelling = prompt("Welke bestelling wilt u toevoegen? (snack)");

    if (bestelling.toLowerCase() === 'snack') {
        let snackKeuze = prompt("Welke snack wilt u bestellen? (frikandel, bitterballen, pizza)");

        if (snackKeuze.toLowerCase() === 'pizza') {
            let slices = parseInt(prompt("In hoeveel slices wilt u de pizza snijden? (1-12)"));
            if (slices >= 1 && slices <= 12) {
                voegBestellingToe('pizza', slices);
            } else {
                alert("U kunt alleen een keuze maken tussen 1 en 12.");
            }
        } else if (snackKeuze.toLowerCase() === 'bitterballen') {
            let aantal = prompt("Hoeveel bitterballen wilt u toevoegen (8 of 16)?");
            if (aantal === '8') {
                voegBestellingToe('bitterballen8', 1);
            } else if (aantal === '16') {
                voegBestellingToe('bitterballen16', 1);
            } else {
                alert("U kunt alleen een keuze maken tussen 8 en 16. De snacks zijn niet toegevoegd aan de bestelling.");
            }
        } else if (snackKeuze.toLowerCase() === 'frikandel') {
            voegBestellingToe('frikandel', 1);
        } else {
            alert("Sorry dat hebben we niet.");
        }
    } else {
        alert("Ongeldige invoer, terug naar het hoofdmenu.");
    }
}

// Start de snack module bij het klikken op de bestellingsknop
document.getElementById('startButton').addEventListener('click', bestelSnacks);
