express = require("express")
app = express()

app.get('/',(req,res)=>{
    res.send("ok")
})
app.post("/",(req,res)=>{
    console.log (req.body)
    res.send(true)
})
app.listen(3000,console.log("Acceptation ready"))