import { createClient } from 'redis';

const client = createClient();

client.on('connect', function () {
    console.log('Redis client connected to the server');
});

client.on('error', function (error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.subscribe('ALXchannel');

client.on('message', function (channel, message) {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('ALX');
    client.end(true);
  }
});
