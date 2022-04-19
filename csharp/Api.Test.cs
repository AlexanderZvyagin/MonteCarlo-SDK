using System;                       // Console
using System.Threading.Tasks;       // Task
using System.Text.Json;             // StringContent
using System.Net.Http;              // HttpClient
using NUnit.Framework;

[TestFixture]
public class ApiTests
{
    static string server;

    [SetUp]
    public void Setup()
    {
        server = System.Environment.GetEnvironmentVariable("MC_SERVER") ?? "http://192.168.1.82:8080";
    }

    [Test]
    public async Task api_version()
    {
        using var client = new HttpClient();
        var response = await client.GetStringAsync($"{server}/version");
        Console.WriteLine(response);
    }

    [Test]
    public async Task api_functions()
    {
        using var client = new HttpClient();
        var response = await client.GetStringAsync($"{server}/functions");
        Console.WriteLine(response);
    }

    [Test]
    public async Task api_model()
    {
        string json_data = @"{
            ""TimeStart"":0,
            ""TimeSteps"":2,
            ""NumPaths"":2,
            ""updaters"":[
                {""name"":""IndependentBrownianMotion"",""args"":[],""refs"":[]},
                {""name"":""SimpleBrownianMotion"",""start"":{""value"":0},""args"":[{""value"":-0.1},{""value"":0.1}],""refs"":[]}
            ],
            ""evaluations"":[
                {""time"":2},
                {""time"":5}
            ]
        }";

        var data = new StringContent(json_data, System.Text.Encoding.UTF8, "application/json");
        using var client = new HttpClient();
        var response = await client.PostAsync($"{server}/model", data);
        Console.WriteLine(response);
    }
}
