// Set constraints for the video stream
var constraints = { video: { facingMode: "user" }, audio: false };
var track = null;

    //var firebaseConfig = {
    //apiKey: 'AIzaSyCxrQzDNrYKkB-WqinKQ68fDhtQbStCt5A',
    //authDomain: '<your-auth-domain>',
    //databaseURL: '<your-database-url>',
    //storageBucket: '<your-storage-bucket-url>'
  //};
  //firebase.initializeApp(firebaseConfig);

  // Get a reference to the storage service, which is used to create references in your storage bucket
  //var storage = firebase.storage(); 

// Define constants
const cameraView = document.querySelector("#camera--view"),
    cameraOutput = document.querySelector("#camera--output"),
    cameraSensor = document.querySelector("#camera--sensor"),
    cameraTrigger = document.querySelector("#camera--trigger");

    // AIzaSyCxrQzDNrYKkB-WqinKQ68fDhtQbStCt5A

// Access the device camera and stream to cameraView
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
            track = stream.getTracks()[0];
            cameraView.srcObject = stream;
        })
        .catch(function(error) {
            console.error("Oops. Something is broken.", error);
        });
}

// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function() {
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    cameraOutput.src = cameraSensor.toDataURL();
    cameraOutput.classList.add("taken");
    console.log(cameraOutput.src);
    // Canvas2Image.saveAsPNG(cameraOutput.src);
    var aLink = document.createElement('a');
    var evt = document.createEvent("HTMLEvents");
    evt.initEvent("click");
    aLink.download = 'image.png';
    aLink.href = cameraOutput.src;
    var download = document.createElement('a');
    download.href = image.png;
    download.download = 'image.png';
    download.click();
    console.log(download.click);
    aLink.dispatchEvent(evt);
    // track.stop();
};



// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);


// Install ServiceWorker
if ('serviceWorker' in navigator) {
  console.log('CLIENT: service worker registration in progress.');
  navigator.serviceWorker.register( '/camera-app/part-2/sw.js' , { scope : ' ' } ).then(function() {
    console.log('CLIENT: service worker registration complete.');
  }, function() {
    console.log('CLIENT: service worker registration failure.');
  });
} else {
  console.log('CLIENT: service worker is not supported.');
}