<?php
highlight_file(__FILE__);
$command = $_GET['command'] ?? '';

if($command === '') {
    die("Please provide a command\n");
}

function filter($command) {
    if(preg_match('/(`|\.|\$|\/|a|c|s|require|include)/i', $command)) {
        return false;
    }
    return true;
}

if(filter($command)) {
    eval($command);
    echo "Command executed";
} else {
    echo "Restricted characters have been used";
}
echo "\n";
?>
shaktictf{y0u_byp4553d_7h3_f1l73r5_y4y} Command executed 