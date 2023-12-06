import express from "express";
import { PORT,mongoDBURL } from "./config.js";
import mongoose from "mongoose";
import { Book } from "./models/bookmodel.js";
import { router } from "./routes/booksRoute.js";
import cors from "cors";

const app = express();

app.use(express.json());

//Middleware  for handling CORS Policy
//option1: allow all the origins with default of cors(*)
app.use(cors());
//option2: allow only custom
// app.use(cors(
//     {
//         origin:"http://localhost:3000",
//         methods: ['GET','POST','PUT','DELETE'],
//         allowedHeaders: ['Content-Type'],
//     }
// ));

app.get('/',(request,response)=>{
    console.log(request);
    console.log('your are inside my app'); 
    return response.status(234).send("your are inside my app");
})

app.use('/books', router);

mongoose
    .connect(mongoDBURL)
    .then(()=>{
        console.log("App connect to db");
        app.listen(PORT, ()=> {
            console.group('app is listening at port:'+PORT);
        });
    })
    .catch((error)=>{
        console.log(error);
    });

