import json
import pickle
import numpy as np

__by = None
__districts = None
__transactiontype = None
__zoning = None
__floor = None
__buildingstate = None
__buildingmat = None
__compyesno = None
__management = None

__data_columns = None
__model = None

def get_estimated_price(lstasqm, floortotal, bsta, bsr, bsh, bsb, parksqm, mainba, ancba, balc, tlu, tbu, tpu, by, district, transtype, zoning, floor, buildingstate, materials, bsc, manage):
    # can't use np.where b/c python list
    # don't have train.columns but have __data_columns which is simple python list
    # train.columns was np array
    # if element is not fun, index() will throw an error. So wrap with try catch block
    try:
        by_index = __data_columns.index(by.lower())
    except:
        by_index = -1
    try:
        district_index = __data_columns.index(district.lower())
    except:
        district_index = -1
    try:
        transtype_index = __data_columns.index(transtype.lower())
    except:
        transtype_index = -1
    try:
        zoning_index = __data_columns.index(zoning.lower())
    except:
        zoning_index = -1
    try:
        floor_index = __data_columns.index(floor.lower())
    except:
        floor_index = -1
    try:
        buildingstate_index = __data_columns.index(buildingstate.lower())
    except:
        buildingstate_index = -1
    try:
        materials_index = __data_columns.index(materials.lower())
    except:
        materials_index = -1
    try:
        bsc_index = __data_columns.index(bsc.lower())
    except:
        bsc_index = -1
    try:
        manage_index = __data_columns.index(manage.lower())
    except:
        manage_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = np.log1p(lstasqm)
    x[1] = np.log1p(floortotal)
    x[2] = np.log1p(bsta)
    x[3] = np.log1p(bsr)
    x[4] = np.log1p(bsh)
    x[5] = np.log1p(bsb)
    x[6] = np.log1p(parksqm)
    x[7] = np.log1p(mainba)
    x[8] = np.log1p(ancba)
    x[9] = np.log1p(balc)
    x[10] = np.log1p(tlu)
    x[11] = np.log1p(tbu)
    x[12] = np.log1p(tpu)

    # setting district_index = 1
    if by_index >= 0:
        x[by_index] = 1
    if district_index >= 0:
        x[district_index] = 1
    if transtype_index >= 0:
        x[transtype_index] = 1
    if zoning_index >= 0:
        x[zoning_index] = 1
    if floor_index >= 0:
        x[floor_index] = 1
    if buildingstate_index >= 0:
        x[buildingstate_index] = 1
    if materials_index >= 0:
        x[materials_index] = 1
    if bsc_index >= 0:
        x[bsc_index] = 1
    if manage_index >= 0:
        x[manage_index] = 1

    # input in predict is 2 dimensional array called x
    # get 2 dimensional array back, since array only has 1 element can access [0] location
    # in that element and will give us the estimated price
    # going to be float, so round to 2 decimal places
    return round(np.expm1(__model.predict([x])[0]), 2)

def get_build_year():
    return __by

def get_district_names():
    return __districts

def get_transaction_type():
    return __transactiontype

def get_zoning():
    return __zoning

def get_floor():
    return __floor

def get_buildingstate():
    return __buildingstate

def get_buildingmat():
    return __buildingmat

def get_compyesno():
    return __compyesno

def get_management():
    return __management

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __by
    global __districts
    global __transactiontype
    global __zoning
    global __floor
    global __buildingstate
    global __buildingmat
    global __compyesno
    global __management
    global __model

    with open("./artifacts/columns.json", "r") as f:
        # whatever's loading will be converted into dict
        __data_columns = json.load(f)["data_columns"]
        # use python index slicing to get elements from list

        __districts = __data_columns[13:25]
        __transactiontype = __data_columns[25:28]
        __zoning = __data_columns[28:37]
        __floor = __data_columns[37:51]
        __buildingstate = __data_columns[51:60]
        __buildingmat = __data_columns[60:75]
        __compyesno = __data_columns[75:77]
        __management = __data_columns[77:79]
        __by = __data_columns[79:92]

    with open("./artifacts/tw_home_price_model.pickle", "rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_district_names())
    print(get_transaction_type())
    print(get_zoning())
    print(get_floor())
    print(get_buildingstate())
    print(get_buildingmat())
    print(get_compyesno())
    print(get_management())
    print(get_build_year())
    print(get_estimated_price(8.65, 13, 41, 1, 1, 1, 0, 26, 0.7, 0, 1, 1, 0, 'build year_2011', 'district_Wenshan District', 'transaction type_land and building', 'zoning_urban:other', 'floor_8', 'building state_Apartment (within 10F w/ Elevator)', 'main building materials_SRC', 'building situation - compartment_Yes', 'management committee_Yes'))


