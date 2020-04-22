function loader() {
	const input = document.getElementById('inputfile');
	const image = document.getElementById('image');
	const preview = document.getElementById('image-preview');
	console.log("called");
	const file = input.files[0];
	if(file){
		const reader = new FileReader();
		image.style.dispay = 'block';
		preview.style.display = 'none';
		reader.addEventListner("load",function(){
			image.setAttribute("src",this.result);
		});
		reader.readAsDataURL(file);
	}
}

