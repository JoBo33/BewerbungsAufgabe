document.addEventListener('DOMContentLoaded', async function () {
    document.getElementById('btn').addEventListener('click', async () => {
        const data = {
            elec_consumption : document.getElementById('elec_consumption').value,
            calc_pv_performance : document.getElementById('calc_pv_performance').value,
            spec_pv_earning: document.getElementById('spec_pv_earning').value,
            self_consumption: document.getElementById('self_consumption').value,
            elec_price: document.getElementById('elec_price').value,
            feed_in_tariff: document.getElementById('feed_in_tariff').value,
            invest_cost: document.getElementById('invest_cost').value,
            anal_period: document.getElementById('anal_period').value,
        }

        const response = await fetch('/', {
            method:'POST',
            headers: {"Content-Type": 'application/json'},
            body: JSON.stringify(data)
        })

        const result = await response.json()

        const calc_output = document.getElementById("calc_output")

        calc_output.innerHTML= `
            <h3>Selber berechnet</h3>
            <p>Jahresertrag: ${result.earning_year} kWh</p>
            <p>Eigenverbrauch in kwh: ${result.self_consumption_kwh} kWh</p>
            <p>einspeisung in kwh: ${result.feed_in_kwh} kWh</p>
            <p>Ersparnis an Strom: ${result.safings_self_consumption} kWh</p>
            <p>Einnahmen durch Einspeisung: ${result.earning_feed_in} kWh</p>
            <p>Jährliche Ersparnis: ${result.total_earning_year} €</p>
            <p>Gesamtkosten: ${result.total_costs} kWh</p>    
            <p>Amortisationszeit: ${result.payback_period} Jahre</p>
        `
        const ai_output = document.getElementById("ai_output")
        ai_output.innerHTML = `
            <h3>AI Analyse</h3>
            <p>${result.ai_analysis}</p>`
        console.log(result)
    })
})