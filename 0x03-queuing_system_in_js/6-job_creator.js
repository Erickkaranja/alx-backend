const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0793561574',
  message: 'GoodMorning',
};

const job = queue.create('push_notification_code', jobData);

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
job.save(() => {
  console.log(`Notification job created: ${job.id}`);
});
