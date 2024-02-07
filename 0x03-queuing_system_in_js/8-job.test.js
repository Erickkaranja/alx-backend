const { expect } = require('chai');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ redis: { port: 6379, host: '127.0.0.1' } });
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    const invalidCall = () => createPushNotificationsJobs('invalid', queue);
    expect(invalidCall).to.throw('Jobs is not an array');
  });

  it('should create a job for each item in the jobs array', () => {
    const jobs = [
      { phoneNumber: '123', message: 'Message 1' },
      { phoneNumber: '456', message: 'Message 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('should log a message when a job is created', () => {
    const jobs = [{ phoneNumber: '123', message: 'Message' }];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
  });

});
