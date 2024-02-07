const redis = require('redis');
const client = redis.createClient();

const setNewSchool = async(schoolName, value) => {
  await client.SET(schoolName, value, redis.print);
};

const displaySchoolValue = async(schoolName) => {
  const value = await client.GET(schoolName);
  console.log(value);
};
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

