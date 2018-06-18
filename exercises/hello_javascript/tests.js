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
    let testsRun = 0;
    testFunctions.forEach(test => {
        let msg = "Testing " + test + " ... ";
        if (test()) {
            msg += "ok";
            testsOk++;
        } else {
            msg += "fail";
        }
        console.error(msg);
        testsRun++;
    });
    return {
        totalPoints: testsOk,
        maxPoints: testsRun
    };
}

if (require.main === module) {
    const result = testMain();
    console.log("TotalPoints: ", result.totalPoints);
    console.log("MaxPoints: ", result.maxPoints);
}
