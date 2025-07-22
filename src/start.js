const { exec } = require('child_process');
const open = require('open');

const folderToServe = './FormHackSlicer/app'; // change if your code is in another folder
const port = 8000;

// Start http-server
const server = exec(`http-server ${folderToServe} -p ${port}`);

server.stdout.on('data', data => {
  console.log(data);

  // Once server is running, open browser
  if (data.includes('Available on:')) {
    open(`http://localhost:${port}`);
  }
});

server.stderr.on('data', data => {
  console.error(data);
});

process.on('exit', () => {
  server.kill();
});
