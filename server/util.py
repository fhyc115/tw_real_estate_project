import json
import pickle
import numpy as np

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
        buildingstate.index = __data_columns.index(buildingstate.lower())
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
    x[0] = lstasqm
    x[1] = floortotal
    x[2] = bsta
    x[3] = bsr
    x[4] = bsh
    x[5] = bsb
    x[6] = parksqm
    x[7] = mainba
    x[8] = ancba
    x[9] = balc
    x[10] = tlu
    x[11] = tbu
    x[12] = tpu
    x[13] = by

    # setting district_index = 1
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
    return round(__model.predict([x])[0], 2)

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
        __districts = __data_columns[14:26]
        __transactiontype = __data_columns[26:29]
        __zoning = __data_columns[29:38]
        __floor = __data_columns[38:87]
        __buildingstate = __data_columns[87:96]
        __buildingmat = __data_columns[96:111]
        __compyesno = __data_columns[111:113]
        __management = __data_columns[113:115]

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
    print(get_estimated_price(8.65, 13, 41, 1, 1, 1, 0, 26, 0.7, 0, 1, 1, 0, 2020, 'district_Wenshan District', 'transaction type_land and building', 'zoning_urban:other', 'floor_8', 'building state_Apartment (within 10F w/ Elevator)', 'main building materials_SRC', 'building situation - compartment_Yes', 'management committee_Yes'))
    print(get_estimated_price(8.65, 13, 41, 1, 1, 1, 0, 26, 0.7, 0, 1, 1, 0, 2021, 'district_Wenshan District', 'transaction type_land and building', 'zoning_urban:other', 'floor_8', 'building state_Apartment (within 10F w/ Elevator)', 'main building materials_SRC', 'building situation - compartment_Yes', 'management committee_Yes'))

