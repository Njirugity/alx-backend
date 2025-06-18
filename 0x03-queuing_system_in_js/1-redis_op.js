import { createClient, print } from "redis";
import {promisify} from 'util';

const client = createClient();

client.on('connect', function(){
    console.log("Redis client connected to the server");
})
client.on('error', (err) =>{
    console.log(`Redis client not connected to the server: ${err}`)
});

function setNewSchool(schoolName, value){
    client.set(schoolName, value, print)
}

const get = promisify(client.get).bind(client)

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(error, result) {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
  });
}

displaySchoolValue('ALX');
setNewSchool("ALXSanFrancisco", "100");
displaySchoolValue("ALXSanFrancisco");
