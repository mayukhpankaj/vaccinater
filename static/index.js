var clat,clon;

        window.onload = function(){

             alert('Please enable location');

            console.log('requesting geolocation');
            
            var userPositionPromise = new Promise(function(resolve, reject) {
            
            if (navigator.geolocation) {
            
                navigator.geolocation.getCurrentPosition(function(data) {
                resolve(data);
                console.log('got permission');
                
                }, function(error) {
                reject(error);
                });
                
            } else {
                reject({
                error: 'browser doesn\'t support geolocation'
                });
            };

            });


            userPositionPromise
            .then(function(data) {
                console.log('storing coords');
                
                console.log(data.coords.latitude);
                console.log(data.coords.longitude);

                clat = data.coords.latitude;
                clon = data.coords.longitude;

                clat = clat.toString();
                clon = clon.toString();


                var state,district,pincode;


        // generating today's date to for Vaccine API 

        var month = new Array();
        month[0] = "January";
        month[1] = "February";
        month[2] = "March";
        month[3] = "April";
        month[4] = "May";
        month[5] = "June";
        month[6] = "July";
        month[7] = "August";
        month[8] = "September";
        month[9] = "October";
        month[10] = "November";
        month[11] = "December";

        var today = new Date();
        var dd = today.getDate();

        month_name = month[today.getMonth()]
        

        var mm = today.getMonth()+1; 
        var yyyy = today.getFullYear();
             if(dd<10) 
            {
                dd='0'+dd;
            } 

            if(mm<10) 
            {
                mm='0'+mm;
            } 
            today = dd+'-'+mm+'-'+yyyy;
            console.log(today);



    geourl = "https://api.opencagedata.com/geocode/v1/json?q="+clat+"%2C"+clon+"&key=3a03ae1a488a43f0a517ac9bdc0c2a8a&language=en&pretty=1&no_annotations=1";


        fetch(geourl)
          .then((res)=>res.json())
          .then((res)=> {

        console.log(res);

        console.log(res.results[0].components.state);
        console.log(res.results[0].components.state_district);

        state = res.results[0].components.state;
        district = res.results[0].components.state_district;
        pincode =  res.results[0].components.postcode;

        console.log(pincode);
        console.log(state,district);

        var lhead = document.getElementById("loc");

        lhead.innerHTML = district+', '+state;




        vaccine_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pincode+"&date="+today
        // vaccine_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=110001&date="+today




                fetch(vaccine_url)
                .then((res1)=>res1.json())
                .then((res1)=> {

                    console.log(res1.centers);

                    for(var data in res1.centers)
                    {

                        var vcenter, vaddress,feetype,age_limit,vname,avail_status,vquantity,vdate;

                        vcenter= res1.centers[data].name;
                        vaddress = res1.centers[data].address + ", "+res1.centers[data].district_name;
                        feetype = res1.centers[data].fee_type;
                        //age_limit = res1.centers[data].

                        console.log(res1.centers[data].sessions)

                        for(var s in res1.centers[data].sessions)
                        {
                            if(res1.centers[data].sessions[s].available_capacity>0){

                                age_limit= res1.centers[data].sessions[s].min_age_limit;

                                vname = res1.centers[data].sessions[s].vaccine;

                                avail_status="Available";

                                vdate = res1.centers[data].sessions[s].date;

                               

                                vquantity = res1.centers[data].sessions[s].available_capacity;

                                var av_html = ` <h6>${vname}</h6> 
                                                 <span> age:  ${age_limit} + </span><span>&ensp; doses: ${vquantity}</span>
                                                 <br>
                                                <p class="gbubble">${avail_status}&ensp;${feetype}</p> `;

                               
                            }
                            else
                            {
                                
                                age_limit= res1.centers[data].sessions[s].min_age_limit;

                                vname = res1.centers[data].sessions[s].vaccine;

                                avail_status="Booked";

                                console.log(vname,age_limit);

                                var bk_html = ` <h6>${vname}</h6>  
                                                <span>age:  ${age_limit}+ </span>
                                                <br>
                                                 <p class="rbubble">${avail_status}</p> <br> `;


                            }

                        

                        }


                        console.log(vcenter);

                        console.log(vaddress);





                        var cards = document.getElementById("panel")

                        if(av_html)
                        {
                            cards.innerHTML += `<div class="card-v col-xs-10 mb-2"><div class="container pt-2">
                                  <div class="row">
                                            <div class="col col-xs-3">
                                              
                                              <div class="datecontainer">
                                                    <div class="date_block">
                                                        <div class="digit">
                                                            <p>${dd}</p>
                                                        </div>
                                                        <div class="wording"><p>${month_name}</p></div>
                                                    </div>
                                                </div>
                                              
                                              
                                              </div>
                                            <div class="col col-xs-9 text-center pl-0">
                                                <b><h6>${vcenter}</h6></b>
                                                <p><small>${vaddress} </small></p>
                                                ${av_html}
                                            </div>
                       </div>
                                            </div></div>`;

                        }
                        else
                        {
                            cards.innerHTML += `<div class="card-v col-xs-10 mb-2"><div class="container pt-2">
                                            <div class="col-x6-4">date</div>
                                            <div class="col-xs-8 text-center">
                                            <b><h6>${vcenter}</h6></b>
                                            <p><small>${vaddress} </small></p>
                                             ${bk_html}
                                             </div>
                                            </div></div>`;


                        }


                    }




                })

      })


         
            })
            .catch(function(error) {
                console.log('Error', error);
                
                alert('Please enable location');
                
            });

        };