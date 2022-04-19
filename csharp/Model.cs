using System.Collections.Generic;   // List
using System;                       // Console
using System.Net.Http;              // HttpClient
using System.Threading.Tasks;       // Task
using System.Text.Json;             // JsonSerializer
using System.Text.Json.Serialization;
using NUnit.Framework;

public class Parameter {
    [JsonConstructor]
    public Parameter(
        string Name="",
        double Value=double.NaN,
        double Step=double.NaN,
        double Min=double.NaN,
        double Max=double.NaN
    ) {
        name = Name;
        value = Value;
        step = Step;
        min = Min;
        max = Max;
    }
    public string name { get; set; }
    public double value { get; set; }
    public double step { get; set; }
    public double min { get; set; }
    public double max { get; set; }
}

public class EvaluationPoint {
    public EvaluationPoint (
        int _state=-1,
        double _time=double.NaN,
        double _value=double.NaN,
        double _error=double.NaN
    ) {
        state = _state;
        time = _time;
        value = _value;
        error = _error;
    }
    public int state { get; set; }
    public double time { get; set; }
    public double value { get; set; }
    public double error { get; set; }
}

public class Updater {
    public Updater(
        string _name,
        List<Parameter> _args = null,
        List<int> _refs = null
    ){
        name = _name;
        args = _args ?? new List<Parameter> {};
        refs = _refs ?? new List<int> {};
    }
    public Updater(
        string _name,
        Parameter _start,
        List<Parameter> _args = null,
        List<int> _refs = null
    ){
        name = _name;
        start = _start;
        args = _args ?? new List<Parameter> {};
        refs = _refs ?? new List<int> {};
    }
    public string name { get; set; }

    public Parameter? start { get; set; } = null;

    public List<Parameter> args { get; set; }

    public List<int> refs { get; set; }
}

public class Model {
    
    public double TimeStart { get; set; } = 0;
    public int TimeSteps { get; set; } = 1;
    public int NumPaths { get; set; } = 1;
    public List<Updater> updaters { get; set; } = new List<Updater> {};
    public List<EvaluationPoint> evaluations { get; set; } = new List<EvaluationPoint> {};
}

public class Statistics {
    [JsonConstructor]
    public Statistics(
        int N=0,
        double Mean = double.NaN,
        double Stddev = double.NaN,
        double Skewness = double.NaN
    ){
        n = N;
        mean = Mean;
        stddev = Stddev;
        skewness = Skewness;
    }
    public int n;
    public double mean { get; set; }
    public double stddev { get; set; }
    public double skewness { get; set; }

    public double meanError => stddev/Math.Sqrt(n);

    public string ToString (){
        return $"n={n} mean={mean}+/-{meanError} stddev={stddev} skewness={skewness}";
    }
}

public class Results {

    [JsonConstructor]
    public Results (
        List<string> Names = null,
        List<int>    Npaths = null,
        List<double> Mean = null,
        List<double> Stddev = null,
        List<double> Skewness = null,
        List<double> Time_points = null,
        List<int>    Time_steps = null
    ) {
        names       = Names       ?? new List<string> {};
        npaths      = Npaths      ?? new List<int>    {};
        mean        = Mean        ?? new List<double> {};
        stddev      = Stddev      ?? new List<double> {};
        skewness    = Skewness    ?? new List<double> {};
        time_points = Time_points ?? new List<double> {};
        time_steps  = Time_steps  ?? new List<int>    {};
    }

    public List<string> names { get; set; }
    public List<int> npaths { get; set; }
    public List<double> mean { get; set; }
    public List<double>  stddev { get; set; }
    public List<double> skewness { get; set; }
    public List<double> time_points { get; set; }
    public List<int> time_steps { get; set; }
    
    public int StatesCount => names.Count;
    public int PointsCount => time_points.Count;

    public void Print(){
        Console.WriteLine($"The results table has {names.Count} states evaluated at {time_points.Count} time point(s).");
        for(int point=0; point<PointsCount; point++)
            for(int state=0; state<StatesCount; state++)
                Console.WriteLine($"[{state}] {names[state]} time={time_points[point]} {StatisticsOfStatePoint(state,point).ToString()}");
    }

    public Statistics StatisticsOfStatePoint(int state,int point){
        if(state<0 || state>=StatesCount || point<0 || point>=PointsCount)
            throw new ArgumentException();
        int id = state+point*StatesCount;
        return new Statistics(npaths[id],mean[id],stddev[id],skewness[id]);
    }
}

// https://github.com/dotnet/runtime/issues/40140
public class DoubleConverter : JsonConverter<double>
{
    public override double Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if( (reader.TokenType == JsonTokenType.String && reader.GetString() == "NaN")
            || reader.TokenType == JsonTokenType.Null
        ){ 
            return double.NaN;
        }

        return reader.GetDouble(); // JsonException thrown if reader.TokenType != JsonTokenType.Number
    }

    public override void Write(Utf8JsonWriter writer, double value, JsonSerializerOptions options)
    {
        if (double.IsNaN(value))
        {
            writer.WriteNullValue();
        }
        else
        {
            writer.WriteNumberValue(value);
        }
    }
}

static public class Helper {
    static public JsonSerializerOptions GetJsonSerializerOptions(){
        var options = new JsonSerializerOptions {
            Converters = { new DoubleConverter() }
        };
        return options;
    }

    static public async Task<Results> RunAsync (Model model,string server) {
        // 1. convert 'model' to JSON
        // 2. send it to the server
        // 3. get back the JSON response
        // 4. deserealize JSON response into model result
        // 5. return the result
        // string model_json = JsonSerializer.Serialize<Model>(model);
        var model_json = JsonSerializer.Serialize<Model>(model,Helper.GetJsonSerializerOptions());
        using var client = new HttpClient();
        var response = await client.PostAsync(
            $"{server}/model",
            new StringContent(model_json, System.Text.Encoding.UTF8, "application/json")
        );
        string data = response.Content.ReadAsStringAsync().Result;
        // Console.WriteLine("MODEL RESPONSE:");
        // Console.WriteLine(data);
        return JsonSerializer.Deserialize<Results>(data,Helper.GetJsonSerializerOptions());
    }

    static public Results Run (Model model,string server) {
        Task<Results> r = RunAsync(model,server);
        return r.Result;
    }
}

[TestFixture]
public class SerializationTests {
    [TestCase(0)]
    [TestCase(double.NaN)]
    public void TestSerializationOfParameter(double value){
        var options = Helper.GetJsonSerializerOptions();
        var p1 = new Parameter("MyParameter",value,1,2,3);
        var p1_js = JsonSerializer.Serialize<Parameter>(p1,options);
        Console.WriteLine($"{p1_js}");
        var p2 = System.Text.Json.JsonSerializer.Deserialize<Parameter>(p1_js,options);
    }
}