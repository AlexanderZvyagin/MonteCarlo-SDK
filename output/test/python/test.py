
from __future__ import annotations
import sys, random, uuid
from dto import *

def random_string(len_max:int = 5) -> str:
    return str(uuid.uuid4())[0:random.randint(0,len_max)]

def random_list_string(min:int = 0, max:int = 3) -> list[str]:
    n = random.randint(min,max)
    return [random_string() for i in range(n)]

def random_optional_string (len_max:int=5) -> str|None:
    if yes_no(): return None
    return random_string()

def random_optional_list_string(min:int = 0, max:int = 3) -> list[str]:
    if yes_no(): return None
    return random_list_string(min,max)

def random_int (min = -1000, max = 1000) -> int:
    return random.randint(min,max)

def yes_no () -> bool:
    return random_int(0,1)

def random_optional_int (min = -1000, max = 1000) -> int:
    if yes_no(): return None
    return random_int(min,max)

def random_list_int(min:int = 0, max:int = 3) -> list[int]:
    n = random.randint(min,max)
    return [random_int() for i in range(n)]

def random_optional_list_int(min:int = 0, max:int = 3) -> list[int]|None:
    if yes_no(): return None
    return random_list_int(min,max)

def random_float (min:float = -1e6, max:float = 1e6) -> float:
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_optional_float (min = -1e6, max = 1e6) -> float|None:
    if yes_no(): return None
    return random_int()
    # FIXME
    # return random.uniform(min,max)

def random_list_float (min:int = 0, max:int = 3) -> list[float]:
    n = random.randint(min,max)
    return [random_float() for i in range(n)]

def random_optional_list_float (min = 0, max = 3) -> list[float]|None:
    if yes_no(): return None
    return random_list_float(min,max)


def random_Error ():
    return Error (
        random_optional_string(),
        random_optional_string(),
        random_optional_int(),
        random_optional_list_Error()

    )


def random_optional_Error () -> Error|None:
    if yes_no():
        return None
    return random_Error()


def random_list_Error (min:int = 0, max:int = 3) -> list[Error]:
    size = random.randint(min,max)
    return [random_Error() for i in range(size)]


def random_optional_list_Error (min:int = 0, max:int = 3) -> list[Error]|None:
    if yes_no():
        return None
    return random_list_Error(min,max)


def random_UpdaterDoc ():
    return UpdaterDoc (
        random_string(),
        random_string(),
        random_string(),
        random_string(),
        random_int(),
        random_int()

    )


def random_optional_UpdaterDoc () -> UpdaterDoc|None:
    if yes_no():
        return None
    return random_UpdaterDoc()


def random_list_UpdaterDoc (min:int = 0, max:int = 3) -> list[UpdaterDoc]:
    size = random.randint(min,max)
    return [random_UpdaterDoc() for i in range(size)]


def random_optional_list_UpdaterDoc (min:int = 0, max:int = 3) -> list[UpdaterDoc]|None:
    if yes_no():
        return None
    return random_list_UpdaterDoc(min,max)


def random_UpdaterDto ():
    return UpdaterDto (
        random_string(),
        random_optional_list_int(),
        random_optional_list_float(),
        random_optional_float()

    )


def random_optional_UpdaterDto () -> UpdaterDto|None:
    if yes_no():
        return None
    return random_UpdaterDto()


def random_list_UpdaterDto (min:int = 0, max:int = 3) -> list[UpdaterDto]:
    size = random.randint(min,max)
    return [random_UpdaterDto() for i in range(size)]


def random_optional_list_UpdaterDto (min:int = 0, max:int = 3) -> list[UpdaterDto]|None:
    if yes_no():
        return None
    return random_list_UpdaterDto(min,max)


def random_Updater ():
    return Updater (
        random_string(),
        random_list_int(),
        random_list_float(),
        random_optional_float(),
        random_string()

    )


def random_optional_Updater () -> Updater|None:
    if yes_no():
        return None
    return random_Updater()


def random_list_Updater (min:int = 0, max:int = 3) -> list[Updater]:
    size = random.randint(min,max)
    return [random_Updater() for i in range(size)]


def random_optional_list_Updater (min:int = 0, max:int = 3) -> list[Updater]|None:
    if yes_no():
        return None
    return random_list_Updater(min,max)


def random_IndependentGaussian ():
    return IndependentGaussian (
        random_list_int(),
        random_string()

    )


def random_optional_IndependentGaussian () -> IndependentGaussian|None:
    if yes_no():
        return None
    return random_IndependentGaussian()


def random_list_IndependentGaussian (min:int = 0, max:int = 3) -> list[IndependentGaussian]:
    size = random.randint(min,max)
    return [random_IndependentGaussian() for i in range(size)]


def random_optional_list_IndependentGaussian (min:int = 0, max:int = 3) -> list[IndependentGaussian]|None:
    if yes_no():
        return None
    return random_list_IndependentGaussian(min,max)


def random_CorrelatedGaussian ():
    return CorrelatedGaussian (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    )


def random_optional_CorrelatedGaussian () -> CorrelatedGaussian|None:
    if yes_no():
        return None
    return random_CorrelatedGaussian()


def random_list_CorrelatedGaussian (min:int = 0, max:int = 3) -> list[CorrelatedGaussian]:
    size = random.randint(min,max)
    return [random_CorrelatedGaussian() for i in range(size)]


def random_optional_list_CorrelatedGaussian (min:int = 0, max:int = 3) -> list[CorrelatedGaussian]|None:
    if yes_no():
        return None
    return random_list_CorrelatedGaussian(min,max)


def random_BrownianMotion ():
    return BrownianMotion (
        random_float(),
        random_float(),
        random_float(),
        random_string()

    )


def random_optional_BrownianMotion () -> BrownianMotion|None:
    if yes_no():
        return None
    return random_BrownianMotion()


def random_list_BrownianMotion (min:int = 0, max:int = 3) -> list[BrownianMotion]:
    size = random.randint(min,max)
    return [random_BrownianMotion() for i in range(size)]


def random_optional_list_BrownianMotion (min:int = 0, max:int = 3) -> list[BrownianMotion]|None:
    if yes_no():
        return None
    return random_list_BrownianMotion(min,max)


def random_BrownianMotionRef ():
    return BrownianMotionRef (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    )


def random_optional_BrownianMotionRef () -> BrownianMotionRef|None:
    if yes_no():
        return None
    return random_BrownianMotionRef()


def random_list_BrownianMotionRef (min:int = 0, max:int = 3) -> list[BrownianMotionRef]:
    size = random.randint(min,max)
    return [random_BrownianMotionRef() for i in range(size)]


def random_optional_list_BrownianMotionRef (min:int = 0, max:int = 3) -> list[BrownianMotionRef]|None:
    if yes_no():
        return None
    return random_list_BrownianMotionRef(min,max)


def random_GeometricalBrownianMotion ():
    return GeometricalBrownianMotion (
        random_float(),
        random_float(),
        random_float(),
        random_string()

    )


def random_optional_GeometricalBrownianMotion () -> GeometricalBrownianMotion|None:
    if yes_no():
        return None
    return random_GeometricalBrownianMotion()


def random_list_GeometricalBrownianMotion (min:int = 0, max:int = 3) -> list[GeometricalBrownianMotion]:
    size = random.randint(min,max)
    return [random_GeometricalBrownianMotion() for i in range(size)]


def random_optional_list_GeometricalBrownianMotion (min:int = 0, max:int = 3) -> list[GeometricalBrownianMotion]|None:
    if yes_no():
        return None
    return random_list_GeometricalBrownianMotion(min,max)


def random_GeometricalBrownianMotionRef ():
    return GeometricalBrownianMotionRef (
        random_float(),
        random_int(),
        random_int(),
        random_string()

    )


def random_optional_GeometricalBrownianMotionRef () -> GeometricalBrownianMotionRef|None:
    if yes_no():
        return None
    return random_GeometricalBrownianMotionRef()


def random_list_GeometricalBrownianMotionRef (min:int = 0, max:int = 3) -> list[GeometricalBrownianMotionRef]:
    size = random.randint(min,max)
    return [random_GeometricalBrownianMotionRef() for i in range(size)]


def random_optional_list_GeometricalBrownianMotionRef (min:int = 0, max:int = 3) -> list[GeometricalBrownianMotionRef]|None:
    if yes_no():
        return None
    return random_list_GeometricalBrownianMotionRef(min,max)


def random_ZeroCouponBond ():
    return ZeroCouponBond (
        random_int(),
        random_float(),
        random_string()

    )


def random_optional_ZeroCouponBond () -> ZeroCouponBond|None:
    if yes_no():
        return None
    return random_ZeroCouponBond()


def random_list_ZeroCouponBond (min:int = 0, max:int = 3) -> list[ZeroCouponBond]:
    size = random.randint(min,max)
    return [random_ZeroCouponBond() for i in range(size)]


def random_optional_list_ZeroCouponBond (min:int = 0, max:int = 3) -> list[ZeroCouponBond]|None:
    if yes_no():
        return None
    return random_list_ZeroCouponBond(min,max)


def random_Option ():
    return Option (
        random_int(),
        random_float(),
        random_int(),
        random_string()

    )


def random_optional_Option () -> Option|None:
    if yes_no():
        return None
    return random_Option()


def random_list_Option (min:int = 0, max:int = 3) -> list[Option]:
    size = random.randint(min,max)
    return [random_Option() for i in range(size)]


def random_optional_list_Option (min:int = 0, max:int = 3) -> list[Option]|None:
    if yes_no():
        return None
    return random_list_Option(min,max)


def random_Barrier ():
    return Barrier (
        random_int(),
        random_float(),
        random_float(),
        random_int(),
        random_int(),
        random_float(),
        random_string()

    )


def random_optional_Barrier () -> Barrier|None:
    if yes_no():
        return None
    return random_Barrier()


def random_list_Barrier (min:int = 0, max:int = 3) -> list[Barrier]:
    size = random.randint(min,max)
    return [random_Barrier() for i in range(size)]


def random_optional_list_Barrier (min:int = 0, max:int = 3) -> list[Barrier]|None:
    if yes_no():
        return None
    return random_list_Barrier(min,max)


def random_Polynom ():
    return Polynom (
        random_int(),
        random_list_float(),
        random_string()

    )


def random_optional_Polynom () -> Polynom|None:
    if yes_no():
        return None
    return random_Polynom()


def random_list_Polynom (min:int = 0, max:int = 3) -> list[Polynom]:
    size = random.randint(min,max)
    return [random_Polynom() for i in range(size)]


def random_optional_list_Polynom (min:int = 0, max:int = 3) -> list[Polynom]|None:
    if yes_no():
        return None
    return random_list_Polynom(min,max)


def random_Multiplication ():
    return Multiplication (
        random_list_int(),
        random_float(),
        random_string()

    )


def random_optional_Multiplication () -> Multiplication|None:
    if yes_no():
        return None
    return random_Multiplication()


def random_list_Multiplication (min:int = 0, max:int = 3) -> list[Multiplication]:
    size = random.randint(min,max)
    return [random_Multiplication() for i in range(size)]


def random_optional_list_Multiplication (min:int = 0, max:int = 3) -> list[Multiplication]|None:
    if yes_no():
        return None
    return random_list_Multiplication(min,max)


def random_HistogramAxis ():
    return HistogramAxis (
        random_int(),
        random_int(),
        random_float(),
        random_float()

    )


def random_optional_HistogramAxis () -> HistogramAxis|None:
    if yes_no():
        return None
    return random_HistogramAxis()


def random_list_HistogramAxis (min:int = 0, max:int = 3) -> list[HistogramAxis]:
    size = random.randint(min,max)
    return [random_HistogramAxis() for i in range(size)]


def random_optional_list_HistogramAxis (min:int = 0, max:int = 3) -> list[HistogramAxis]|None:
    if yes_no():
        return None
    return random_list_HistogramAxis(min,max)


def random_Histogram ():
    return Histogram (
        random_HistogramAxis(),
        random_optional_HistogramAxis(),
        random_optional_int(),
        random_optional_list_float()

    )


def random_optional_Histogram () -> Histogram|None:
    if yes_no():
        return None
    return random_Histogram()


def random_list_Histogram (min:int = 0, max:int = 3) -> list[Histogram]:
    size = random.randint(min,max)
    return [random_Histogram() for i in range(size)]


def random_optional_list_Histogram (min:int = 0, max:int = 3) -> list[Histogram]|None:
    if yes_no():
        return None
    return random_list_Histogram(min,max)


def random_EvaluationPoint ():
    return EvaluationPoint (
        random_float(),
        random_optional_list_Histogram()

    )


def random_optional_EvaluationPoint () -> EvaluationPoint|None:
    if yes_no():
        return None
    return random_EvaluationPoint()


def random_list_EvaluationPoint (min:int = 0, max:int = 3) -> list[EvaluationPoint]:
    size = random.randint(min,max)
    return [random_EvaluationPoint() for i in range(size)]


def random_optional_list_EvaluationPoint (min:int = 0, max:int = 3) -> list[EvaluationPoint]|None:
    if yes_no():
        return None
    return random_list_EvaluationPoint(min,max)


def random_Model ():
    return Model (
        random_float(),
        random_int(),
        random_int(),
        random_list_Updater(),
        random_list_EvaluationPoint(),
        random_optional_int(),
        random_optional_float(),
        random_optional_int()

    )


def random_optional_Model () -> Model|None:
    if yes_no():
        return None
    return random_Model()


def random_list_Model (min:int = 0, max:int = 3) -> list[Model]:
    size = random.randint(min,max)
    return [random_Model() for i in range(size)]


def random_optional_list_Model (min:int = 0, max:int = 3) -> list[Model]|None:
    if yes_no():
        return None
    return random_list_Model(min,max)


def random_Result ():
    return Result (
        random_int(),
        random_float(),
        random_float(),
        random_float()

    )


def random_optional_Result () -> Result|None:
    if yes_no():
        return None
    return random_Result()


def random_list_Result (min:int = 0, max:int = 3) -> list[Result]:
    size = random.randint(min,max)
    return [random_Result() for i in range(size)]


def random_optional_list_Result (min:int = 0, max:int = 3) -> list[Result]|None:
    if yes_no():
        return None
    return random_list_Result(min,max)


def random_EvaluationResults ():
    return EvaluationResults (
        random_list_string(),
        random_list_int(),
        random_list_int(),
        random_list_float(),
        random_list_float(),
        random_list_float(),
        random_list_float(),
        random_list_int(),
        random_list_Histogram(),
        random_optional_Model()

    )


def random_optional_EvaluationResults () -> EvaluationResults|None:
    if yes_no():
        return None
    return random_EvaluationResults()


def random_list_EvaluationResults (min:int = 0, max:int = 3) -> list[EvaluationResults]:
    size = random.randint(min,max)
    return [random_EvaluationResults() for i in range(size)]


def random_optional_list_EvaluationResults (min:int = 0, max:int = 3) -> list[EvaluationResults]|None:
    if yes_no():
        return None
    return random_list_EvaluationResults(min,max)


def random_Sum ():
    return Sum (
        random_list_float(),
        random_list_int(),
        random_string()

    )


def random_optional_Sum () -> Sum|None:
    if yes_no():
        return None
    return random_Sum()


def random_list_Sum (min:int = 0, max:int = 3) -> list[Sum]:
    size = random.randint(min,max)
    return [random_Sum() for i in range(size)]


def random_optional_list_Sum (min:int = 0, max:int = 3) -> list[Sum]|None:
    if yes_no():
        return None
    return random_list_Sum(min,max)


def random_SumOfFutureValues ():
    return SumOfFutureValues (
        random_int(),
        random_list_float(),
        random_string()

    )


def random_optional_SumOfFutureValues () -> SumOfFutureValues|None:
    if yes_no():
        return None
    return random_SumOfFutureValues()


def random_list_SumOfFutureValues (min:int = 0, max:int = 3) -> list[SumOfFutureValues]:
    size = random.randint(min,max)
    return [random_SumOfFutureValues() for i in range(size)]


def random_optional_list_SumOfFutureValues (min:int = 0, max:int = 3) -> list[SumOfFutureValues]|None:
    if yes_no():
        return None
    return random_list_SumOfFutureValues(min,max)


def test_round_trip_python(command, struct_name, file1_name, file2_name):
    if command=='build':
        return

    if command=='create':
        if False:
            pass

        elif struct_name=='Error':
            obj1 = random_Error()
            open(file1_name,'w').write(Error_to_json_string(obj1))
            obj2 = Error_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Error)
            assert isinstance(obj2,Error)
            assert obj1==obj2


        elif struct_name=='UpdaterDoc':
            obj1 = random_UpdaterDoc()
            open(file1_name,'w').write(UpdaterDoc_to_json_string(obj1))
            obj2 = UpdaterDoc_from_json_string(open(file1_name).read())
            assert isinstance(obj1,UpdaterDoc)
            assert isinstance(obj2,UpdaterDoc)
            assert obj1==obj2


        elif struct_name=='UpdaterDto':
            obj1 = random_UpdaterDto()
            open(file1_name,'w').write(UpdaterDto_to_json_string(obj1))
            obj2 = UpdaterDto_from_json_string(open(file1_name).read())
            assert isinstance(obj1,UpdaterDto)
            assert isinstance(obj2,UpdaterDto)
            assert obj1==obj2


        elif struct_name=='Updater':
            obj1 = random_Updater()
            open(file1_name,'w').write(Updater_to_json_string(obj1))
            obj2 = Updater_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Updater)
            assert isinstance(obj2,Updater)
            assert obj1==obj2


        elif struct_name=='IndependentGaussian':
            obj1 = random_IndependentGaussian()
            open(file1_name,'w').write(IndependentGaussian_to_json_string(obj1))
            obj2 = IndependentGaussian_from_json_string(open(file1_name).read())
            assert isinstance(obj1,IndependentGaussian)
            assert isinstance(obj2,IndependentGaussian)
            assert obj1==obj2


        elif struct_name=='CorrelatedGaussian':
            obj1 = random_CorrelatedGaussian()
            open(file1_name,'w').write(CorrelatedGaussian_to_json_string(obj1))
            obj2 = CorrelatedGaussian_from_json_string(open(file1_name).read())
            assert isinstance(obj1,CorrelatedGaussian)
            assert isinstance(obj2,CorrelatedGaussian)
            assert obj1==obj2


        elif struct_name=='BrownianMotion':
            obj1 = random_BrownianMotion()
            open(file1_name,'w').write(BrownianMotion_to_json_string(obj1))
            obj2 = BrownianMotion_from_json_string(open(file1_name).read())
            assert isinstance(obj1,BrownianMotion)
            assert isinstance(obj2,BrownianMotion)
            assert obj1==obj2


        elif struct_name=='BrownianMotionRef':
            obj1 = random_BrownianMotionRef()
            open(file1_name,'w').write(BrownianMotionRef_to_json_string(obj1))
            obj2 = BrownianMotionRef_from_json_string(open(file1_name).read())
            assert isinstance(obj1,BrownianMotionRef)
            assert isinstance(obj2,BrownianMotionRef)
            assert obj1==obj2


        elif struct_name=='GeometricalBrownianMotion':
            obj1 = random_GeometricalBrownianMotion()
            open(file1_name,'w').write(GeometricalBrownianMotion_to_json_string(obj1))
            obj2 = GeometricalBrownianMotion_from_json_string(open(file1_name).read())
            assert isinstance(obj1,GeometricalBrownianMotion)
            assert isinstance(obj2,GeometricalBrownianMotion)
            assert obj1==obj2


        elif struct_name=='GeometricalBrownianMotionRef':
            obj1 = random_GeometricalBrownianMotionRef()
            open(file1_name,'w').write(GeometricalBrownianMotionRef_to_json_string(obj1))
            obj2 = GeometricalBrownianMotionRef_from_json_string(open(file1_name).read())
            assert isinstance(obj1,GeometricalBrownianMotionRef)
            assert isinstance(obj2,GeometricalBrownianMotionRef)
            assert obj1==obj2


        elif struct_name=='ZeroCouponBond':
            obj1 = random_ZeroCouponBond()
            open(file1_name,'w').write(ZeroCouponBond_to_json_string(obj1))
            obj2 = ZeroCouponBond_from_json_string(open(file1_name).read())
            assert isinstance(obj1,ZeroCouponBond)
            assert isinstance(obj2,ZeroCouponBond)
            assert obj1==obj2


        elif struct_name=='Option':
            obj1 = random_Option()
            open(file1_name,'w').write(Option_to_json_string(obj1))
            obj2 = Option_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Option)
            assert isinstance(obj2,Option)
            assert obj1==obj2


        elif struct_name=='Barrier':
            obj1 = random_Barrier()
            open(file1_name,'w').write(Barrier_to_json_string(obj1))
            obj2 = Barrier_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Barrier)
            assert isinstance(obj2,Barrier)
            assert obj1==obj2


        elif struct_name=='Polynom':
            obj1 = random_Polynom()
            open(file1_name,'w').write(Polynom_to_json_string(obj1))
            obj2 = Polynom_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Polynom)
            assert isinstance(obj2,Polynom)
            assert obj1==obj2


        elif struct_name=='Multiplication':
            obj1 = random_Multiplication()
            open(file1_name,'w').write(Multiplication_to_json_string(obj1))
            obj2 = Multiplication_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Multiplication)
            assert isinstance(obj2,Multiplication)
            assert obj1==obj2


        elif struct_name=='HistogramAxis':
            obj1 = random_HistogramAxis()
            open(file1_name,'w').write(HistogramAxis_to_json_string(obj1))
            obj2 = HistogramAxis_from_json_string(open(file1_name).read())
            assert isinstance(obj1,HistogramAxis)
            assert isinstance(obj2,HistogramAxis)
            assert obj1==obj2


        elif struct_name=='Histogram':
            obj1 = random_Histogram()
            open(file1_name,'w').write(Histogram_to_json_string(obj1))
            obj2 = Histogram_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Histogram)
            assert isinstance(obj2,Histogram)
            assert obj1==obj2


        elif struct_name=='EvaluationPoint':
            obj1 = random_EvaluationPoint()
            open(file1_name,'w').write(EvaluationPoint_to_json_string(obj1))
            obj2 = EvaluationPoint_from_json_string(open(file1_name).read())
            assert isinstance(obj1,EvaluationPoint)
            assert isinstance(obj2,EvaluationPoint)
            assert obj1==obj2


        elif struct_name=='Model':
            obj1 = random_Model()
            open(file1_name,'w').write(Model_to_json_string(obj1))
            obj2 = Model_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Model)
            assert isinstance(obj2,Model)
            assert obj1==obj2


        elif struct_name=='Result':
            obj1 = random_Result()
            open(file1_name,'w').write(Result_to_json_string(obj1))
            obj2 = Result_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Result)
            assert isinstance(obj2,Result)
            assert obj1==obj2


        elif struct_name=='EvaluationResults':
            obj1 = random_EvaluationResults()
            open(file1_name,'w').write(EvaluationResults_to_json_string(obj1))
            obj2 = EvaluationResults_from_json_string(open(file1_name).read())
            assert isinstance(obj1,EvaluationResults)
            assert isinstance(obj2,EvaluationResults)
            assert obj1==obj2


        elif struct_name=='Sum':
            obj1 = random_Sum()
            open(file1_name,'w').write(Sum_to_json_string(obj1))
            obj2 = Sum_from_json_string(open(file1_name).read())
            assert isinstance(obj1,Sum)
            assert isinstance(obj2,Sum)
            assert obj1==obj2


        elif struct_name=='SumOfFutureValues':
            obj1 = random_SumOfFutureValues()
            open(file1_name,'w').write(SumOfFutureValues_to_json_string(obj1))
            obj2 = SumOfFutureValues_from_json_string(open(file1_name).read())
            assert isinstance(obj1,SumOfFutureValues)
            assert isinstance(obj2,SumOfFutureValues)
            assert obj1==obj2

        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    elif command=='convert':
        if False:
            pass

        elif struct_name=='Error':
            obj = Error_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Error_to_json_string(obj))


        elif struct_name=='UpdaterDoc':
            obj = UpdaterDoc_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(UpdaterDoc_to_json_string(obj))


        elif struct_name=='UpdaterDto':
            obj = UpdaterDto_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(UpdaterDto_to_json_string(obj))


        elif struct_name=='Updater':
            obj = Updater_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Updater_to_json_string(obj))


        elif struct_name=='IndependentGaussian':
            obj = IndependentGaussian_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(IndependentGaussian_to_json_string(obj))


        elif struct_name=='CorrelatedGaussian':
            obj = CorrelatedGaussian_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(CorrelatedGaussian_to_json_string(obj))


        elif struct_name=='BrownianMotion':
            obj = BrownianMotion_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(BrownianMotion_to_json_string(obj))


        elif struct_name=='BrownianMotionRef':
            obj = BrownianMotionRef_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(BrownianMotionRef_to_json_string(obj))


        elif struct_name=='GeometricalBrownianMotion':
            obj = GeometricalBrownianMotion_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(GeometricalBrownianMotion_to_json_string(obj))


        elif struct_name=='GeometricalBrownianMotionRef':
            obj = GeometricalBrownianMotionRef_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(GeometricalBrownianMotionRef_to_json_string(obj))


        elif struct_name=='ZeroCouponBond':
            obj = ZeroCouponBond_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(ZeroCouponBond_to_json_string(obj))


        elif struct_name=='Option':
            obj = Option_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Option_to_json_string(obj))


        elif struct_name=='Barrier':
            obj = Barrier_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Barrier_to_json_string(obj))


        elif struct_name=='Polynom':
            obj = Polynom_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Polynom_to_json_string(obj))


        elif struct_name=='Multiplication':
            obj = Multiplication_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Multiplication_to_json_string(obj))


        elif struct_name=='HistogramAxis':
            obj = HistogramAxis_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(HistogramAxis_to_json_string(obj))


        elif struct_name=='Histogram':
            obj = Histogram_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Histogram_to_json_string(obj))


        elif struct_name=='EvaluationPoint':
            obj = EvaluationPoint_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(EvaluationPoint_to_json_string(obj))


        elif struct_name=='Model':
            obj = Model_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Model_to_json_string(obj))


        elif struct_name=='Result':
            obj = Result_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Result_to_json_string(obj))


        elif struct_name=='EvaluationResults':
            obj = EvaluationResults_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(EvaluationResults_to_json_string(obj))


        elif struct_name=='Sum':
            obj = Sum_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(Sum_to_json_string(obj))


        elif struct_name=='SumOfFutureValues':
            obj = SumOfFutureValues_from_json_string(open(file1_name).read())
            open(file2_name,'w').write(SumOfFutureValues_to_json_string(obj))

        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    elif command=='compare':
        if False:
            pass

        elif struct_name=='Error':
            obj1 = Error_from_json_string(open(file1_name).read())
            obj2 = Error_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='UpdaterDoc':
            obj1 = UpdaterDoc_from_json_string(open(file1_name).read())
            obj2 = UpdaterDoc_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='UpdaterDto':
            obj1 = UpdaterDto_from_json_string(open(file1_name).read())
            obj2 = UpdaterDto_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Updater':
            obj1 = Updater_from_json_string(open(file1_name).read())
            obj2 = Updater_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='IndependentGaussian':
            obj1 = IndependentGaussian_from_json_string(open(file1_name).read())
            obj2 = IndependentGaussian_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='CorrelatedGaussian':
            obj1 = CorrelatedGaussian_from_json_string(open(file1_name).read())
            obj2 = CorrelatedGaussian_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='BrownianMotion':
            obj1 = BrownianMotion_from_json_string(open(file1_name).read())
            obj2 = BrownianMotion_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='BrownianMotionRef':
            obj1 = BrownianMotionRef_from_json_string(open(file1_name).read())
            obj2 = BrownianMotionRef_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='GeometricalBrownianMotion':
            obj1 = GeometricalBrownianMotion_from_json_string(open(file1_name).read())
            obj2 = GeometricalBrownianMotion_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='GeometricalBrownianMotionRef':
            obj1 = GeometricalBrownianMotionRef_from_json_string(open(file1_name).read())
            obj2 = GeometricalBrownianMotionRef_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='ZeroCouponBond':
            obj1 = ZeroCouponBond_from_json_string(open(file1_name).read())
            obj2 = ZeroCouponBond_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Option':
            obj1 = Option_from_json_string(open(file1_name).read())
            obj2 = Option_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Barrier':
            obj1 = Barrier_from_json_string(open(file1_name).read())
            obj2 = Barrier_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Polynom':
            obj1 = Polynom_from_json_string(open(file1_name).read())
            obj2 = Polynom_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Multiplication':
            obj1 = Multiplication_from_json_string(open(file1_name).read())
            obj2 = Multiplication_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='HistogramAxis':
            obj1 = HistogramAxis_from_json_string(open(file1_name).read())
            obj2 = HistogramAxis_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Histogram':
            obj1 = Histogram_from_json_string(open(file1_name).read())
            obj2 = Histogram_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='EvaluationPoint':
            obj1 = EvaluationPoint_from_json_string(open(file1_name).read())
            obj2 = EvaluationPoint_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Model':
            obj1 = Model_from_json_string(open(file1_name).read())
            obj2 = Model_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Result':
            obj1 = Result_from_json_string(open(file1_name).read())
            obj2 = Result_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='EvaluationResults':
            obj1 = EvaluationResults_from_json_string(open(file1_name).read())
            obj2 = EvaluationResults_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='Sum':
            obj1 = Sum_from_json_string(open(file1_name).read())
            obj2 = Sum_from_json_string(open(file2_name).read())
            assert obj1==obj2


        elif struct_name=='SumOfFutureValues':
            obj1 = SumOfFutureValues_from_json_string(open(file1_name).read())
            obj2 = SumOfFutureValues_from_json_string(open(file2_name).read())
            assert obj1==obj2

        else:
            raise Exception(f'Operation "{command}" does not supported struct {struct_name}')
    else:
        raise Exception(f'Not supported command {command}')

