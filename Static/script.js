
// ADD CROP

function addCrop(){

fetch("/add_crop",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
farmer_name:farmer.value,
crop:crop.value,
price:price.value,
quantity:quantity.value,
location:location.value,
phone:phone.value
})
})

.then(res=>res.json())
.then(data=>{
alert("✅ Crop Added Successfully")
})

}


// LOAD CROPS

function loadCrops(){

fetch("/get_crops")
.then(res=>res.json())
.then(data=>{

let html=""

data.forEach(item=>{

html+=`
<div class="crop-card">
<h3>${item.crop}</h3>
<p>👨‍🌾 ${item.farmer_name}</p>
<p>💰 ₹${item.price}</p>
<p>📦 ${item.quantity} Kg</p>
<p>📍 ${item.location}</p>
<p>📞 ${item.phone}</p>
</div>
`

})

document.getElementById("cropList").innerHTML=html

})

}


// PRICE PREDICTION

function predictPrice(){

let cropName=document.getElementById("predictCrop").value

fetch("/predict_price",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({crop:cropName})
})

.then(res=>res.json())
.then(data=>{

if(data.status=="success"){
document.getElementById("predictionResult").innerText="Predicted Market Price: ₹"+data.predicted_price
}
else{
document.getElementById("predictionResult").innerText="Crop Not Found"
}

})

}


// VOICE INPUT

function startVoiceHindi(){

let recognition=new webkitSpeechRecognition()
recognition.lang="hi-IN"
recognition.start()

recognition.onresult=function(event){
document.getElementById("predictCrop").value=event.results[0][0].transcript
}

}

function startVoiceEnglish(){

let recognition=new webkitSpeechRecognition()
recognition.lang="en-IN"
recognition.start()

recognition.onresult=function(event){
document.getElementById("predictCrop").value=event.results[0][0].transcript
}

}
