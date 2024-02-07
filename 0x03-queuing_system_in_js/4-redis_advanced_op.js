const redis = require('redis');
const client = redis.createClient();

const hashKey = 'HolbertonSchools';

client.HSET(hashKey, 'Portland', 50, redis.print);
client.HSET(hashKey, 'Seattle', 80, redis.print);
client.HSET(hashKey, 'New York', 20, redis.print);
client.HSET(hashKey, 'Bogota', 20, redis.print);
client.HSET(hashKey, 'Cali', 40, redis.print);
client.HSET(hashKey, 'Paris', 2, redis.print);

client.HGETALL(hashKey, (err, reply) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Hash stored in Redis:');
    console.log(reply);
  }
  client.quit();
});
