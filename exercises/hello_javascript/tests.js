"use strict";

const hello = require("./functions");

function isFunction() {
    return typeof hello === "function";
}

function returnsString() {
    return typeof hello() === "string";
}

function returnsHello() {
    return hello() === "Hello JavaScript!";
}

const testFunctions = [
    isFunction,
    returnsString,
    returnsHello
];

function testMain() {
    let testsOk = 0;
    let success = true;
    for (let test of testFunctions) {
        let msg = "Testing " + test + " ... ";
        if (success) {
            success = test();
        }
        if (success) {
            testsOk++;
            console.error(msg + "ok");
        } else {
            console.error(msg + "fail");
        }
    }
    return {
        totalPoints: testsOk,
        maxPoints: testFunctions.length
    };
}

if (require.main === module) {
    const result = testMain();
    console.log("TotalPoints: ", result.totalPoints);
    console.log("MaxPoints: ", result.maxPoints);
}
