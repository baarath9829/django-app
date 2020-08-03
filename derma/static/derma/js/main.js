function loader() {
	const input = document.getElementById('inputfile');
	const image = document.getElementById('image');
	const preview = document.getElementById('preview');
	//console.log("called");
	const file = input.files[0];
	if(file){
		const reader = new FileReader();
		image.style.display = 'block';
		preview.style.display = 'none';
		reader.addEventListener("load",function(){
			image.setAttribute("src",this.result);
		});
		reader.readAsDataURL(file);
	}
}
function feedback_yes(){
}
function feedback_no(){
}