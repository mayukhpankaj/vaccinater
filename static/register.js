
  window.onload = populateSelect();

  function populateSelect() {

      // CREATE AN XMLHttpRequest OBJECT, WITH GET METHOD.
      var xhr = new XMLHttpRequest(), 
          method = 'GET',
          overrideMimeType = 'application/json',
          url = 'https://cdn-api.co-vin.in/api/v2/admin/location/states';        // ADD THE URL OF THE FILE.

      xhr.onreadystatechange = function () {
          if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
              
              // PARSE JSON DATA.
              var data = JSON.parse(xhr.responseText);

              console.log(data['states'])

              states = data['states']

              var ele = document.getElementById('sel_state');
              for (var i = 0; i < states.length; i++) {
                  // BIND DATA TO <select> ELEMENT.
                  ele.innerHTML = ele.innerHTML +
                      '<option value="' + states[i]['state_id']  + '">' + states[i]['state_name'] + '</option>';
              }
          }
      };
      xhr.open(method, url, true);
      xhr.send();
  }

  function show(ele) {
      // GET THE SELECTED VALUE FROM <select> ELEMENT AND SHOW IT.

      var state_id = ele.value;

      var xhr = new XMLHttpRequest(), 
          method = 'GET',
          overrideMimeType = 'application/json',
          url = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/'+state_id;        // ADD THE URL OF THE FILE.

      xhr.onreadystatechange = function () {
          if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
              
              // PARSE JSON DATA.
              var data = JSON.parse(xhr.responseText);

              console.log(data['districts'])

              districts = data['districts']

              var dis = document.getElementById('sel_district');
              for (var i = 0; i < districts.length; i++) {
                  // BIND DATA TO <select> ELEMENT.
                  dis.innerHTML = dis.innerHTML +
                      '<option value="' + districts[i]['district_id']  + '">' + districts[i]['district_name'] + '</option>';
              }
          }
      };
      xhr.open(method, url, true);
      xhr.send();




      
      var msg = document.getElementById('msg');
      var dis = document.getElementById('sel_district');
      msg.innerHTML = 'Selected state : <b>' + ele.options[ele.selectedIndex].text + '</b> </br>' +
          'ID: <b>' + ele.value + '</b>'+'<br> Selected district '+dis.options[dis.selectedIndex].text+' id: '+dis.value;

      dis.innerHTML = '<option value="">-- Select --</option>'



  }
