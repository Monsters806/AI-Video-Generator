async function generateStory(){

const topic=document.getElementById("topic").value;
const story=document.getElementById("story");

story.innerHTML="Generating...";

const response=await fetch("/generate",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
topic:topic
})
});

const data=await response.json();

if(data.story){
story.innerHTML=data.story;
}else{
story.innerHTML="Error: "+JSON.stringify(data);
}

}
