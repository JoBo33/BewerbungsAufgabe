import express from "express"
import path from 'path'
import { execSync } from 'child_process';
import fs from 'fs';

const app = express()
const port = 3000

app.use(express.json());
app.use('/', express.static(path.join(import.meta.dirname, 'public')))

app.post('/', (req, res) => {
    fs.writeFileSync('data.json', JSON.stringify(req.body))
    const output = execSync('py modules/analysis.py')
    console.log(output.toString())
    const result = JSON.parse(output.toString())

    res.json(result)
})

app.listen(port, () => console.log("Listening on port: " + port))