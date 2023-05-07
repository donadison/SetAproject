// rezerwacje
const listaRezerwacji = document.querySelector('.rec-chart-bars');

//pokoje
const listaPokoi = document.querySelector('.rec-chart-ylabels');

//zabawa rezerwacjami
listaRezerwacji.querySelectorAll('li').forEach(rezerwacja => {
    //daty
    const przyjazd = new Date(rezerwacja.dataset.przyjazd);
    const wyjazd = new Date(rezerwacja.dataset.wyjazd);

    //pokoj
    const pokojNr = rezerwacja.dataset.pokoj;

    //rzad tabeli
    const wiersz = listaPokoi.querySelector(`li[data-nr="${pokojNr}"]`);

    // polozenie paska
    rezerwacja.style.width = szerokoscPaska(przyjazd, wyjazd);
    rezerwacja.style.left = pozycjaPaska(przyjazd);
    rezerwacja.style.top = pozycjaPionowa(wiersz);

});

function iloscDni (poczatek, koniec) {
    poczatek.setUTCHours(0,0,0,0);
    koniec.setUTCHours(0,0,0,0);

    const roznica = Number(koniec) - Number(poczatek);
    const dni = roznica/(1000*60*60*24);
    console.log(dni);

    return dni;
}

function szerokoscPaska(przyjazd, wyjazd) {

    const dniWykresu = datyWykresu();
    console.log("szerokoscPaska");
    const dniRezerwacji = iloscDni(przyjazd, wyjazd);

    const szerokosc = (dniRezerwacji/dniWykresu) * 100;

    return `${szerokosc}%`;
}

function pozycjaPaska(przyjazd) {
    const dniOdPoczatku = odPoczatku(przyjazd);

    const elementListy = document.querySelector('.rec-chart-xlabels :first-child');
    const elementStyl = getComputedStyle(elementListy);
    const pozycjaPx = (elementStyl.width).slice(0,2);
    const pozycja = (dniOdPoczatku * pozycjaPx) + 0.5 * pozycjaPx;

    console.log("pozycja ", dniOdPoczatku, pozycjaPx);

    return `${pozycja}px`;
}

function pozycjaPionowa(wiersz) {
    //pierwszy i odstatni wiersz
    const pierwszyPokoj = document.querySelector('.rec-chart-ylabels li:first-child');
    const ostatniPokoj = document.querySelector('.rec-chart-ylabels li:last-child');
    const pierwszyIndeks = pierwszyPokoj.dataset.indeks;
    const ostatniIndeks = ostatniPokoj.dataset.indeks;

    //wiersz rezerwacji
    const wierszIndeks = wiersz.dataset.indeks;

    //wysokosci
    const iloscPokoi = ostatniIndeks - pierwszyIndeks + 1;
    const wysokoscPaska = 1/iloscPokoi * 100;
    const odlegloscPionowa = wierszIndeks * wysokoscPaska;

    return `${odlegloscPionowa}%`;

}

function datyWykresu () {
    const poczatekWykresu = document.querySelector('.rec-chart-xlabels li:first-child');
    const koniecWykresu = document.querySelector('.rec-chart-xlabels li:last-child');
    const pierwszaData = new Date(poczatekWykresu.dataset.dzien);
    const ostatniaData = new Date(koniecWykresu.dataset.dzien);

    console.log("datyWykresu");
    const dni = iloscDni(pierwszaData, ostatniaData);
    return `${dni}`;
}

function odPoczatku (przyjazd) {
    const poczatekWykresu = document.querySelector('.rec-chart-xlabels li:first-child');
    const pierwszaData = new Date(poczatekWykresu.dataset.dzien);

    console.log("odPoczatku");
    const dni = iloscDni(pierwszaData, przyjazd);
    return `${dni}`;
}

// przekazuje nr rezerwacji do okna rezerwacji
function klikRezerwacja(numer) {
    const nazwa = "idreztab-" + numer;
    document.getElementById(`${nazwa}`).submit();
}

Testowa. Linijka. Z. Wstawionymi. Spacjami. Na.Miejscu.
