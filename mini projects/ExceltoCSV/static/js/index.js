const submit = document.getElementById("submit");
const downloadBtn = document.getElementById("downloadBtn")
let filename = ""

submit.addEventListener("click",event=>{
  event.preventDefault();
  const file = document.getElementById("file");
  const formdata = new FormData()

  formdata.append("file", file.files[0])

  fetch(uploadUrl,{
    method : 'POST',
    body : formdata
  })
  .then(response => response.json())
  .then(data=>{
      console.log(data);
      filename = data.filename;
      result = document.getElementById("result") 
      result.style.color = "Green";
      result.innerText= data.message;
    })
  .catch(console.error)

})

downloadBtn.addEventListener("click", event=>{
  if(filename){
    window.location.href = `${downloadUrl}/${filename}`; 
  }
  else{
    alert("No files to download. First Upload and Convert the file!!")
  }
})
