
// d3.select("#predict").on("click", function myFunction() {
//    var text = document.getElementById("msg").value;
//    document.getElementById("dom").innerHTML = "DOM:" + text;

//     // var text = document.getElementById('msg').textContent;
//     // var text = range.editAsText() + ''
//     // var text = elements.editAsText()
//     var sentences = text.split('.')
//     var y = 0
//     for (i = 0; i < sentences.length; i++) {
//       var words = sentences[y].split(" ")
//       console.log(words)

//     }
// }
// )




d3.select("#predict").on("click", function changeIt(){
    var srType = d3.select("#msg").node().value;
    console.log(srType)
}
)
    // var ward = d3.select("#selectWard").node().value;
    // // Assign the value of the dropdown menu option to a variable
    // var raw_param = d3.select("#meeting-time").node().value;
    // console.log(raw_param)
    // var stringDate = raw_param.toString()
    // console.log(stringDate)
    // var month = parseFloat(stringDate.slice(5,7))
    // console.log(month)
    // var hour = parseFloat(stringDate.slice(11,13))
    // console.log(hour)