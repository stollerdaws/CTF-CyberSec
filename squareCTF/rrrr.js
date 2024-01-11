const timestampStr = process.argv[2];
const formattedTimestampStr = timestampStr.replace(/-/g, 'T') + 'Z'; // Format to ISO 8601

const timestamp = new Date(formattedTimestampStr).getTime() / 1000;

let seed = timestamp;

function lcgRandom() {
    const a = 1664525;
    const c = 1013904223;
    const m = 2 ** 32;
    seed = (a * seed + c) % m;
    return seed / m;
}

function generateSeededRandomNumbers(count) {
    const numbers = [];
    for (let i = 0; i < count; i++) {
        numbers.push(Math.floor(lcgRandom() * 4294967296));
    }
    return numbers;
}

const randomNumbers = generateSeededRandomNumbers(48);
console.log(randomNumbers);
