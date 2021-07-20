const exec = require('child_process').exec;


console.log('test');


exec('pip install jupyter-book', (error, stdout, stderr) => {
    if (error) {
        throw error;
    }

    console.log(stdout)
    console.log(stderr);

    exec('jupyter-book build .', '../',  (err, stdout, stderr) => {
        if (err) {
            throw err;
        }

        console.log(stdout)
        console.log(stderr);
    })

});