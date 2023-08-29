import fetch from "node-fetch"

export async function run (model:Model, server:string) {
    return fetch(
        `${server}/model`,
        {
            method: 'post',
            body: JSON.stringify(model)
        }
    ).then(async result => {
        const json = await result.json();
        return json;
    })
}
