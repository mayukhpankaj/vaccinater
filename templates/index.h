<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

    <title>Vaccinator</title> 

    <style>

        
.card-v{
    box-shadow: 0 4px 4px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 90%;
    border-radius: 5px;
    
    color: #474647c9;
    background: rgba(211, 210, 210, 0.288);
   
    
  }
  
  .card-v:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
     
        
  }

  .banner {

    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji" !important; 
  }

  .gbubble {
  
  margin: 40px;
  display: inline-block;
  position: relative;
	width: auto;
	height: auto;
	background-color: #99ff99;
  
  }


  .rbubble {
  
  margin: 40px;
  display: inline-block;
  position: relative;
	width: auto;
	height: auto;
	background-color: #ff9999;
  
  }


 


        .date_block {
            width: 100px;
            height: 150px;
   
            box-shadow: 0 4px 6px -6px black;
        }

        .digit {
            background-color: #ccc;
            width: 100%;
            height: 65%;
            display: flex;
            justify-content: center;
            align-items: center;
          
        }

        div.digit>p {
            font-family: 'Saira Condensed', sans-serif;
            font-size: 4rem;
            color: white;
        }
        .wording {
            margin-top: 10%;
            width: 100%;
            height: 35%;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        div.wording>p {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.25rem;
            color: black;
        }
        div.wording>p ~ p {
            font-family: 'Montserrat', sans-serif;
            font-size: .80rem;
            color: black;
        }


        .datecontainer {
          
            align-items: center;
            justify-content: center;
            padding-left: 25%;
            padding-top: 12%;
            
        }

        #octocat {

          animation: floating 7s ease-in-out infinite;
        }

        @keyframes floating {
          0% {
          
            transform: translateY(0);
          }
        
          50% {
            
            transform: translateY(20px);
          }
        
          100% {
          
            transform: translateY(0);
          }
        }

        .footer {
    bottom: 5px;
    left: 0;
    width: 100%;
    height: 40px;
    background-color: #f8f9fa;
    color: #6c757d;
    text-align: center;
 }

    </style>


  </head>
  <body>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid ">
        
          <a class="navbar-brand" href="/"> &nbsp; Vaccinator</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <a class="nav-link" aria-current="page" href="{{url_for('about')}}">About</a>
            </div>
          </div>
        </div>
      </nav>

    
<div class="container-fluid banner">
<div class="row">

<div class="col-sm-6" style="background-color:lavender;"> 
    <br>
    <center>
     <div id="octocat"><img src='./static/octocat.png' alt='octocat' width="50%" height="60%"></div> 
    </center>






    <br>
</div>
<div class="col-sm-6"style="background-color:lavenderblush;">
 
    <div class="jumbotron jumbotron-fluid">
        <div class="container">
                    <br>
                <h2>Create vaccine alert ! 📢</h2> 
                <div class="col-sm-6 text-justify">  
                <p>
                    Get Notified about vaccine availability in your location on email & sms ✉️!
                    Vaccinator Octocat tracks & sends personalised vaccine info everday.<br>
                    <i>Go get your shot ! 💉</i>
                    <br><br>
                    <a href="{{url_for('home')}}" class="btn btn-success">Notify Me</a>
                </p>

        </div>   
          <br>
        </div>
      </div>



</div>
</div>
</div>


    <div class="container ">


        <br>

  
        <div class="text-center">
        <h4>Vaccination centers in</h4>
        <h5 id="loc" style="color: #ccc;"></h5>
      </div>
        <br>
      


     <div id="panel" class=" mx-auto" style="margin-left: 15%;">
<!-- 
        <div class="card-v col-xs-4">
            <div class="container">
                <b><h5> center </h5></b>
                <p>  address </p> 
                <br>
            </div>
          </div> -->



     </div>







    </div>

    
    <!----->

    <div class="footer">

      <p style="margin-bottom: 3px;"></p><center>Vaccinator Made with ❤️ in India 🇮🇳</center><p></p>
    </div>


    <script>

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


    </script>












    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>


    

<script type='text/javascript' src='https://www.bing.com/api/maps/mapcontrol?key=AhwT4-MdaboX-XaoAc6-ZunQQv0hbUOzw_nu9XUniQ-1844Q7-ZE61nE0cB3vOPC&callback=loadMapScenario' async defer></script>


   
  </body>
</html>