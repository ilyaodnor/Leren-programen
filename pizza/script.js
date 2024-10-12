// Prijzen voor elke pizzagrootte
const pizzaPrijzen = {
    small: 6.50,
    medium: 8.50,
    large: 12.00
};

/**
 * Functie om het totaalbedrag te berekenen en te tonen
 */
function berekenTotaal() {
    // Ophalen van het aantal bestelde pizza's per grootte
    const aantalSmall = parseInt(document.getElementById('small').value);
    const aantalMedium = parseInt(document.getElementById('medium').value);
    const aantalLarge = parseInt(document.getElementById('large').value);

    // Berekenen van de totale kosten per pizzagrootte
    const totaalSmall = aantalSmall * pizzaPrijzen.small;
    const totaalMedium = aantalMedium * pizzaPrijzen.medium;
    const totaalLarge = aantalLarge * pizzaPrijzen.large;

    // Berekenen van de totale prijs van alle pizza's
    const totaalPrijs = totaalSmall + totaalMedium + totaalLarge;

    // Leegmaken van de resultatensectie voor nieuwe berekening
    const resultaatDiv = document.getElementById('resultaat');
    resultaatDiv.innerHTML = '';

    // Resultaten weergeven alleen als er pizza's besteld zijn
    if (aantalSmall > 0) {
        resultaatDiv.innerHTML += `<p>Small pizza's: ${aantalSmall} x €${pizzaPrijzen.small.toFixed(2)} = €${totaalSmall.toFixed(2)}</p>`;
    }
    if (aantalMedium > 0) {
        resultaatDiv.innerHTML += `<p>Medium pizza's: ${aantalMedium} x €${pizzaPrijzen.medium.toFixed(2)} = €${totaalMedium.toFixed(2)}</p>`;
    }
    if (aantalLarge > 0) {
        resultaatDiv.innerHTML += `<p>Large pizza's: ${aantalLarge} x €${pizzaPrijzen.large.toFixed(2)} = €${totaalLarge.toFixed(2)}</p>`;
    }

    // Als er pizza's besteld zijn, toon het totaalbedrag
    if (totaalPrijs > 0) {
        resultaatDiv.innerHTML += `<h3>Totaal: €${totaalPrijs.toFixed(2)}</h3>`;
        document.getElementById('resultaat-section').style.display = 'block'; // Toon het resultaat
    } else {
        resultaatDiv.innerHTML += `<p>Je hebt geen pizza's geselecteerd.</p>`;
    }
}

// Voegt het huidige jaar automatisch toe aan de footer
document.getElementById('jaar').textContent = new Date().getFullYear();
