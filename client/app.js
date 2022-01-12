// function getBathValue() {
//     var uiBathrooms = document.getElementsByName("uiBathrooms");
//     for(var i in uiBathrooms) {
//       if(uiBathrooms[i].checked) {
//           return parseInt(i)+1;
//       }
//     }
//     return -1; // Invalid Value
//   }
  
//   function getBHKValue() {
//     var uiBHK = document.getElementsByName("uiBHK");
//     for(var i in uiBHK) {
//       if(uiBHK[i].checked) {
//           return parseInt(i)+1;
//       }
//     }
//     return -1; // Invalid Value
//   }
  
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var lstasqm = document.getElementById("uiLandShiftingTotalAreaSQM");
    var floortotal = document.getElementById("uiFloorTotal");
    var bsta = document.getElementById("uiBsta");
    var bsr = document.getElementById("uiBsr");
    var bsh = document.getElementById("uiBsh");
    var bsb = document.getElementById("uiBsb");
    var parksqm = document.getElementById("uiParksqm");
    var mainba = document.getElementById("uiMainba");
    var ancba = document.getElementById("uiAncba");
    var balc = document.getElementById("uiBalc");
    var tlu = document.getElementById("uiTlu");
    var tbu = document.getElementById("uiTbu");
    var tpu = document.getElementById("uiTpu");
    var by = document.getElementById("uiBy");
    var district = document.getElementById("uiDistricts");
    var transtype = document.getElementById("uiTransactionTypes");
    var zoning = document.getElementById("uiZoning");
    var floor = document.getElementById("uiFloor");
    var buildingstate = document.getElementById("uiBuildingState");
    var materials = document.getElementById("uiBuildingMaterial");
    var bsc = document.getElementById("uiBuildingStateCompartment");
    var manage = document.getElementById("uiManagementCommittee");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    // use JQuery post call
    $.post(url, {
        lstasqm: parseFloat(lstasqm.value),
        floortotal: parseFloat(floortotal.value),
        bsta: parseInt(bsta.value),
        bsr: parseInt(bsr.value),
        bsh: parseInt(bsh.value),
        bsb: parseInt(bsb.value),
        parksqm: parseFloat(parksqm.value),
        mainba: parseFloat(mainba.value),
        ancba: parseFloat(ancba.value),
        balc: parseFloat(balc.value),
        tlu: parseInt(tlu.value),
        tbu: parseInt(tbu.value),
        tpu: parseInt(tpu.value),
        by: parseInt(by.value),
        district: district.value,
        transtype: transtype.value,
        zoning: zoning.value,
        floor: floor.value,
        buildingstate: buildingstate.value,
        materials: materials.value,
        bsc: bsc.value,
        manage: manage.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " NTD</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_district"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    // $ is for jquery, get is get call to url. In data, you will get that response back
    $.get(url,function(data, status) {
        console.log("got response for get_district request");
        if(data) {
            var district = data.district;
            var uiDistricts = document.getElementById("uiDistricts");
            $('#uiDistricts').empty();
            for(var i in district) {
                var opt = new Option(district[i]);
                // add districts into dropdown
                $('#uiDistricts').append(opt);
            }
        }
    })

    var url = "http://127.0.0.1:5000/get_transtype";
    $.get(url,function(data, status) {
        console.log("got response for get_transtype request");
        if(data) {
            var transtype = data.transtype;
            var uiTransactionTypes = document.getElementById("uiTransactionTypes");
            $('#uiTransactionTypes').empty();
            for(var i in transtype) {
                var opt = new Option(transtype[i]);
                // add districts into dropdown
                $('#uiTransactionTypes').append(opt);
            }
        }
    });

    var url = "http://127.0.0.1:5000/get_zoning"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    // $ is for jquery, get is get call to url. In data, you will get that response back
    $.get(url,function(data, status) {
        console.log("got response for get_zoning request");
        if(data) {
            var zoning = data.zoning;
            var uiZoning = document.getElementById("uiZoning");
            $('#uiZoning').empty();
            for(var i in zoning) {
                var opt = new Option(zoning[i]);
                // add districts into dropdown
                $('#uiZoning').append(opt);
            }
        }
    })

    var url = "http://127.0.0.1:5000/get_floor"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    // $ is for jquery, get is get call to url. In data, you will get that response back
    $.get(url,function(data, status) {
        console.log("got response for get_zoning request");
        if(data) {
            var floor = data.floor;
            var uiFloor = document.getElementById("uiFloor");
            $('#uiFloor').empty();
            for(var i in floor) {
                var opt = new Option(floor[i]);
                // add districts into dropdown
                $('#uiFloor').append(opt);
            }
        }
    })

    var url = "http://127.0.0.1:5000/get_buildingstate"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    // $ is for jquery, get is get call to url. In data, you will get that response back
    $.get(url,function(data, status) {
        console.log("got response for get_zoning request");
        if(data) {
            var buildingstate = data.buildingstate;
            var uiBuildingState = document.getElementById("uiBuildingState");
            $('#uiBuildingState').empty();
            for(var i in buildingstate) {
                var opt = new Option(buildingstate[i]);
                // add districts into dropdown
                $('#uiBuildingState').append(opt);
            }
        }
    })

    var url = "http://127.0.0.1:5000/get_buildingmat"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    // $ is for jquery, get is get call to url. In data, you will get that response back
    $.get(url,function(data, status) {
        console.log("got response for get_buildingmat request");
        if(data) {
            var materials = data.materials;
            var uiBuildingMaterial = document.getElementById("uiBuildingMaterial");
            $('#uiBuildingMaterial').empty();
            for(var i in materials) {
                var opt = new Option(materials[i]);
                // add districts into dropdown
                $('#uiBuildingMaterial').append(opt);
            }
        }
    })

    var url = "http://127.0.0.1:5000/get_bsc"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    // $ is for jquery, get is get call to url. In data, you will get that response back
    $.get(url,function(data, status) {
        console.log("got response for get_bsc request");
        if(data) {
            var bsc = data.bsc;
            var uiBuildingStateCompartment = document.getElementById("uiBuildingStateCompartment");
            $('#uiBuildingStateCompartment').empty();
            for(var i in bsc) {
                var opt = new Option(bsc[i]);
                // add districts into dropdown
                $('#uiBuildingStateCompartment').append(opt);
            }
        }
    })

    var url = "http://127.0.0.1:5000/get_manage"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    // $ is for jquery, get is get call to url. In data, you will get that response back
    $.get(url,function(data, status) {
        console.log("got response for get_manage request");
        if(data) {
            var manage = data.manage;
            var uiManagementCommittee = document.getElementById("uiManagementCommittee");
            $('#uiManagementCommittee').empty();
            for(var i in manage) {
                var opt = new Option(manage[i]);
                // add districts into dropdown
                $('#uiManagementCommittee').append(opt);
            }
        }
    })




  }
  
  window.onload = onPageLoad;