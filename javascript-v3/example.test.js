import {describe, expect, it, beforeEach, afterEach, test} from 'vitest';

describe("dummy", () => {
    beforeEach(() => {
        console.log('beforeEach');
    })

    afterEach(() => {
        console.log('afterEach');
    })

    test("false is false", () => {
        expect(false).toBeFalsy();
    })
})